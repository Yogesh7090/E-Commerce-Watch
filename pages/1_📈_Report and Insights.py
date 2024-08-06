import streamlit as st
import pandas as pd
import plotly.express as px
import openai
from sqlalchemy import create_engine
# from openai import OpenAI
from langchain.llms import OpenAI

import os
import streamlit.components.v1 as components
from logo import add_logo

 
# API_KEY = os.getenv('OPENAI_API_KEY')
# Set your OpenAI API keystre
openai.api_key="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"
 
# Streamlit configuration
st.set_page_config(layout="wide")

add_logo()

# Function to fetch data from MSSQL
# @st.cache
def load_data():
    server = 'catalytics-dw01.database.windows.net'  # replace with your server name
    database = 'dunnhumby'  # replace with your database name
    username = 'sqladmin'  # replace with your username
    password = '7yZ63d2KdkAY'  # replace with your password
    driver = 'ODBC Driver 17 for SQL Server'  # replace with your driver
 
    # Create a connection string
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
 
    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
 
    # Query the data from two tables
    query1 = 'SELECT * FROM Sentiment_Data'  # replace with your first table name
    query2 = 'SELECT * FROM Topic_data'  # replace with your second table name
 
    data1 = pd.read_sql(query1, engine)
    data2 = pd.read_sql(query2, engine)
 
    return data1, data2
 
# Load data
data1, data2 = load_data()
 
def get_ai_insights(data1, data2):
    data_sample1 = data1.head(200).to_dict()
    data_sample2 = data2.head(200).to_dict()
   
    client = OpenAI(api_key=openai.api_key)
 
    model = "gpt-4o"
    messages = [
        {
            "role": "user",
            "content": f"""
            I require a thorough analysis of the following dataset, which includes sentiment and topic data from our e-commerce platform. The analysis should encompass the following:
            1. An in-depth summary that highlights key insights, trends, and patterns within the data.
            2. Examination of correlations between sentiment scores and various topics.
            3. Detailed breakdown of sentiment distribution across different topics.
            4. Identification and explanation of any anomalies or outliers in the data.
            5. Strategic recommendations for actions or areas requiring further investigation based on the analysis.
 
            Here is a sample of the sentiment data:
            {data_sample1}
 
            Here is a sample of the topic data:
            {data_sample2}
            """
        }
    ]
 
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    response_message = response.choices[0].message.content
 
    return response_message
 
 
st.markdown(
    """
    <style>
        .embed-container {
            position: relative;
            width: 100%;
            padding-bottom: 59.25%; /* 16:9 aspect ratio */
            height: 0;
            overflow: hidden;
            margin-top: -50px; /* Lift the iframe 20px towards the top */
        }
        .embed-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }
        @media (max-width: 767px) {
            .embed-container {
                padding-bottom: 75%; /* Adjust aspect ratio for smaller screens */
            }
        }
    </style>
    <div class="embed-container">
        <iframe
            src="https://app.powerbi.com/reportEmbed?reportId=22722546-449c-4f72-b0cf-adeec85ea8f9&autoAuth=true&ctid=4ecd958c-a12f-45ac-95d6-ab307820bddb"
            allowFullScreen="true"
            scrolling="no">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)
 
st.markdown('<div style="margin-top: 5px;"></div>', unsafe_allow_html=True)
 
 
# Function to dynamically fetch data based on interaction
def fetch_data_based_on_interaction():
    # This function should be implemented to fetch data based on Power BI interactions.
    # For the sake of this example, let's simulate it by returning the whole dataset.
    return data1, data2
 
# Fetch data and generate insights based on user interaction
if st.button("Generate Insights"):
    dynamic_data1, dynamic_data2 = fetch_data_based_on_interaction()
    summary = get_ai_insights(dynamic_data1, dynamic_data2)
   
    st.subheader("Automated Insights:")
    st.write(summary)
 
    # Display graphs dynamically based on the fetched data
    if not dynamic_data1.empty and not dynamic_data2.empty:
        st.subheader("Graphs from Sentiment Data:")
        for column in dynamic_data1.columns:
            if column == 'Sentiment':
                fig = px.histogram(dynamic_data1, x=column, title=f'Distribution of {column}')
                st.plotly_chart(fig)
            
 

 
        st.subheader("Graphs from Topic Data:")
        for column in dynamic_data2.columns:
            if column not in ['Review', 'Date', 'Document_ID', 'Dominant_Topic', 'Topic_Perc_Contrib',
                              'Topic_Keywords']:
                fig = px.histogram(dynamic_data2, x=column, title=f'Distribution of {column}')
                st.plotly_chart(fig)
        
