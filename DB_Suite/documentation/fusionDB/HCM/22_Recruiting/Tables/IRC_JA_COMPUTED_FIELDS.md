# IRC_JA_COMPUTED_FIELDS

This table stores the computed field configurations.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjacomputedfields-21506.html#ircjacomputedfields-21506](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjacomputedfields-21506.html#ircjacomputedfields-21506)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_COMPUTED_FIELDS_PK | COMPUTED_FIELD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMPUTED_FIELD_ID | NUMBER |  | 18 | Yes | Primary Key for the Table. System generated. |
| FLEX_CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | Flexfield context to be used for storing the computed field values. |
| FLEX_SEGMENT_CODE | VARCHAR2 | 30 |  | Yes | Flexfield segment to be used for storing the computed field values. |
| FORMULA_ID | NUMBER |  | 18 | Yes | Unique identifier of the fast formula. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_COMPUTED_FIELDS_PK | Unique | Default | COMPUTED_FIELD_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
