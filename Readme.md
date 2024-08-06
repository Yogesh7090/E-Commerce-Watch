Project Documentation of VOC Dashboard

1. Objective
To create a Streamlit application that fetches sentiment and topic data from an MSSQL database, generates insights using OpenAI's GPT-4 model, and displays interactive visualizations and PowerBI reports.


2. Workflow
    a)  Setup Streamlit Environment: Configure the Streamlit application with a wide layout and add a company logo.

    b) Fetch Data from MSSQL: Connect to the MSSQL database, execute SQL queries to retrieve data from the Sentiment_Data and Topic_data tables, and store the data in Pandas DataFrames.

    c) Generate AI Insights: Use the OpenAI API to analyze the fetched data and generate detailed insights.

    d) Display PowerBI Reports: Embed a PowerBI report in the Streamlit application.

    e) Dynamic Data Interaction: Allow users to interact with the data and generate dynamic insights and visualizations based on user interactions.


3. Requirements

Software and Libraries:

    Streamlit
    Pandas
    Plotly
    SQLAlchemy
    OpenAI API
    Streamlit Components
    PowerBI


Database: MSSQL Server with tables Sentiment_Data and Topic_data

APIs and Keys: OpenAI API Key

Configuration: Database connection parameters (server, database, username, password, driver)


4. Solution:
    1_📈_Report and Insights.py






Project Documentation of VOC Bot


1. Objective
    To develop a Streamlit application named VOC Bot that allows users to interact with sentiment and topic data from an MSSQL database, generating insights and summaries using OpenAI's GPT-4 model, and presenting results through interactive chat and visualizations.


2. Workflow
    a) Setup Streamlit Environment: Configure the Streamlit application layout, add a custom title, and display the company logo.

    b)Database Connection: Establish a connection to the MSSQL database and reflect the schema using SQLAlchemy.

    c) Generate AI Insights: Formulate a prompt for GPT-4, generate SQL queries, and retrieve summarized insights based on user questions.

    d) User Interaction and Chat: Implement a chat interface that takes user inputs, processes them to generate responses, and displays both user and assistant messages.

    e) Display Results and Error Handling: Generate dynamic responses and handle errors gracefully.


3. Requirements
    Software and Libraries:

    Streamlit
    Pandas
    SQLAlchemy
    OpenAI
    LlamaIndex
    Streamlit Components
    PyODBC


    Database: MSSQL Server with tables Sentiment_Data and Topic_data

    APIs and Keys: OpenAI API Key

    Configuration: Database connection parameters (server, database, username, password, driver)


4. Solution:

    2_🤖_VOC bot.py




