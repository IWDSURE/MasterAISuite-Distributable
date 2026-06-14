# BEN_LER_RL_F

BEN_LER_RL_F identifies one or more eligibility, document approval, and alert related rules to a life event for the purpose of determining a person's eligibility to participate, document approval setup for self reporting life events, and the alert setup respectively

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerrlf-31671.html#benlerrlf-31671](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerrlf-31671.html#benlerrlf-31671)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_RL_F_PK | LER_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LER_RL_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LER_ID | NUMBER |  | 18 | Yes | This column holds foreign key to BEN_LER_F |
| RL_TYP_CD | VARCHAR2 | 30 |  | Yes | This column holds life event rule type |
| STATUS_CD | VARCHAR2 | 30 |  | Yes | This column holds life event rule status. |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | This column holds life event rule Description |
| ELIGY_PRFL_ID | NUMBER |  | 18 |  | Foreign key to BEN_ELIGY_PRFL_F |
| SEQ_NUM | NUMBER |  | 9 |  | Sequence Number for Eligibility |
| ELIG_REQD | VARCHAR2 | 30 |  |  | Eligibility required flag Y or N |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to HR_DOCUMENT_TYPES_F |
| DOC_REQD | VARCHAR2 | 30 |  |  | This column holds document required flag Y or N |
| APPROVAL_REQD | VARCHAR2 | 30 |  |  | This column holds approval required flag Y or N |
| APPROVAL_ALERT_REQD | VARCHAR2 | 30 |  |  | Approval alert required flag Y or N |
| STAT_ANTHR_EVT_STRTD | VARCHAR2 | 30 |  |  | Status of potential life event if another life event is in started state. Manual or Unprocessed are possible values |
| ALERT_TYP_CD | VARCHAR2 | 30 |  |  | This column holds alert type code |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use |
| SYSTEM_DOCUMENT_TYPE | VARCHAR2 | 120 |  |  | Document type code for the specific document type Id. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_RL_F_N1 | Non Unique | Default | ELIGY_PRFL_ID |
| BEN_LER_RL_F_N2 | Non Unique | Default | LER_ID, RL_TYP_CD, STATUS_CD |
| BEN_LER_RL_F_N3 | Non Unique | Default | DOCUMENT_TYPE_ID |
| BEN_LER_RL_F_PK | Unique | Default | LER_RL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
