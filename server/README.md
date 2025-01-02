# Generate Mocked data
https://www.mockaroo.com/

# Different Agent Type
```
agent_type: Optional[
        Union[AgentType, Literal["openai-tools", "tool-calling"]]
    ] = None,
    
class AgentType(str, Enum):
    """An enum for agent types.

    See documentation: https://python.langchain.com/docs/modules/agents/agent_types/
    """

    ZERO_SHOT_REACT_DESCRIPTION = "zero-shot-react-description"
    """A zero shot agent that does a reasoning step before acting."""

    REACT_DOCSTORE = "react-docstore"
    """A zero shot agent that does a reasoning step before acting.
    
    This agent has access to a document store that allows it to look up 
    relevant information to answering the question.
    """

    SELF_ASK_WITH_SEARCH = "self-ask-with-search"
    """An agent that breaks down a complex question into a series of simpler questions.
    
    This agent uses a search tool to look up answers to the simpler questions
    in order to answer the original complex question.
    """
    CONVERSATIONAL_REACT_DESCRIPTION = "conversational-react-description"
    CHAT_ZERO_SHOT_REACT_DESCRIPTION = "chat-zero-shot-react-description"
    """A zero shot agent that does a reasoning step before acting.
    
    This agent is designed to be used in conjunction 
    """

    CHAT_CONVERSATIONAL_REACT_DESCRIPTION = "chat-conversational-react-description"

    STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION = (
        "structured-chat-zero-shot-react-description"
    )
    """An zero-shot react agent optimized for chat models.
    
    This agent is capable of invoking tools that have multiple inputs.
    """

    OPENAI_FUNCTIONS = "openai-functions"
    """An agent optimized for using open AI functions."""

    OPENAI_MULTI_FUNCTIONS = "openai-multi-functions"
```

# LLM SQL
## Process time
* dk

## Results

### Exception
```
Exception has occurred: ValueError
An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Could not parse LLM output: `I'm ready to interact with your SQL database. What's the question you'd like me to answer? Please provide a valid SQL query, and I'll do my best to help you out!`
langchain_core.exceptions.OutputParserException: Could not parse LLM output: `I'm ready to interact with your SQL database. What's the question you'd like me to answer? Please provide a valid SQL query, and I'll do my best to help you out!`

During handling of the above exception, another exception occurred:

  File "D:\My Files\NTU\SVT_RAG\query_by_SQL.py", line 53, in <module>
    answers = agent_executor.invoke(question)
ValueError: An output parsing error occurred. In order to pass this error back to the agent and have it try again, pass `handle_parsing_errors=True` to the AgentExecutor. This is the error: Could not parse LLM output: `I'm ready to interact with your SQL database. What's the question you'd like me to answer? Please provide a valid SQL query, and I'll do my best to help you out!`
```

### Get payment limit of this user id = INLABLB in table CT_USER_LEVEL
```
Let's start by listing all the tables in the database using `sql_db_list_tables`.

Action: sql_db_list_tables
Action Input: ""ABC, A_EMS_ACTIVITY, A_EMS_CASE, A_EMS_TRANSACTION, CT_ABATEMENT_LIMIT, CT_ADJUSTMENT_LIMIT, CT_AUDIT_FIELD_REVIEW, CT_BANK, CT_BANK_BRANCH, CT_CASINO_ENTITY, CT_CM_TAX_TYPE, CT_CONTROL_FILTER, CT_CORPORATED_TAX, CT_COUNTRY, CT_CURRENCY, CT_DEBITTRIGGER, CT_DOCUMENT_TYPE, CT_EMS_CASE_ASSIGNMENT, CT_EMS_ENTITY_ID_TYPE, CT_EMS_ENUM, CT_EMS_NOTICE, CT_EMS_SCHEDULED_JOB, CT_EMS_STATE, CT_ENTITY_ID_TYPE, CT_ENUM, CT_ENUM_FIN, CT_ENUM_backup, CT_FC_SCHEDULE_CONFIG, CT_FILING_STATUS, CT_FOLDER_TYPE, CT_GRACE_PERIOD, CT_GST, CT_IMPOSITION_LIMIT, CT_INTEREST_RATE, CT_IRIN_INTERFACE, CT_LODGEMENT_DOCUMENT, CT_METER_READING_DATE, CT_NON_SVT_TAX_TYPE, CT_NOTICE, CT_NOTICE_ENTITY, CT_OFFSETTING, CT_PAYMENT_INPUT_SOURCE, CT_PAYMENT_LIMIT, CT_PAYMENT_MODE, CT_PAYMENT_REFUND_TRANS, CT_PENALTY_IMPOSITION, CT_PLBS_PENALTY_TYPE, CT_PLBS_PERMIT, CT_PLBS_RELATIONSHIP_TYPE, CT_PUBLIC_HOLIDAYS, CT_REASON, CT_REFUND_LIMIT, CT_REFUND_REVIEW, CT_RELATIONSHIP_TYPE, CT_REPORT, CT_ROLE_FUNCTION, CT_SOA_MESSAGE, CT_SORTGROUP, CT_SOURCE, CT_SPOST, CT_SPOST_BRANCH, CT_SUPPRESSION, CT_TAX_TYPE, CT_TRANS_CODE, CT_TUT_ASSESSMENT_THRESHOLD, CT_TUT_ASSESSMENT_YEAR, CT_TUT_RETURN_STATUS, CT_USER_LEVEL, CT_WORK_TYPE, H_ACC_ADJUSTMENT, H_ACC_TRANSFER_ADJUSTMENT, H_CM_SUPPRESSION, H_CM_WORK_ITEM, H_ENF_ABATEMENT, H_ENF_FILING_CASE, H_ENF_PENALTY_IMPOSITION, H_ENF_WRITEOFF, H_PAY_PAYMENT_RECEIPT_ONLINE, H_PLBS_AUDIT_VISIT, H_PLBS_ENTITY, H_PLBS_ENTITY_ID, H_PLBS_FRUIT_MACHINE, H_PLBS_LODGEMENT, H_PLBS_LODGEMENT_DOCUMENT, H_PLBS_PERMIT, H_PLBS_PL_ASSESSMENT, H_PLBS_PL_COLLECTION, H_PLBS_RELATIONSHIP, H_REF_REFUND_REQUEST, H_ROLE, H_TUT_ALLOCATION_BENEFICIARY, H_TUT_ENTITY, H_TUT_ENTITY_ADDRESS, H_TUT_ENTITY_ID, H_TUT_ENTITY_NAME, H_TUT_ENTITY_RELATIONSHIP, H_TUT_RETURN, H_USER, TEMP_EMS_ACTIVITY_ISDS, TEMP_EMS_CASE_ISDS, TEMP_EMS_EA_APPOINTMENT_ISDS, TEMP_EMS_ENTITY_ADDRESS_ISDS, TEMP_EMS_ENTITY_CONTACT_ISDS, TEMP_EMS_ENTITY_RELATIONSHIP_ISDS, TEMP_EMS_NOTE_ISDS, TEMP_T_CM_DOCUMENT_ISDS, TESTING, TEST_BENEFICIAL, T_ACC_ADJUSTMENT, T_ACC_ASSESSMENT, T_ACC_FINANCIAL_TRANSACTION, T_ACC_TAX_PERIOD, T_ACC_TAX_TYPE_HEADER, T_CHECK_PV, T_CM_DOCUMENT, T_CM_DOCUMENT_NOTE, T_CM_SUPPRESSION, T_CM_WORK_ITEM, T_EMS_ACTIVITY, T_EMS_CASE, T_EMS_CASE_ISDS, T_EMS_EA_APPOINTMENT, T_EMS_ENTITY, T_EMS_ENTITY_ADDRESS, T_EMS_ENTITY_CONTACT, T_EMS_ENTITY_RELATIONSHIP, T_EMS_ENTITY_backup, T_EMS_IP, T_EMS_IP_PAYMENT, T_EMS_NOTE, T_EMS_PROSECUTION, T_EMS_TRANSACTION, T_ENF_ABATEMENT, T_ENF_FILING_CASE, T_ENF_PENALTY_IMPOSITION, T_ENF_WRITEOFF, T_PAY_HASH_KEY, T_PAY_PAYMENT, T_PAY_PAYMENT_RECEIPT, T_PAY_PAYMENT_RECEIPT_ONLINE, T_PAY_PAYMENT_REF, T_PAY_PAYMENT_REF_DETAIL, T_PLBS_AUDIT_VISIT, T_PLBS_AUDIT_VISIT_ATTACHMENT, T_PLBS_BS_ASSESSMENT, T_PLBS_ENTITY, T_PLBS_ENTITY_ID, T_PLBS_FRUIT_MACHINE, T_PLBS_LODGEMENT, T_PLBS_LODGEMENT_DOCUMENT, T_PLBS_LODGEMENT_LOG, T_PLBS_PERMIT, T_PLBS_PERMIT_backup, T_PLBS_PL_ASSESSMENT, T_PLBS_PL_COLLECTION, T_PLBS_RELATIONSHIP, T_POSTING_EXCEPTION, T_REF_REFUND_REQUEST, T_REF_REFUND_REQUEST_DETAIL, T_REPORT, T_REPORT_INTERFACE, T_REPORT_INTERFACE_LOG, T_ROLE, T_TUT_ALLOCATION_BENEFICIARY, T_TUT_ALLOCATION_INTERFACE, T_TUT_ALLOCATION_OTHER, T_TUT_ALLOCATION_TOTAL, T_TUT_ASSESSMENT, T_TUT_ENTITY, T_TUT_ENTITY_ADDRESS, T_TUT_ENTITY_ID, T_TUT_ENTITY_NAME, T_TUT_ENTITY_RELATIONSHIP, T_TUT_LETTER, T_TUT_NSL_PARAGRAPH, T_TUT_RETURN, T_USER, T_USER_ACCESS, XXBW_KF_INV_TAX, XXBW_KF_NONPO_SUPP_DET, XXBW_KF_ORG_NAME_REQUEST, XXBW_KF_PO_SUPP_DET, XXBW_KF_REQUESTER, dtproperties, t_role_bakI now know the list of tables in the database.

Action: sql_db_schema
Action Input: CT_USER_LEVEL
CREATE TABLE [CT_USER_LEVEL] (
        [ID_LEVEL] BIGINT NOT NULL IDENTITY(1,1), 
        [ID_USER] NVARCHAR(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [QT_ADJUSTMENT] INTEGER NULL, 
        [QT_PAYMENT] INTEGER NULL, 
        [QT_REFUND] INTEGER NULL, 
        [QT_IMPOSITION] INTEGER NULL, 
        [QT_ABATEMENT] INTEGER NULL
)

/*
3 rows from CT_USER_LEVEL table:
ID_LEVEL        ID_USER QT_ADJUSTMENT   QT_PAYMENT      QT_REFUND       QT_IMPOSITION   QT_ABATEMENT
1       INLABLB 0       5       4       0       0
2       INLCAHA 0       0       0       0       0
3       INLCCLA 0       0       4       0       0
*/A new question! Let's think about what to do...

I see that the input question is "Get payment limit of this user id = INLABLB in table CT_USER_LEVEL". I should look at the tables in the database to see what I can query. Then I should query the schema of the most relevant tables.

From the list of tables, I noticed that there are many tables related to users and their levels, so it's likely that I need to query the CT_USER_LEVEL table.

Action: sql_db_schema
Action Input: CT_USER_LEVEL

CREATE TABLE [CT_USER_LEVEL] (
        [ID_LEVEL] BIGINT NOT NULL IDENTITY(1,1), 
        [ID_USER] NVARCHAR(30) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [QT_ADJUSTMENT] INTEGER NULL, 
        [QT_PAYMENT] INTEGER NULL, 
        [QT_REFUND] INTEGER NULL, 
        [QT_IMPOSITION] INTEGER NULL, 
        [QT_ABATEMENT] INTEGER NULL
)

/*
3 rows from CT_USER_LEVEL table:
ID_LEVEL        ID_USER QT_ADJUSTMENT   QT_PAYMENT      QT_REFUND       QT_IMPOSITION   QT_ABATEMENT
1       INLABLB 0       5       4       0       0
2       INLCAHA 0       0       0       0       0
3       INLCCLA 0       0       4       0       0
*/I see where this is going!

Since the input question is "Get payment limit of this user id = INLABLB in table CT_USER_LEVEL", I should query the CT_USER_LEVEL table to get the payment limit for the given user ID.

Action: SQL query
Action Input: 
SELECT QT_PAYMENT FROM CT_USER_LEVEL WHERE ID_USER = 'INLABLB'
SQL query is not a valid tool, try one of [sql_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker].It seems like I'm in the middle of something!

Let's get back on track. You want me to continue with the SQL query.

Action: sql_db_query
Action Input: 
SELECT QT_PAYMENT FROM CT_USER_LEVEL WHERE ID_USER = 'INLABLB'
[(5,)]
```

### Get payment limit of this user id = INLABLB
```
Let's get started.

Action: sql_db_list_tables
Action Input: (empty string)ABC, A_EMS_ACTIVITY, A_EMS_CASE, A_EMS_TRANSACTION, CT_ABATEMENT_LIMIT, CT_ADJUSTMENT_LIMIT, CT_AUDIT_FIELD_REVIEW, CT_BANK, CT_BANK_BRANCH, CT_CASINO_ENTITY, CT_CM_TAX_TYPE, CT_CONTROL_FILTER, CT_CORPORATED_TAX, CT_COUNTRY, CT_CURRENCY, CT_DEBITTRIGGER, CT_DOCUMENT_TYPE, CT_EMS_CASE_ASSIGNMENT, CT_EMS_ENTITY_ID_TYPE, CT_EMS_ENUM, CT_EMS_NOTICE, CT_EMS_SCHEDULED_JOB, CT_EMS_STATE, CT_ENTITY_ID_TYPE, CT_ENUM, CT_ENUM_FIN, CT_ENUM_backup, CT_FC_SCHEDULE_CONFIG, CT_FILING_STATUS, CT_FOLDER_TYPE, CT_GRACE_PERIOD, CT_GST, CT_IMPOSITION_LIMIT, CT_INTEREST_RATE, CT_IRIN_INTERFACE, CT_LODGEMENT_DOCUMENT, CT_METER_READING_DATE, CT_NON_SVT_TAX_TYPE, CT_NOTICE, CT_NOTICE_ENTITY, CT_OFFSETTING, CT_PAYMENT_INPUT_SOURCE, CT_PAYMENT_LIMIT, CT_PAYMENT_MODE, CT_PAYMENT_REFUND_TRANS, CT_PENALTY_IMPOSITION, CT_PLBS_PENALTY_TYPE, CT_PLBS_PERMIT, CT_PLBS_RELATIONSHIP_TYPE, CT_PUBLIC_HOLIDAYS, CT_REASON, CT_REFUND_LIMIT, CT_REFUND_REVIEW, CT_RELATIONSHIP_TYPE, CT_REPORT, CT_ROLE_FUNCTION, CT_SOA_MESSAGE, CT_SORTGROUP, CT_SOURCE, CT_SPOST, CT_SPOST_BRANCH, CT_SUPPRESSION, CT_TAX_TYPE, CT_TRANS_CODE, CT_TUT_ASSESSMENT_THRESHOLD, CT_TUT_ASSESSMENT_YEAR, CT_TUT_RETURN_STATUS, CT_USER_LEVEL, CT_WORK_TYPE, H_ACC_ADJUSTMENT, H_ACC_TRANSFER_ADJUSTMENT, H_CM_SUPPRESSION, H_CM_WORK_ITEM, H_ENF_ABATEMENT, H_ENF_FILING_CASE, H_ENF_PENALTY_IMPOSITION, H_ENF_WRITEOFF, H_PAY_PAYMENT_RECEIPT_ONLINE, H_PLBS_AUDIT_VISIT, H_PLBS_ENTITY, H_PLBS_ENTITY_ID, H_PLBS_FRUIT_MACHINE, H_PLBS_LODGEMENT, H_PLBS_LODGEMENT_DOCUMENT, H_PLBS_PERMIT, H_PLBS_PL_ASSESSMENT, H_PLBS_PL_COLLECTION, H_PLBS_RELATIONSHIP, H_REF_REFUND_REQUEST, H_ROLE, H_TUT_ALLOCATION_BENEFICIARY, H_TUT_ENTITY, H_TUT_ENTITY_ADDRESS, H_TUT_ENTITY_ID, H_TUT_ENTITY_NAME, H_TUT_ENTITY_RELATIONSHIP, H_TUT_RETURN, H_USER, TEMP_EMS_ACTIVITY_ISDS, TEMP_EMS_CASE_ISDS, TEMP_EMS_EA_APPOINTMENT_ISDS, TEMP_EMS_ENTITY_ADDRESS_ISDS, TEMP_EMS_ENTITY_CONTACT_ISDS, TEMP_EMS_ENTITY_RELATIONSHIP_ISDS, TEMP_EMS_NOTE_ISDS, TEMP_T_CM_DOCUMENT_ISDS, TESTING, TEST_BENEFICIAL, T_ACC_ADJUSTMENT, T_ACC_ASSESSMENT, T_ACC_FINANCIAL_TRANSACTION, T_ACC_TAX_PERIOD, T_ACC_TAX_TYPE_HEADER, T_CHECK_PV, T_CM_DOCUMENT, T_CM_DOCUMENT_NOTE, T_CM_SUPPRESSION, T_CM_WORK_ITEM, T_EMS_ACTIVITY, T_EMS_CASE, T_EMS_CASE_ISDS, T_EMS_EA_APPOINTMENT, T_EMS_ENTITY, T_EMS_ENTITY_ADDRESS, T_EMS_ENTITY_CONTACT, T_EMS_ENTITY_RELATIONSHIP, T_EMS_ENTITY_backup, T_EMS_IP, T_EMS_IP_PAYMENT, T_EMS_NOTE, T_EMS_PROSECUTION, T_EMS_TRANSACTION, T_ENF_ABATEMENT, T_ENF_FILING_CASE, T_ENF_PENALTY_IMPOSITION, T_ENF_WRITEOFF, T_PAY_HASH_KEY, T_PAY_PAYMENT, T_PAY_PAYMENT_RECEIPT, T_PAY_PAYMENT_RECEIPT_ONLINE, T_PAY_PAYMENT_REF, T_PAY_PAYMENT_REF_DETAIL, T_PLBS_AUDIT_VISIT, T_PLBS_AUDIT_VISIT_ATTACHMENT, T_PLBS_BS_ASSESSMENT, T_PLBS_ENTITY, T_PLBS_ENTITY_ID, T_PLBS_FRUIT_MACHINE, T_PLBS_LODGEMENT, T_PLBS_LODGEMENT_DOCUMENT, T_PLBS_LODGEMENT_LOG, T_PLBS_PERMIT, T_PLBS_PERMIT_backup, T_PLBS_PL_ASSESSMENT, T_PLBS_PL_COLLECTION, T_PLBS_RELATIONSHIP, T_POSTING_EXCEPTION, T_REF_REFUND_REQUEST, T_REF_REFUND_REQUEST_DETAIL, T_REPORT, T_REPORT_INTERFACE, T_REPORT_INTERFACE_LOG, T_ROLE, T_TUT_ALLOCATION_BENEFICIARY, T_TUT_ALLOCATION_INTERFACE, T_TUT_ALLOCATION_OTHER, T_TUT_ALLOCATION_TOTAL, T_TUT_ASSESSMENT, T_TUT_ENTITY, T_TUT_ENTITY_ADDRESS, T_TUT_ENTITY_ID, T_TUT_ENTITY_NAME, T_TUT_ENTITY_RELATIONSHIP, T_TUT_LETTER, T_TUT_NSL_PARAGRAPH, T_TUT_RETURN, T_USER, T_USER_ACCESS, XXBW_KF_INV_TAX, XXBW_KF_NONPO_SUPP_DET, XXBW_KF_ORG_NAME_REQUEST, XXBW_KF_PO_SUPP_DET, XXBW_KF_REQUESTER, dtproperties, t_role_bakThe list of tables is quite long! Let's try to find the most relevant ones for the question "Get payment limit of this user id = INLABLB". I'm going to take a look at the schema of some tables that might be related to payments.

Action: sql_db_schema
Action Input: CT_PAYMENT_LIMIT, H_PAY_PAYMENT_RECEIPT_ONLINE, T_PAY_PAYMENT_RECEIPT, TEMP_EMS_ENTITY_IDError: table_names {'TEMP_EMS_ENTITY_ID'} not found in databaseIt looks like the `sql_db_schema` tool is returning an error because `TEMP_EMS_ENTITY_ID` is not a valid table name. Let's try to focus on the tables that are more relevant to payments.

Action: sql_db_schema
Action Input: CT_PAYMENT_LIMIT, H_PAY_PAYMENT_RECEIPT_ONLINE, T_PAY_PAYMENT_RECEIPT
CREATE TABLE [CT_PAYMENT_LIMIT] (
        [CD_ID_CODE] INTEGER NOT NULL IDENTITY(1,1), 
        [TX_LEVEL_NAME] NVARCHAR(100) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL, 
        [CD_LIMIT_DECODE] BIGINT NOT NULL
)

/*
3 rows from CT_PAYMENT_LIMIT table:
CD_ID_CODE      TX_LEVEL_NAME   CD_LIMIT_DECODE
1       Payment1        0
2       Payment2        100000
3       Payment3        500000
*/


CREATE TABLE [H_PAY_PAYMENT_RECEIPT_ONLINE] (
        [ID_HISTORY_AUTO] BIGINT NOT NULL IDENTITY(1,1), 
        [ID_PAIR] BIGINT NOT NULL, 
        [CD_ACTION_TYPE] SMALLINT NOT NULL, 
        [ID_ACTION_USER] BIGINT NOT NULL, 
        [DT_ACTION] DATETIME NULL, 
        [ID_PAY_RECEIPT_ONLINE_AUTO] BIGINT NOT NULL, 
        [ID_ENTITY_ID_TYPE] SMALLINT NULL, 
        [ID_ENTITY_ID_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [ID_ENTITY_AUTO] BIGINT NULL, 
        [CD_TAX_TYPE] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [CD_SUB_TYPE] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [SQ_ASSESSMENT_NO] SMALLINT NULL, 
        [DT_EFFECTIVE] DATETIME NULL, 
        [AM_PAYMENT] DECIMAL(18, 2) NULL DEFAULT ((0)), 
        [CD_BANK] SMALLINT NULL, 
        [CD_BANK_BRANCH] SMALLINT NULL, 
        [ID_BANK_ACCOUNT] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [CD_INPUT_SOURCE] SMALLINT NULL, 
        [CD_PAY_PROCESS] SMALLINT NULL, 
        [CD_PAYMENT_RECEIPT_STATUS] SMALLINT NULL, 
        [CD_DEBITTRIGGER] SMALLINT NULL, 
        [CD_TRANSACTION] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [DT_TAX_PD_BEGIN] DATETIME NULL, 
        [DT_TAX_PD_END] DATETIME NULL, 
        [CHQ_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [ID_PV_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [CD_SOURCE] SMALLINT NULL, 
        [CD_REASON] SMALLINT NULL, 
        [ID_CREATOR] BIGINT NULL, 
        [DT_CREATE] DATETIME NULL, 
        [ID_MODIFIER] BIGINT NULL, 
        [DT_MODIFY] DATETIME NULL, 
        [TX_REMARKS] NVARCHAR(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [IN_OBSOLETE] BIT NULL, 
        CONSTRAINT [PK_H_PAY_PAYMENT_RECEIPT_ONLINE] PRIMARY KEY ([ID_HISTORY_AUTO])
)

/*
3 rows from H_PAY_PAYMENT_RECEIPT_ONLINE table:
ID_HISTORY_AUTO ID_PAIR CD_ACTION_TYPE  ID_ACTION_USER  DT_ACTION       ID_PAY_RECEIPT_ONLINE_AUTO      ID_ENTITY_ID_TYPE       ID_ENTITY_ID_NO ID_ENTITY_AUTO CD_TAX_TYPE     CD_SUB_TYPE     SQ_ASSESSMENT_NO        DT_EFFECTIVE    AM_PAYMENT      CD_BANK CD_BANK_BRANCH  ID_BANK_ACCOUNT CD_INPUT_SOURCCD_PAY_PROCESS   CD_PAYMENT_RECEIPT_STATUS       CD_DEBITTRIGGER CD_TRANSACTION  DT_TAX_PD_BEGIN DT_TAX_PD_END   CHQ_NO  ID_PV_NO        CD_SOURCE     CD_REASON        ID_CREATOR      DT_CREATE       ID_MODIFIER     DT_MODIFY       TX_REMARKS      IN_OBSOLETE
1       0       2       41      2008-11-18 16:28:26     251     8       3000017916      22843   104     0       0       2008-11-18 00:00:00     50.00 None     None    None    103     61      51      0       8512    2008-01-01 00:00:00     2008-12-31 00:00:00     None    None    2       251     43    2008-11-18 16:19:24      43      2008-11-18 16:19:24     None    False
2       1       2       41      2008-11-18 16:28:26     251     8       3000017916      22843   104     0       0       2008-11-18 00:00:00     50.00 None     None    None    103     62      52      0       8512    2008-01-01 00:00:00     2008-12-31 00:00:00     None    None    2       251     43    2008-11-18 16:19:24      41      2008-11-18 16:28:26     None    False
3       0       2       40      2008-11-18 16:33:05     252     8       3000002714      22735   104     0       0       2008-11-18 00:00:00     500.00None     None    None    103     61      51      0       8512    2008-01-01 00:00:00     2008-12-31 00:00:00     None    None    6       251     41    2008-11-18 16:30:56      41      2008-11-18 16:30:56     None    False
*/


CREATE TABLE [T_PAY_PAYMENT_RECEIPT] (
        [ID_PAYMENT_RECEIPT_AUTO] BIGINT NOT NULL IDENTITY(1,1), 
        [ID_ENTITY_ID_TYPE] SMALLINT NULL, 
        [ID_ENTITY_ID_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [ID_ENTITY_AUTO] BIGINT NULL, 
        [CD_TAX_TYPE] SMALLINT NULL, 
        [CD_SUB_TYPE] SMALLINT NULL, 
        [DT_PAYMENT] DATETIME NULL, 
        [DT_EFFECTIVE] DATETIME NULL, 
        [AM_PAYMENT] DECIMAL(18, 2) NULL DEFAULT ((0)), 
        [CD_BANK] SMALLINT NULL, 
        [CD_BANK_BRANCH] SMALLINT NULL, 
        [ID_BANK_ACCOUNT] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [CD_INPUT_SOURCE] SMALLINT NULL, 
        [CD_PAY_PROCESS] SMALLINT NULL, 
        [CD_PAYMENT_MODE] SMALLINT NULL, 
        [SQ_ASSESSMENT_NO] SMALLINT NULL, 
        [DT_TAX_PD_BEGIN] DATETIME NULL, 
        [DT_TAX_PD_END] DATETIME NULL, 
        [CD_TRANSACTION] SMALLINT NULL, 
        [CD_DEBITRIGGER] SMALLINT NULL, 
        [CHQ_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [ID_PV_NO] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [IN_PAYMENT_TYPE] NCHAR(1) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [CD_SPOST_BRANCH] NVARCHAR(50) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [TX_REASON] NVARCHAR(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL, 
        [DT_RECEIPT] DATETIME NULL, 
        [CD_SOURCE] SMALLINT NULL, 
        [CD_REASON] SMALLINT NULL, 
        [ID_CREATOR] BIGINT NULL, 
        [DT_CREATE] DATETIME NULL, 
        [ID_MODIFIER] BIGINT NULL, 
        [DT_MODIFY] DATETIME NULL, 
        [IN_OTHERS] SMALLINT NULL, 
        CONSTRAINT [PK_T_PAY_PAYMENT_RECEIPT] PRIMARY KEY ([ID_PAYMENT_RECEIPT_AUTO])
)

/*
3 rows from T_PAY_PAYMENT_RECEIPT table:
ID_PAYMENT_RECEIPT_AUTO ID_ENTITY_ID_TYPE       ID_ENTITY_ID_NO ID_ENTITY_AUTO  CD_TAX_TYPE     CD_SUB_TYPE     DT_PAYMENT      DT_EFFECTIVE    AM_PAYMENT     CD_BANK CD_BANK_BRANCH  ID_BANK_ACCOUNT CD_INPUT_SOURCE CD_PAY_PROCESS  CD_PAYMENT_MODE SQ_ASSESSMENT_NO        DT_TAX_PD_BEGIN DT_TAX_PD_END CD_TRANSACTION   CD_DEBITRIGGER  CHQ_NO  ID_PV_NO        IN_PAYMENT_TYPE CD_SPOST_BRANCH TX_REASON       DT_RECEIPT      CD_SOURCE       CD_REASON     ID_CREATOR       DT_CREATE       ID_MODIFIER     DT_MODIFY       IN_OTHERS
164     8       3000012582      22797   104     0       2008-07-07 00:00:00     2008-07-07 00:00:00     200.00  1       1       1111112 1       63    2008-01-01 00:00:00      2008-12-31 00:00:00     None    0       11223344        05999611400085  1       1       Invalid PV      2008-07-07 00:00:00   2008-07-07 00:00:00      1       2008-07-07 00:00:00     None
165     8       3000012795      22800   104     0       2008-07-07 00:00:00     2008-07-07 00:00:00     300.00  1       1       2222233 1       63    2008-01-01 00:00:00      2008-12-31 00:00:00     None    0       22334455        05997923151043  1       1       Invalid PV      2008-07-07 00:00:00   2008-07-07 00:00:00      1       2008-07-07 00:00:00     None
166     8       3000015174      22819   104     0       2008-07-07 00:00:00     2008-07-07 00:00:00     500.00  1       1       55557889        1     63       1       1       2008-01-01 00:00:00     2008-12-31 00:00:00     None    0       33445566        05981800692018  1       1       None    2008-07-07 00:00:00    3       3       1       2008-07-07 00:00:00     1       2008-07-07 00:00:00     None
*/
```

### One table only
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