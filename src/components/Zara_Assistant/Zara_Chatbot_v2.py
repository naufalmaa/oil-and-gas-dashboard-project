import pandas as pd
from dash import Dash, html, Input, Output, ctx, State, dcc, dash_table
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns
from ...components.Zara_Assistant import openai_api_key
from ..Zara_Assistant import prompt

import pandas as pd
import time
# import prompt

# from langchain_community.llms import OpenAI
# from langchain_experimental.agents import create_pandas_dataframe_agent
from openai import OpenAI

import plotly.express as px

import re

from io import StringIO
import os

openai_api_key_ = openai_api_key.KEY
os.environ["OPENAI_API_KEY"] = openai_api_key_

client = OpenAI(api_key=openai_api_key_)

conv_hist = []

def contains_word(text, word_list):
    for word in word_list:
        if text.find(word) != -1:
            return True
    return False

word_list = ['table', 'summary', 'summarize', 'rangkum', 'rangkuman']
plot_list = ['plot', 'graph']

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

def generate_prompt(df, question):
    # Generate insights
    insights = []

    # Basic DataFrame Information
    insights.append(
        f"The DataFrame contains {len(df)} rows and {len(df.columns)} columns."
    )
    insights.append("Here are the first 5 rows of the DataFrame:\n")
    insights.append(df.head().to_string(index=False))

    # Summary Statistics
    insights.append("\nSummary Statistics:")
    insights.append(df.describe().to_string())

    # Column Information
    insights.append("\nColumn Information:")
    for col in df.columns:
        insights.append(f"- Column '{col}' has {df[col].nunique()} unique values.")

    # Missing Values
    missing_values = df.isnull().sum()
    insights.append("\nMissing Values:")
    for col, count in missing_values.items():
        if count > 0:
            insights.append(f"- Column '{col}' has {count} missing values.")

    # Most Common Values in Categorical Columns
    categorical_columns = df.select_dtypes(include=["object"]).columns
    for col in categorical_columns:
        top_value = df[col].mode().iloc[0]
        insights.append(f"\nMost common value in '{col}' column: {top_value}")

    insights_text = "\n".join(insights)

    # Compliment and Prompt
    prompt = (
        "You are a master project manager, data analyst, and also petroleum engineer in oil and gas industry named Zara, who an assistant that has a lot of knowledge and experience with project management."
        "The questions about arbitrary datasets. The user's question will be provided. Ensure you "
        "answer the user's question accurately and given the context of the dataset. The user "
        "will use the results of your commentary to work on a project management or to research the data. "
        "If the user's question doesn't make sense, feel free to make a witty remark about user's question."
        "Your response should use Markdown markup. Limit your response to only 1-3 sentences. Address the"
        "user directly as they can see your response. If user asking about your name, respond it with saying your name, Zara."
        "You can provide tabular data by generating the code <code> for viewing the previous data in pandas if necessary, in the format requested. The solution should be given using pandas and only pandas in python. Do not use other source. Return the code <code> in the following format '''python <code>'''."
        "You can also provide data visualization by generating the code <code> the previous data in plotly, in the format requested. The solution should be given using plotly and only plotly in python. Do not use matplotlib or other source. Return the code <code> in the following format '''python <code>'''."

    )

    prompt = f"{prompt}\n\nContext:\n\n{insights_text}\n\nUser's Question: {question}"

    return prompt

# filtering code of python
def extract_python_code(text):
    pattern = r'```python\s(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if not matches:
        return None
    else:
        return matches[0]
    
def safe_exec(code, globals=None, locals=None):
    exec_globals = globals if globals else {}
    exec_locals = locals if locals else {}
    exec(code, exec_globals, exec_locals)
    return exec_locals

# rendering code

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.RESPONSE_CHAT, 'children'),
        Output(ids.ZARA_CHAT_AREA, "value"),
        Input(ids.ZARA_SUBMIT_BUTTON, 'n_clicks'),
        Input(ids.MEMORY_OUTPUT, 'data'),
        State(ids.ZARA_CHAT_AREA, "value"),
        State(ids.RESPONSE_CHAT, 'children'),
        State("checkbox-plotting", "checked"),
        State("checkbox-pandasai", "checked"),
    )
    
    def update_convo(n, data, question, cur, plotting_enabled, query_enabled):
        if question:
            df = pd.DataFrame(data)
            prompt_content = prompt.generate_prompt(df, question)

            messages = [
                {"role": "system", "content": "You are Zara, a master project manager and data analyst in the oil and gas industry. Answer the user's questions about arbitrary datasets accurately, using the context provided. Use Markdown for formatting and limit your response to 1-3 sentences unless generating code. Provide tabular data using pandas or data visualization using plotly. For example: '''python <code>'''"},
                {"role": "user", "content": prompt_content}
            ]

            if query_enabled:
                messages.append({"role": "assistant", "content": """
                    Generate the code <code> for creating dataframe of the previous data in pandas python,
                    in the format requested. The solution should be given using pandas
                    and only pandas. Do not use other sources.
                    Return the code <code> in the following
                    format ```python <code>```.
                    Remember, always put the result with variable of <df_result>.
                    Always assume the data source comes from the variable of <df>, do not use other variable.
                """})

            if plotting_enabled:
                messages.append({"role": "assistant", "content": """
                    Generate the code <code> for plotting the previous data in plotly,
                    in the format requested. The solution should be given using plotly
                    and only plotly. Do not use matplotlib.
                    Return the code <code> in the following
                    format ```python <code>```.
                    Remember, always put the result with variable of <fig>.
                    Always assume the data source comes from the variable of <df>, do not use other variable.
                """})

            completion = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                temperature=0.0,
                max_tokens=4000,
                top_p=0.5
            )
            
            print(completion.choices[0].message.content)
            code = extract_python_code(completion.choices[0].message.content)
            if code is None:
                question = [
                    dcc.Markdown(question, className="chat-item question"),
                    dcc.Markdown(completion.choices[0].message.content, className="chat-item answer")
                ]
                return (question + cur if cur else question), None
            else:
                import_statement = "import pandas as pd\nimport plotly.express as px\n"
                code_with_import = import_statement + code
                
                # Execute the generated code safely
                exec_globals = {"df": df, "px": px}
                exec_locals = safe_exec(code_with_import, globals=exec_globals)
                
                # Initialize the outputs to default values
                graph_output = None
                data_output = None

                # Determine the type of output and render appropriately
                if "fig" in exec_locals:
                    fig = exec_locals["fig"]
                    graph_output = dcc.Graph(figure=fig)
                    # data_output = ""
                elif "df_result" in exec_locals:
                    result_df_series = exec_locals["df_result"]
                    
                    # Check if the DataFrame has a non-default index
                    if result_df_series.index.name or result_df_series.index.names:
                        result_df_series = result_df_series.reset_index()
                        
                    result_df = pd.DataFrame(result_df_series)
                    # graph_output = ""
                    data_output = dash_table.DataTable(
                        columns=[{"name": i, "id": i} for i in result_df.columns],
                        data=result_df.to_dict('records'),
                        style_cell={'padding': '5px'},
                        style_header={
                            'backgroundColor': '#C0C0C0',
                            'fontWeight': 'bold'
                        },
                        export_format='xlsx',
                    )
                else:
                    graph_output = html.Div("No valid output generated.")
                    data_output = html.Div("No valid output generated.")

                question = [
                    dcc.Markdown(question, className="chat-item question"),
                    # dcc.Markdown(completion.choices[0].message.content, className="chat-item answer"),
                ]
                # Conditionally add graph_output and data_output to question
                if graph_output is not None:
                    question.append(html.Div(children=[graph_output], className="chat-item answer"))
                if data_output is not None:
                    question.append(html.Div(children=[data_output], className="chat-item answer"))
                    
                
                return (question + cur if cur else question), None
        else:
            return [], None

    return html.Div(
        className=cns.ZARA_CHAT_INPUT,
        children=[
            dmc.Textarea(
                className=cns.ZARA_CHAT_AREA,
                id=ids.ZARA_CHAT_AREA,
                placeholder='Write your question here...',
                autosize=False,
                minRows=2,
                maxRows=2,
                variant='default',
                radius='lg',
                debounce=True
            ),
            dmc.Checkbox(id="checkbox-plotting", label="Enable plotting"),
            dmc.Checkbox(id="checkbox-pandasai", label="Enable query"),
            html.Div(className=cns.ZARA_SUBMIT_BUTTON,
                     children=[
                         dmc.ActionIcon(
                             DashIconify(icon='formkit:submit', width=25),
                             id=ids.ZARA_SUBMIT_BUTTON,
                             radius='md',
                             size=60,
                             variant='subtle',
                             color='gray',
                             n_clicks=0
                         )
                     ])
        ]
    )
