# HWR_XP_STATEMENT_B

This is the table for the experience store statements.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpstatementb-16465.html#hwrxpstatementb-16465](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpstatementb-16465.html#hwrxpstatementb-16465)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_STATEMENT_B_PK | STATEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATEMENT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this statement. |
| UUID | VARCHAR2 | 255 |  |  | The universally unique identifier for this statement. |
| VERB_ID | NUMBER |  | 18 | Yes | The verb identifier for this statement. |
| ACTOR_ID | NUMBER |  | 18 | Yes | The actor identifier for this statement. |
| RESULT_ID | NUMBER |  | 18 |  | The result identifier for this statement. |
| CONTEXT_ID | NUMBER |  | 18 |  | The context identifier for this statement. |
| AUTHORITY_ID | NUMBER |  | 18 |  | The authority identifier(actor) for this statement. |
| TIMESTAMP | TIMESTAMP |  |  |  | The timestamp for this statement. |
| STORED | TIMESTAMP |  |  |  | The stored date for this statement. |
| OBJECT_TYPE | VARCHAR2 | 64 |  | Yes | The object type for this statement. |
| OBJECT_ACTIVITY_ID | NUMBER |  | 18 |  | The object activity id for this statement. |
| OBJECT_ACTOR_ID | NUMBER |  | 18 |  | The object actor id for this statement. |
| OBJECT_STATEMENT_ID | NUMBER |  | 18 |  | The object statement id for this statement. |
| REF_ACTIVITY_ID | NUMBER |  | 18 |  | This field is for search optimization and contains the activity value of the referred statement. |
| REF_ACTOR_ID | NUMBER |  | 18 |  | This field is for search optimization and contains the actor value of the referred statement. |
| REF_VERB_ID | NUMBER |  | 18 |  | This field is for search optimization and contains the verb value of the referred statement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_STATEMENT_B_N1 | Non Unique | Default | CONTEXT_ID |
| HWR_XP_STATEMENT_B_N10 | Non Unique | Default | OBJECT_ACTOR_ID |
| HWR_XP_STATEMENT_B_N11 | Non Unique | Default | OBJECT_STATEMENT_ID |
| HWR_XP_STATEMENT_B_N2 | Non Unique | Default | REF_ACTOR_ID |
| HWR_XP_STATEMENT_B_N3 | Non Unique | Default | REF_ACTIVITY_ID |
| HWR_XP_STATEMENT_B_N4 | Non Unique | Default | REF_VERB_ID |
| HWR_XP_STATEMENT_B_N5 | Non Unique | Default | VERB_ID |
| HWR_XP_STATEMENT_B_N6 | Non Unique | Default | ACTOR_ID |
| HWR_XP_STATEMENT_B_N7 | Non Unique | Default | RESULT_ID |
| HWR_XP_STATEMENT_B_N8 | Non Unique | Default | AUTHORITY_ID |
| HWR_XP_STATEMENT_B_N9 | Non Unique | Default | OBJECT_ACTIVITY_ID |
| HWR_XP_STATEMENT_B_U1 | Unique | Default | STATEMENT_ID |
| HWR_XP_STATEMENT_B_U2 | Unique | Default | UUID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
