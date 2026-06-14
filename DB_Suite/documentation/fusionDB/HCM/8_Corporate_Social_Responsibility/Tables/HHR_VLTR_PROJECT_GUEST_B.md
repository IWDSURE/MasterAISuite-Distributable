# HHR_VLTR_PROJECT_GUEST_B

This table stores base  guest information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguestb-21710.html#hhrvltrprojectguestb-21710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguestb-21710.html#hhrvltrprojectguestb-21710)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_PROJECT_GUEST_B_PK | GUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| GUEST_ID | NUMBER |  | 18 | Yes | GUEST_ID |  |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |  |
| VOLUNTEER_ID | NUMBER |  | 18 | Yes | VOLUNTEER_ID | Obsolete |
| HCM_PERSON_ID | NUMBER |  | 18 | Yes | HCM_PERSON_ID |  |
| T_SIZE | VARCHAR2 | 20 |  |  | T_SIZE |  |
| T_STYLE | VARCHAR2 | 20 |  |  | T_STYLE |  |
| IS_MINOR | NUMBER |  | 1 |  | IS_MINOR |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HHR_VLTR_PROJECT_GUEST_B_U1 | Unique | FUSION_TS_TX_IDX | GUEST_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
