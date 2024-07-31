# oil-and-gas-dashboard-project

This prototype of oil and gas dashboard mainly uses Python and Dash. I understand this code still has so many bugs and needs an improvement, so it will be updated regularly.

### The step-by-step of compiling this code:
1. Clone the repository
```
git clone https://github.com/yourusername/oil-and-gas-dashboard-project
```

2. Install required Python packages, using python 3.10.11 is preferred.
```
pip install -r requirements.txt
```
3. Create file "openai_api_key.py" in folder src > components > Zara_Assistant
   
4. Put your openai api key on this file by simply using
```
KEY = "write-your-api-key-here"
```

5. Run Python file "main.py" on terminal
```
python main.py
```

### How to prompt?
You can ask everything about the data shown above. It can also show dataframe and graph.
![screenshot_3](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/42ab7268-e30f-4ca0-9621-c5609b7ca443)
1. Choose the data you want (Production Data, Water Cut Daily Gas Ratio, Log Data, Blocks Data, and Wells Data.)
2. Check "enable query" to query dataframe you want, and check "enable plotting" to create plot based on dataframe
3. Uncheck everything for general questions or dataframe related in general.



### this is the screenshots of the dashboard

1. this is webmaps. it has filters: map settings to configure basemaps, block filters to configure settings of blocks showings, well filters to configure settings of well showings.
![image](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/04cf7152-7acb-4b6a-b1be-c72d67ce7bb0)


2. this is overview analysis. it has filters: summary filters to filters blocks, from date, and to date that you need to show 
![image](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/14fcd8d6-6654-439d-ae33-5f08968e086f)


3. this is production performance analysis. it has filters: well production filters to filters wells, from date, and to date that you need to show 
![image](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/748dd8c3-f830-4adf-87fa-8459c754a339)


4. this is gng analysis. it has filters: well-log filters to configure well-log data, 3D graphs filter to show parameter well and lithology
![image](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/c5a05f6f-d891-48c1-ad64-9963bcd22c31)

5. this is Zara Chatbot. you can ask everything about the data shown above. It can also show dataframe and graph.
![screenshot_2](https://github.com/naufalmaa/dashboard-and-web-maps-app-zara/assets/112636018/df394511-2643-4ef1-907b-c63d3d98eba2)







