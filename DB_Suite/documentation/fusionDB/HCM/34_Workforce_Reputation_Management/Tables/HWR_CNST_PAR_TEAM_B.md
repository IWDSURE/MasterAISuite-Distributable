# HWR_CNST_PAR_TEAM_B

This table store teams participating in contests.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstparteamb-10375.html#hwrcnstparteamb-10375](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstparteamb-10375.html#hwrcnstparteamb-10375)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_PAR_TEAM_B_PK | CONTEST_TEAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_TEAM_ID | NUMBER |  | 18 | Yes | This is the primary key of the table. |
| NAME | VARCHAR2 | 512 |  |  | This column stores the name of the corresponding contest team. |
| IMAGE_URI | VARCHAR2 | 1000 |  |  | This column stores the image uri associated with this row |
| CONTEST_PARTICIPANT_ID | NUMBER |  | 18 |  | This column is a foreign key to HWR_CNST_PAR_IND_B table. It indicates the owner of the current team |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_PAR_TEAM_B_N1 | Non Unique | FUSION_TS_TX_DATA | CONTEST_PARTICIPANT_ID |
| HWR_CNST_PAR_TEAM_B_U1 | Unique | FUSION_TS_TX_DATA | CONTEST_TEAM_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
