from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase


model = ChatOllama(
    model="llama3:8b"
)

question = "Get payment limit of this user id = INLABLB"
# question = "How many rows in this table?"

db = SQLDatabase.from_uri("sqlite:///mydb.db")
agent_executor = create_sql_agent(model, db=db, verbose=True)

answers = agent_executor.invoke(question)

print("Answer: ", answers)