# HWR_ISSUE_B

This table stores reputation control issues.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrissueb-19527.html#hwrissueb-19527](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrissueb-19527.html#hwrissueb-19527)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ISSUE_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| GBL_PRFL_ID | NUMBER |  | 18 |  | This is global profile id of the user |
| ORG_ID | VARCHAR2 | 80 |  |  | Indicates the identifier of the business unit associated to the row. |
| CONTROL_KEY | VARCHAR2 | 64 |  | Yes | The key of the reputation control from the HWR_REP_CONTROL_B table. |
| RELEVANCE | NUMBER |  |  |  | This is the relevance value for this post. |
| NUM_OCCURRENCES | NUMBER |  |  |  | This is the number of occurrences for this result. |
| SRC_POST_ID | VARCHAR2 | 500 |  |  | This is the id of the post from the source. |
| MESSAGE | CLOB |  |  |  | This is the message that was posted. |
| POST_DATE | TIMESTAMP |  |  |  | The date on which the post was created. |
| PRFL_ID | VARCHAR2 | 500 |  |  | The id of the profile that posted this post. |
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the Id of the source in the HWR_SRC_SOURCE_B table. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ISSUE_B_N1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID |
| HWR_ISSUE_B_U1 | Unique | FUSION_TS_TX_DATA | ID |
| HWR_ISSUE_B_U2 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, CONTROL_KEY, SRC_POST_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
