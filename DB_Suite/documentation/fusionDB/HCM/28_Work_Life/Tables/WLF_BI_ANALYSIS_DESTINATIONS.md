# WLF_BI_ANALYSIS_DESTINATIONS

Table to store analysis destinations

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfbianalysisdestinations-26939.html#wlfbianalysisdestinations-26939](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfbianalysisdestinations-26939.html#wlfbianalysisdestinations-26939)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_BI_ANALYSIS_DESTINATI_PK | ANALYSIS_REPORT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ANALYSIS_REPORT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| REPORT_NAME | VARCHAR2 | 4000 |  | Yes | Name of the BI Analysis Report |
| REPORT_PATH | VARCHAR2 | 4000 |  |  | Relative path of the Report along with the Report Name. Column being made redundant from 20.01 and will not store any data. |
| LEARNING_ITEM_NUM_PROMPT_VAL | VARCHAR2 | 30 |  |  | Column to capture Learning Item Number information that can be used within Analysis as prompted filter. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_BI_ANALYSIS_DEST_U1 | Unique | Default | ANALYSIS_REPORT_ID |
| WLF_BI_ANALYSIS_DEST_U2 | Unique | Default | REPORT_NAME, LEARNING_ITEM_NUM_PROMPT_VAL |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
