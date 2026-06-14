# WLF_LI_SEQUENCE_RULES_F

This table is used to store sequence rules of activities inside a specialization or offering

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflisequencerulesf-23344.html#wlflisequencerulesf-23344](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflisequencerulesf-23344.html#wlflisequencerulesf-23344)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_SEQUENCE_RULES_F_PK | SEQUENCE_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCE_RULE_ID | NUMBER |  | 18 | Yes | Column value represents primary key |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SEQUENCE_RULE_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify Sequence Rule. |
| HIERARCHY_ID | NUMBER |  | 18 |  | Column value represents the hierarchy id for which sequence rule is applied |
| SEQUENCE_RULE | VARCHAR2 | 256 |  |  | Column value represent dependent learning item required  for  accessing Hierarchy Id |
| SEQUENCE_TYPE | VARCHAR2 | 32 |  |  | Column value is used to represent the sequence type , will have predecessor as value. |
| PARENT_LEARNING_ITEM_ID | NUMBER |  | 18 |  | Represents learningitemid of owning entity.
 If sequence rule defined is for activity then it represent section learningitemid.
 If sequence rule is for section then it represents specialization or offering learningitemid |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_SEQUENCE_RULES_F_N1 | Non Unique | Default | HIERARCHY_ID |
| WLF_LI_SEQUENCE_RULES_F_N2 | Non Unique | Default | SEQUENCE_RULE |
| WLF_LI_SEQUENCE_RULES_F_N3 | Non Unique | Default | PARENT_LEARNING_ITEM_ID |
| WLF_LI_SEQUENCE_RULES_F_N4 | Non Unique | Default | SEQUENCE_RULE_NUMBER |
| WLF_LI_SEQUENCE_RULES_F_N5 | Non Unique | WLF_LI_SEQUENCE_RULES_F_N5 | TO_CHAR("HIERARCHY_ID"), SEQUENCE_RULE |
| WLF_LI_SEQUENCE_RULES_F_U1 | Unique | Default | SEQUENCE_RULE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
