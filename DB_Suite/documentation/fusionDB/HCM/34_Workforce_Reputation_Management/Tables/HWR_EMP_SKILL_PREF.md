# HWR_EMP_SKILL_PREF

This table stores the employee skill preferences information

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrempskillpref-27851.html#hwrempskillpref-27851](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrempskillpref-27851.html#hwrempskillpref-27851)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EMP_SKILL_PREF_PK | FUS_PRFL_ID#01, TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GLBL_PRFL_ID | NUMBER |  | 18 |  | This column stores the global profile id. |  |
| FUS_PRFL_ID | NUMBER |  | 18 |  | FUS_PRFL_ID | Obsolete |
| FUS_PRFL_ID#01 | NUMBER |  | 18 | Yes | This column stores the fusion profile ID. |  |
| TOPIC_ID | NUMBER |  | 18 | Yes | This column stores the topic id. |  |
| TOPIC_KEY | VARCHAR2 | 400 |  | Yes | This column is used to store the topic key. |  |
| CATEGORY_ID | NUMBER |  | 18 |  | This column is used to store the catgory id. |  |
| CATEGORY_KEY | VARCHAR2 | 400 |  | Yes | This column is used to store the category key. |  |
| IS_NEW | NUMBER |  | 1 |  | This column indicates if it is new. |  |
| PROFICIENCY | NUMBER |  | 1 |  | This column contains the proficiency id of the skill |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_EMP_SKILL_PREF_N1 | Non Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID#01, TOPIC_ID | Obsolete |
| HWR_EMP_SKILL_PREF_U1 | Unique | FUSION_TS_TX_DATA | FUS_PRFL_ID#01, TOPIC_ID |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
