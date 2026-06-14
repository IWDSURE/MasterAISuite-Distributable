# WLF_AR_RELATIONS_F

Table to store Assignment Relations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfarrelationsf-13668.html#wlfarrelationsf-13668](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfarrelationsf-13668.html#wlfarrelationsf-13668)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_AR_RELATIONS_F_PK | RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RELATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ASSIGNMENT_RECORD_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_RECORD_ID that this is related to |
| RELATION_TYPE | VARCHAR2 | 30 |  | Yes | The type of the relationship |
| RELATED_OBJECT_TYPE | VARCHAR2 | 20 |  | Yes | RELATED_OBJECT_TYPE |
| RELATED_OBJECT_ID | NUMBER |  | 18 | Yes | RELATED_OBJECT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PRIMARY_FLAG | VARCHAR2 | 1 |  |  | Identifier for choosing primary relationship |
| INVERSE_RELATION_TYPE | VARCHAR2 | 30 |  |  | this column is to store Target to source relation in case of Assignment Conflict Rules defined |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_AR_RELATIONS_F_N1 | Non Unique | Default | ASSIGNMENT_RECORD_ID |
| WLF_AR_RELATIONS_F_N2 | Non Unique | Default | RELATED_OBJECT_ID, RELATION_TYPE |
| WLF_AR_RELATIONS_F_N3 | Non Unique | Default | INVERSE_RELATION_TYPE, RELATED_OBJECT_ID |
| WLF_AR_RELATIONS_F_U1 | Unique | Default | RELATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
