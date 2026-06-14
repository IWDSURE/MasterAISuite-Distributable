# HWR_PER_GBL_PRFL_B

The global person profile table is used to store a profile of a person.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflb-12679.html#hwrpergblprflb-12679](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflb-12679.html#hwrpergblprflb-12679)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PER_GBL_PRFL_B_PK | GBL_PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GLOBAL_PROFILE_ID | VARCHAR2 | 400 |  | Yes | This is the primary key for the global profile tables. | Obsolete |
| GBL_PRFL_ID | NUMBER |  | 18 | Yes | This is the primary key for the global profile tables. |  |
| GENDER_CODE | VARCHAR2 | 80 |  | Yes | A string code for gender: MALE, FEMALE or NA (not available). | Active |
| EMAIL | VARCHAR2 | 800 |  |  | This is the email address of the person. | Active |
| MENTOR_STATUS | NUMBER |  |  |  | This is for storing mentor status. |  |
| IMAGE_URL | VARCHAR2 | 4000 |  |  | The URL to the person's photo image. | Active |
| GAMIFICATION_USER_ID | VARCHAR2 | 400 |  |  | The Gamification user ID for this person. |  |
| GAMIFICATION_PLAYER_ID | VARCHAR2 | 400 |  |  | The Gamification player ID for this person. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_PER_GBL_PRFL_B_U1 | Unique | FUSION_TS_TX_DATA | GBL_PRFL_ID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
