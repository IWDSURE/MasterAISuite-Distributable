# HWR_CNST_REWARD_B

This table contains the reward description for a contest.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstrewardb-25373.html#hwrcnstrewardb-25373](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstrewardb-25373.html#hwrcnstrewardb-25373)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_REWARD_B_PK | REWARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REWARD_ID | NUMBER |  | 18 | Yes | This column is the primary key for this table |
| REWARD_ORDER | NUMBER |  | 18 |  | Storing sequence order of rewards |
| NO_OF_REWARDS | NUMBER |  | 18 |  | Storing number of rewards information |
| NAME | VARCHAR2 | 512 |  | Yes | This columns contians the name of the reward tuple |
| DESCRIPTION | VARCHAR2 | 4000 |  | Yes | this column contains the description of the current tuple |
| VALUE | NUMBER |  | 18 |  | This column indicates the value of the reward. |
| UNIT | VARCHAR2 | 256 |  |  | This column indicates the unit of the reward |
| MAX_NO_RECIPIENTS | NUMBER |  | 18 |  | This column stores the MaxNumberOfRecipients |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_REWARD_B_U1 | Unique | FUSION_TS_TX_DATA | REWARD_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
