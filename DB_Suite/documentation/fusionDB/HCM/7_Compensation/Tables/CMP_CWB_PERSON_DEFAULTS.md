# CMP_CWB_PERSON_DEFAULTS

Stores data related to UI properties in worksheet for each user in a given plan and period.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersondefaults-21915.html#cmpcwbpersondefaults-21915](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpersondefaults-21915.html#cmpcwbpersondefaults-21915)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_PERSON_DEFAULTS_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| DISPLAY_ROWS | NUMBER |  | 3 |  | DISPLAY_ROWS |
| FREEZE_COLS | NUMBER |  | 2 |  | FREEZE_COLS |
| TABLE_VIEW | NUMBER |  | 1 |  | TABLE_VIEW |
| FILTER_REPORTS | NUMBER |  | 18 |  | FILTER_REPORTS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| TABLE_DENSITY | VARCHAR2 | 30 |  |  | TABLE_DENSITY |
| INSTRUCTIONS_FLAG | VARCHAR2 | 30 |  |  | INSTRUCTIONS_FLAG |
| SUMMARY_SECTION_FLAG | VARCHAR2 | 30 |  |  | SUMMARY_SECTION_FLAG |
| FILTERS_FLAG | VARCHAR2 | 30 |  |  | FILTERS_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_PERSON_DEFAULTS_U1 | Unique | Default | PERSON_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
