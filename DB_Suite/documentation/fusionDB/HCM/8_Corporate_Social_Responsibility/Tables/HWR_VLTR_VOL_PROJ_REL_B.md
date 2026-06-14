# HWR_VLTR_VOL_PROJ_REL_B

this table store project relation

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolprojrelb-12402.html#hwrvltrvolprojrelb-12402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrvolprojrelb-12402.html#hwrvltrvolprojrelb-12402)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_VOL_PROJ_REL_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |  |
| SOURCE_ID | NUMBER |  | 18 |  | This column used to store the id of communication source. |  |
| CONVERSATION_ID | VARCHAR2 | 100 |  |  | This column used to store the id of conversation. |  |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |  |
| VOLUNTEER_ID | NUMBER |  | 18 | Yes | VOLUNTEER_ID | Obsolete |
| HCM_PERSON_ID | NUMBER |  | 18 |  | HCM_PERSON_ID |  |
| PROJECT_ID | NUMBER |  | 18 | Yes | PROJECT_ID |  |
| NUM_MINORS | NUMBER |  | 4 |  | NUM_MINORS |  |
| T_SIZE | VARCHAR2 | 20 |  |  | T_SIZE |  |
| T_STYLE | VARCHAR2 | 20 |  |  | T_STYLE |  |
| SUBSCRIPTION_DATE | TIMESTAMP |  |  | Yes | SUBSCRIPTION_DATE |  |
| SUBSCRIPTION_ENDDATE | TIMESTAMP |  |  |  | SUBSCRIPTION_ENDDATE |  |
| VERSION | NUMBER |  | 10 | Yes | VERSION |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_VOL_PROJ_REL_U1 | Unique | FUSION_TS_TX_IDX | ID |
| hwr_vltr_vol_proj_rel_b_U1 | Unique | Default | PROJECT_ID, HCM_PERSON_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
