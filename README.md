# LLM SQL
## Process time
* dk

## Results
```
Let's get started!

Thought: Since we're looking for a payment limit, I think we might need to check if there are any tables related to payments or user information.

Action: sql_db_list_tables
Action Input: (empty string)CT_USER_LEVELI'll start by listing the tables in the database using `sql_db_list_tables`. This will give me an idea of what tables are available for querying.

Question: Get payment limit of this user id = INLABLB
Thought: I should look at the tables in the database to see what I can query.  Then I should query the schema of the most relevant tables.
Action: sql_db_list_tables
Action Input: (empty string)CT_USER_LEVELBased on the observation that the table "CT_USER_LEVEL" exists, my next action is to check the schema of this table to see what columns are available for querying.

Action: sql_db_schema
Action Input: CT_USER_LEVEL
CREATE TABLE "CT_USER_LEVEL" (
        "index" INTEGER, 
        "ID_USER" TEXT, 
        "QT_ADJUSTMENT" INTEGER, 
        "QT_PAYMENT" INTEGER, 
        "QT_REFUND" INTEGER, 
        "QT_IMPOSITION" INTEGER, 
        "QT_ABATEMENT" INTEGER
)

/*
3 rows from CT_USER_LEVEL table:
index   ID_USER QT_ADJUSTMENT   QT_PAYMENT      QT_REFUND       QT_IMPOSITION   QT_ABATEMENT
0       INLCCLA 0       0       4       0       0
1       INLTWWA 4       0       9       0       0
2       INLCCTA 0       0       0       0       0
*/I think I know what to do!

Question: Get payment limit of this user id = INLABLB
Thought: Since we have the schema of the CT_USER_LEVEL table, let's query it to get the payment limit for the given user ID.

Action: sql_db_query
Action Input: SELECT QT_PAYMENT FROM CT_USER_LEVEL WHERE ID_USER = 'INLABLB'[(5,)]Let's finish answering the question!

Thought: I now know the final answer.
Final Answer: 5

The query `SELECT QT_PAYMENT FROM CT_USER_LEVEL WHERE ID_USER = 'INLABLB'` returns a single row with a value of 5 for the `QT_PAYMENT` column, which is the payment limit for the given user ID.

> Finished chain.
```

# Embedding vector (NOT GOOD)
## Process time

* Load model: 0.634
* Get Embedding for 5 rows in 2.19

* Load model 0.635
* Get Embedding for 87 rows in 36.69

## Results
### Use all columns
```
'{"ID_LEVEL":10103,"ID_USER":"INLLWSH","QT_ADJUSTMENT":3,"QT_PAYMENT":0,"QT_REFUND":3,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.25573468693565715
'{"ID_LEVEL":44,"ID_USER":"INLTHGA","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":0,"QT_IMPOSITION":3,"QT_ABATEMENT":4}' =
0.2556428229656703
'{"ID_LEVEL":78,"ID_USER":"INLNZAB","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":0,"QT_IMPOSITION":2,"QT_ABATEMENT":2}' =
0.2550232395532044
'{"ID_LEVEL":66,"ID_USER":"INLPSCD","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":1,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.25492110821694025
'{"ID_LEVEL":82,"ID_USER":"INLNPKA","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":0,"QT_IMPOSITION":3,"QT_ABATEMENT":3}' =
0.25442826075814673
'{"ID_LEVEL":8,"ID_USER":"INLCSPA","QT_ADJUSTMENT":0,"QT_PAYMENT":2,"QT_REFUND":2,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.2544043602207443
'{"ID_LEVEL":1,"ID_USER":"INLABLB","QT_ADJUSTMENT":0,"QT_PAYMENT":5,"QT_REFUND":4,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.2538718975126377
```

### Use relevant columns only
```
'{"ID_USER":"INLAK0A","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":0,"QT_IMPOSITION":2,"QT_ABATEMENT":1}' =
0.25458052241944773
'{"ID_USER":"INLNPKA","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":0,"QT_IMPOSITION":3,"QT_ABATEMENT":3}' =
0.24971750096863377
'{"ID_USER":"INLTWWA","QT_ADJUSTMENT":4,"QT_PAYMENT":0,"QT_REFUND":9,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.24953182139640218
'{"ID_USER":"INLTWWA","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":9,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.2486932934540611
'{"ID_USER":"INLLWWB","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":3,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.24756757371135962
'{"ID_USER":"INLTWCA","QT_ADJUSTMENT":0,"QT_PAYMENT":0,"QT_REFUND":5,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.24722427462334107
'{"ID_USER":"INLCSPA","QT_ADJUSTMENT":0,"QT_PAYMENT":2,"QT_REFUND":2,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.24701861620448362
'{"ID_USER":"INLABLB","QT_ADJUSTMENT":0,"QT_PAYMENT":5,"QT_REFUND":4,"QT_IMPOSITION":0,"QT_ABATEMENT":0}' =
0.24699483676088185
```