from langchain_ollama import ChatOllama
from langchain_community.agent_toolkits import create_sql_agent
# from langchain_community.utilities import SQLDatabase
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
import pyodbc

model = ChatOllama(
    model="llama3:8b"
)

question = "Get payment limit of this user id = INLABLB"
# question = "How many rows in this table?"

# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=localhost;"
#                       "Database=SVT_UAT;"
#                       "Trusted_Connection=yes;")

# db = SQLDatabase.from_uri("sqlite:///mydb.db")
# connectionString = "mssql+pyodbc://localhost:1433/SVT_UAT?driver=ODBC Driver 17 for SQL Server;Trusted_Connection=yes;"
connectionString = "mssql+pyodbc:///?odbc_connect='DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-OGDKKJ9;DATABASE=SVT_UAT;Trusted_Connection=yes;"
# connection_string = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=localhost;"
#     "Database=your_database_name;"
#     "Trusted_Connection=yes;"
# )

conn = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=SVT_UAT;Trusted_Connection=yes;'
cnxn = pyodbc.connect(conn)

# connectionString = "mssql+pymssql://localhost/SVT_UAT;Trusted_Connection=yes;"
db_engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn}")

# with db_engine.connect() as connection:
    # result = connection.execute("SELECT * FROM CT_USER_LEVEL")
    # print(result)
# db = SQLDatabase(db_engine)
# print(db.get_table_names())

# Step 2: Create an SQLAlchemy engine from the pyodbc connection
# engine = create_engine("mssql+pyodbc://localhost:1433/SVT_UAT?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes;")
# engine = create_engine('mssql+pyodbc:///?odbc_connect=' + cnxn.connection_string)

# Step 3: Initialize LangChain's SQLDatabase with the engine
# db = SQLDatabase.from_uri(engine.url)

# Create a SQLDatabase instance
db = SQLDatabase(db_engine)
agent_executor = create_sql_agent(model, db=db, verbose=False, handle_parsing_errors=True)

# print(agent_executor.invoke(question))

answers = agent_executor.invoke(question)

print("Answer: ", answers)