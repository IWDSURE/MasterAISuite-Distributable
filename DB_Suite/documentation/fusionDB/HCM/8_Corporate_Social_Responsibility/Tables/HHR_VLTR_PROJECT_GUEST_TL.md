# HHR_VLTR_PROJECT_GUEST_TL

This table stores base  guest translation information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguesttl-12836.html#hhrvltrprojectguesttl-12836](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguesttl-12836.html#hhrvltrprojectguesttl-12836)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_PROJECT_GUEST_TL_PK | GUEST_ID, PROJECT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GUEST_ID | NUMBER |  | 18 | Yes | GUEST_ID |  |
| VOLUNTEER_ID | NUMBER |  | 18 |  | VOLUNTEER_ID | Obsolete |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| FIRST_NAME | VARCHAR2 | 500 |  |  | This is the first name of the project guest |  |
| LAST_NAME | VARCHAR2 | 500 |  |  | This is the last name of the project guest |  |
| EMAIL | VARCHAR2 | 800 |  |  | This is the email of the project guest |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_PROJECT_GUEST_TL_U1 | Unique | FUSION_TS_TX_IDX | GUEST_ID, PROJECT_ID, LANGUAGE |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
