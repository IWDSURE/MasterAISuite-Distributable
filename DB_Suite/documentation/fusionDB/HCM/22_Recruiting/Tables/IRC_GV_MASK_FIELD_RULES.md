# IRC_GV_MASK_FIELD_RULES

This table is created to save the rules to be applied for unmasking the data.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvmaskfieldrules-25617.html#ircgvmaskfieldrules-25617](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvmaskfieldrules-25617.html#ircgvmaskfieldrules-25617)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_MASK_FIELD_RULES_PK | MASK_FIELD_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASK_FIELD_RULE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| GV_CONTEXT_CODE | VARCHAR2 | 100 |  | Yes | Stores the context code for which all the views will be stored. For example : Context can be ORA_SUBMISSION and all the rules related to Unmask would be specified with this context code. |
| MASK_EXPRESSION | VARCHAR2 | 2000 |  | Yes | Stores EL expression to mask data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GV_MASK_FIELD_RULES_PK | Unique | Default | MASK_FIELD_RULE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
