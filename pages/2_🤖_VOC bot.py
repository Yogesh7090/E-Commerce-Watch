import streamlit as st
import os
import openai
import time

# from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.memory import ConversationBufferMemory
from sqlalchemy import create_engine, MetaData
from llama_index.core import SQLDatabase
from llama_index.core.indices.struct_store.sql_query import NLSQLTableQueryEngine
from llama_index.llms.openai import OpenAI
from logo import add_logo

add_logo()

@st.cache_resource(show_spinner="Connecting to the database...")
def connection_string():
    user = "sqladmin"
    password = "7yZ63d2KdkAY"
    host = "catalytics-dw01.database.windows.net"
    database = "dunnhumby"
    port = 1433
    conn_string = f'mssql+pyodbc://{user}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    # conn_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    # db = SQLDatabase.from_uri(conn_string)
    # print(db)
    engine = create_engine(conn_string)

    # Reflect the database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    return engine


def template_formation():

    PROMPT_SUFFIX = """Use only the following tables in the database to query:
    'Sentiment_Data' and 'Topic_data'. 
    The 'Sentiment_Data' table has the following columns:
    'Review', 'Date', 'Rating', 'Document_ID', 'Scores', 'Sentiment', 'Brand', 'Company'.
    
    The 'Topic_data' table has the following columns:
    'Review', 'Date', 'Rating', 'Document_ID', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Topic_Keywords', 'Topic_Name'.

    Question: {input}"""

    _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct query to run, then 
    look at the results of the query and return the answer in summarized format. 
    Make sure the columns are correctly used in the query for each table used.
    The SQL Query should be compatible in MICROSOFT SQL server.
    Unless the user specifies in his/her question a specific number of examples he wishes to obtain, always fetch at most 50 
    results. If the user asks to list out some values from the table always pick only the top 50 results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    Never query for all the columns from a specific table, only ask for a few relevant columns given the question.
    Pay attention to use only the column names that you can see in the schema description. Be careful to not 
    query for columns that do not exist. Please do not mix up the columns in each table. Carefully use the column names. 
    Also, pay attention to which column is in which table. If there is no result from SQL server, please mention that there are no 
    results for the question asked.
    Please note that the Date column in both tables are in the format 'year-month-day hour:minute:seconds.millisecond'. 
    For example '2020-11-05 00:00:00.000' . When querying related to date please use date format.
    When user asks to give any information for 'today' or 'now', please use today's date. 
    To check reviews please use the 'Sentiment_Data' table as default unless specified by the user.
    If question is a greeting, please respond with a greeting and 'how can I help you. Please ask a question related to VOC.'.
    If there is an error in sql query, please respond the following "Please check the question again. Ask me a question related to VOC!".
    Use the following format:
    Your answer should contain only the summary of the sql result.
    """

    return (
    _DEFAULT_TEMPLATE + PROMPT_SUFFIX
    )
st.markdown(
    """
    <style>
    .custom-title {
        color: #005F7B;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class in the title
st.markdown('<h1 class="custom-title">VOC Bot</h1>', unsafe_allow_html=True)
# st.title('VOC Bot')

engine = connection_string()
sql_database = SQLDatabase(engine, include_tables=['Sentiment_Data', 'Topic_data'])


if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello. Ask me a question related to VOC!",  "avatar": "🤖"}
    ]

for message in st.session_state.messages: # Display the prior chat messages
    print("message:", message)
    with st.chat_message(message["role"], avatar=message['avatar']):
        st.markdown(message["content"])

memory = ConversationBufferMemory()
# openai.api_key = os.getenv('OPENAI_API_KEY')
#API_KEY = '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'
openai.api_key='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'

# API_KEY = os.getenv('OPENAI_API_KEY')


llm = OpenAI(model="gpt-4-turbo", temperature=0, api_key= openai.api_key)
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=['Sentiment_Data', 'Topic_data'],
    llm=llm,
    verbose=True
)

def response_generator():
    prompt_template = template_formation()
    formatted_prompt = prompt_template.format(memory=memory, input=prompt)
    response = query_engine.query(str(formatted_prompt))
    print(f"Generated SQL Query: {response.metadata}")
    for word in response.response.split():
        yield word + " "
        time.sleep(0.05)

try:
    if prompt := st.chat_input("Your question"):
        with st.chat_message("user", avatar='👤'):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt, "avatar": "👤"})
        # st.write(prompt)

        # formatted_prompt = prompt_template.format(memory=memory, input=prompt) 
        # response = query_engine.query(str(formatted_prompt))
        # print("Response:", response)
        with st.chat_message("assistant", avatar='🤖'):
            # st.markdown(response_generator())
            response = st.write_stream(response_generator())
        st.session_state.messages.append({"role": "assistant", "content": response, "avatar": "🤖"})
except Exception as e:
    print(str(e))
    with st.chat_message("assistant",  avatar='🤖'):
        response = "The question was not understood. Please ask me a question related to VOC!"
        response = st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response, "avatar": "🤖"})

       


# Questions:
# Querying with: list out reviews related to customer service
# Querying with: list out what are the positive reviews of customer service
# Querying with: could you tell me all the negative reviews
# Querying with: could you tell me the exact negative review received
# Querying with: could you mention what is the lowest rating for the negative reviews?
# list out what are the positive reviews about customer service; list down specifically the reviews with free shipping offer.
#  what are the negative reviews received on april 4th 2024?
# what are the reviews received in November 2023?
# what are the Topic names for the rating 5?
#how many reviews with rating more than 3?
# are there any reviews for the year 2024?
# what are the various topics based on reviews?
# would you give me reviews based on the topic Product Quality?