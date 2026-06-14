# HWR_COMPETENCY_B

The competency table stores profile competency data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcompetencyb-8292.html#hwrcompetencyb-8292](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcompetencyb-8292.html#hwrcompetencyb-8292)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_COMPETENCY_B_PK | SOURCE_ID, COMPETENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPETENCY_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the competency table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the competency. |
| COMPETENCY_TEXT | CLOB |  |  |  | This is the full text of the competency. |
| EVALUATION_TYPE | VARCHAR2 | 255 |  |  | This is the evaluation type of the competency. |
| PROFICIENCY | VARCHAR2 | 1000 |  |  | This is the proficiency of the competency. |
| START_DATE | TIMESTAMP |  |  |  | This is the start date of the competency. |
| END_DATE | TIMESTAMP |  |  |  | This is the end date of the competency. |
| YEARS_OF_EXPERIENCE | NUMBER |  |  |  | This is the number of years of experience of the competency. |
| LAST_USED_DATE | TIMESTAMP |  |  |  | This is the last used date of the competency. |
| ACQUIRED_DATE | TIMESTAMP |  |  |  | This is the acquired date of the competency. |
| RECOMMENDER_ID | VARCHAR2 | 500 |  |  | This is the unique Id of the recommender. |
| RECOMMENDER_URI | VARCHAR2 | 500 |  |  | This is the URI identifying the recommender. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_COMPETENCY_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, COMPETENCY_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
