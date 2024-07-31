import pandas as pd
from dash import Dash, html, Input, Output, ctx, State, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from ...data.source import DataSource
from ...components import ids, cns
from ...components.Zara_Assistant import openai_api_key

import pandas as pd
import time
# import prompt

from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

import chartgpt as cg

from io import StringIO
import os

openai_api_key = openai_api_key.KEY
os.environ["OPENAI_API_KEY"] = openai_api_key

conv_hist = []

def contains_word(text, word_list):
    for word in word_list:
        if text.find(word) != -1:
            return True
    return False

word_list = [
    'table', 'summary', 'summarize', 'rangkum', 'rangkuman'
    ]
# plot_list = ['plot', 'graph']

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table

def generate_prompt(df, question):
    # # Limit the DataFrame size to prevent token overflow
    # max_rows = 10
    # max_cols = 5
    
    # if len(df) > max_rows:
    #     df = df.head(max_rows)
    
    # if len(df.columns) > max_cols:
    #     df = df.iloc[:, :max_cols]
        
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
    )

    prompt = f"{prompt}\n\nContext:\n\n{insights_text}\n\nUser's Question: {question}"

    return prompt

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.RESPONSE_CHAT, 'children'),
        Input(ids.ZARA_SUBMIT_BUTTON, 'n_clicks'),
        State(ids.ZARA_CHAT_AREA, 'value'),
        Input(ids.MEMORY_OUTPUT, 'data')
    )
    
    def update_convo(n, human_prompt, data_chosen):
        button_click = ctx.triggered_id
        global conv_hist
        
        if button_click == ids.ZARA_SUBMIT_BUTTON:
            time.sleep(1)
            
            df = pd.DataFrame(data_chosen)
            # prompt_content = prompt.generate_prompt

            # if contains_word(human_prompt.lower(), word_list):
<<<<<<< HEAD
            #     agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            #     chatbot_resp = agent.run(human_prompt)
=======
            #     prompt = generate_prompt(df, human_prompt)  # Generate prompt using the function
            #     # print(prompt)
            #     agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            #     print(agent)
            #     chatbot_resp = agent.run(prompt)  # Use the generated prompt
            #     print(chatbot_resp) # Print
>>>>>>> c3539ed3b5360adf57107c6e3f28e703c01114ee
                
            #     bot_table_output = f"{chatbot_resp}"
            #     df_ = pd.read_csv(StringIO(bot_table_output), delim_whitespace=True, header=0, index_col=0)
            #     df_.transpose()
            #     df_.reset_index(inplace=True)
                
            #     final_table = dmc.Table(create_table(df_))
                
<<<<<<< HEAD
=======
            #     whole_div = html.Div(children=[
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:user-outline", width=30), color='gray', radius='xl', size='30px', style={'border': '2px solid #868E96', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div(dmc.Text(human_prompt, style={'text-align':'left'})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div'),
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:face-agent", width=30), color='blue', radius='xl', size='30px', style={'border': '2px solid #53A5EC', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div([final_table]), className='grid-chat-for-table')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div')
            #     ])
                
            #     conv_hist.append(whole_div)
                
            #     return conv_hist
            
            # elif contains_word(human_prompt.lower(), plot_list):
            #     chart = cg.Chart(df, api_key=openai_api_key)
            #     fig = chart.plot(human_prompt, return_fig=True)
            #     fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            #     graph_bot = dcc.Graph(figure=fig)

>>>>>>> c3539ed3b5360adf57107c6e3f28e703c01114ee
            #     whole_div = html.Div(children=[
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:user-outline", width=30), color='gray', radius='xl', size='30px', style={'border': '2px solid #868E96', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div(dmc.Text(human_prompt, style={'text-align':'left'})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div'),
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:face-agent", width=30), color='blue', radius='xl', size='30px', style={'border': '2px solid #53A5EC', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div([final_table]), className='grid-chat-for-table')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div')
            #     ])
                
            #     conv_hist.append(whole_div)
                
            #     return conv_hist
            
<<<<<<< HEAD
            # # elif contains_word(human_prompt.lower(), plot_list):
            # #     chart = cg.Chart(df, api_key=openai_api_key)
            # #     fig = chart.plot(human_prompt, return_fig=True)
            # #     fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            # #     graph_bot = dcc.Graph(figure=fig)

            # #     whole_div = html.Div(children=[
            # #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:user-outline", width=30), color='gray', radius='xl', size='30px', style={'border': '2px solid #868E96', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            # #                                         dmc.Col(html.Div(dmc.Text(human_prompt, style={'text-align':'left'})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div'),
            # #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:face-agent", width=30), color='blue', radius='xl', size='30px', style={'border': '2px solid #53A5EC', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            # #                                         dmc.Col(html.Div(graph_bot), className='grid-chat-for-table')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div')
            # #         ])
                
            # #     conv_hist.append(whole_div)
                
            # #     return conv_hist
            
            # else:
            #     prompt = generate_prompt(df, human_prompt)  # Generate prompt using the function
            #     agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            #     chatbot_resp = agent.run(prompt)  # Use the generated prompt
                
=======
            # else:
            #     prompt = generate_prompt(df, human_prompt)  # Generate prompt using the function
            #     agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            #     chatbot_resp = agent.run(prompt)  # Use the generated prompt
                
>>>>>>> c3539ed3b5360adf57107c6e3f28e703c01114ee
            #     whole_div = html.Div(children=[
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:user-outline", width=30), color='gray', radius='xl', size='30px', style={'border': '2px solid #868E96', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div(dmc.Text(human_prompt, style={'text-align':'left', 'font-weight':700})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div'),
            #         dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:face-agent", width=30), color='blue', radius='xl', size='30px', style={'border': '2px solid #53A5EC', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
            #                                         dmc.Col(html.Div(dmc.Text(chatbot_resp, style={'text-align':'left'})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div')
            #     ])

            #     conv_hist.append(whole_div)

<<<<<<< HEAD
            #     return conv_hist
            prompt = generate_prompt(df, human_prompt)  # Generate prompt using the function
            agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            chatbot_resp = agent.run(prompt)  # Use the generated prompt
=======
            prompt = generate_prompt(df, human_prompt)  # Generate prompt using the function
            agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)
            print(agent)
            chatbot_resp = agent.run(prompt)  # Use the generated prompt
            print(chatbot_resp)
>>>>>>> c3539ed3b5360adf57107c6e3f28e703c01114ee
            
            whole_div = html.Div(children=[
                dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:user-outline", width=30), color='gray', radius='xl', size='30px', style={'border': '2px solid #868E96', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
                                                dmc.Col(html.Div(dmc.Text(human_prompt, style={'text-align':'left', 'font-weight':700})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div'),
                dmc.Grid(gutter='xs', children=[dmc.Col(html.Div(dmc.Avatar(DashIconify(icon="mdi:face-agent", width=30), color='blue', radius='xl', size='30px', style={'border': '2px solid #53A5EC', 'border-radius':'50%'})), span='content', className=cns.ZARA_PROFILE_GRID),
                                                dmc.Col(html.Div(dmc.Text(chatbot_resp, style={'text-align':'left'})), className='grid-chat')], style={'padding':'5px 0px 5px 0px'}, className='chat-full-div')
            ])

            conv_hist.append(whole_div)

            return conv_hist
    
        else:
            return None

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
