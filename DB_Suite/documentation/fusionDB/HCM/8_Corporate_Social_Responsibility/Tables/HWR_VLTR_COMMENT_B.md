# HWR_VLTR_COMMENT_B

This table stores base for comments

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcommentb-23813.html#hwrvltrcommentb-23813](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcommentb-23813.html#hwrvltrcommentb-23813)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_COMMENT_B_PK | COMMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMMENT_ID | NUMBER |  | 18 | Yes | COMMENT_ID |
| ENTITY_STATE | VARCHAR2 | 100 |  |  | ENTITY_STATE |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| ENTITY_TYPE | VARCHAR2 | 100 |  |  | ENTITY_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_COMMENT_B_N1 | Non Unique | FUSION_TS_TX_IDX | ENTITY_ID, ENTITY_TYPE |
| HWR_VLTR_COMMENT_B_U1 | Unique | FUSION_TS_TX_IDX | COMMENT_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
