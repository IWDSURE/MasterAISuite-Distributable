# CMP_TCS_PER_PERD_STMT_XML

Table that stores the XML data for pdf processing.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmtxml-18451.html#cmptcsperperdstmtxml-18451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsperperdstmtxml-18451.html#cmptcsperperdstmtxml-18451)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PERD_STMT_XML_ID | NUMBER |  | 18 | Yes | PER_PERD_STMT_XML_ID |
| PER_PERD_STMT_ID | NUMBER |  | 18 |  | PER_PERD_STMT_ID |
| STMT_ID | NUMBER |  | 18 |  | STMT_ID |
| PERD_RUN_ID | NUMBER |  | 18 |  | PERD_RUN_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| XML_LOB_STMT | CLOB |  |  |  | XML_LOB_STMT |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_PER_PERD_STMT_XML_N1 | Non Unique | Default | PER_PERD_STMT_ID |
| CMP_TCS_PER_PERD_STMT_XML_UK1 | Unique | Default | PER_PERD_STMT_XML_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
