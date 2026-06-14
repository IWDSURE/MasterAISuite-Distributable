# HWR_CNST_B

HWR_CNST_B: this table stores contests.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstb-3236.html#hwrcnstb-3236](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstb-3236.html#hwrcnstb-3236)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_B_PK | CONTEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONTEST_ID | NUMBER |  | 18 | Yes | This is the primary key of the table. |  |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |  |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |  |
| IS_TIES_ALLOWED | VARCHAR2 | 4 |  |  | This column indicated whether ties allowd or not for corresponding competition |  |
| NAME | VARCHAR2 | 512 |  |  | This is the name of the contest. |  |
| START_DATE | DATE |  |  |  | This column stores the start of the corresponding contest. |  |
| END_DATE | DATE |  |  |  | This column stores the end date of the corresponding contest. |  |
| CORPORATE_FLAG | VARCHAR2 | 4 |  |  | This column indicates if a contest is a coporate contest rather than a regular contest. |  |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | This is the description of the contest. |  |
| PARTICIPANT_TYPE | VARCHAR2 | 256 |  | Yes | Determines what type participants are allowed to participate in the contest. |  |
| IMAGE_URI | VARCHAR2 | 512 |  |  | This column stores the image URI for the current contest. |  |
| MAX_NO_PARTICIPANTS | NUMBER |  | 18 |  | This column stores the MaxNumberOfParticipants. |  |
| PARTICIPATION_RATE_TARGET | NUMBER |  | 18 |  | The column stores the target participation rate. |  |
| REWARD_ID | NUMBER |  | 18 |  | This column is a FK to HWR_CNST_REWARD_B  table. (OBSOLETE) | Obsolete |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_B_U1 | Unique | FUSION_TS_TX_DATA | CONTEST_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
