import pandas as pd
import sqlite3
# ct_user_level_df = pd.read_csv("./data/CT_USER_LEVEL.csv")

# # Create a connection to a local database (This will create a file called mydatabase.db)
# connection = sqlite3.connect('mydb.db')

# # Copy the dataframe to our SQLite database
# ct_user_level_df.to_sql('CT_USER_LEVEL', connection, if_exists='replace')

from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///mydb.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM CT_USER_LEVEL LIMIT 10;")