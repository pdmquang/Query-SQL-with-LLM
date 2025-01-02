from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent
# from langchain_community.utilities import SQLDatabase
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine

model = ChatOllama(
    model="llama3:8b"
)

question = "Get payment limit of this user id = INLABLB in table CT_USER_LEVEL"
# question = "How many rows in this table?"

conn = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=SVT_UAT;Trusted_Connection=yes;'
db_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn}")

# Create a SQLDatabase instance
db = SQLDatabase(db_engine)
agent_executor = create_sql_agent(model, db=db, verbose=True, 
                                  agent_executor_kwargs={"handle_parsing_errors": True},)

try:
    # Invoke the agent executor with the question
    print(f"********ANSWER**********: \n{agent_executor.invoke(question)}")
    # print(langchain.globals.get_verbose())
except ValueError as e:
    # Handle parsing errors specifically
    print(f"An error occurred**********: {e}")