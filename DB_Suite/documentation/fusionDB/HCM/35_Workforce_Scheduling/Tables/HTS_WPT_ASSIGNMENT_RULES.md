# HTS_WPT_ASSIGNMENT_RULES

Table to store the work pattern template assignment rules information

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htswptassignmentrules-4085.html#htswptassignmentrules-4085](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htswptassignmentrules-4085.html#htswptassignmentrules-4085)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_WPT_ASSIGNMENT_RULES_PK | WPT_ASSIGNMENT_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WPT_ASSIGNMENT_RULE_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for a work pattern assignment rule |
| WPT_ASSIGNMENT_RULE_CODE | VARCHAR2 | 30 |  | Yes | Unique code entered when creating a work pattern assignment rule, in order to help user identify the work pattern assignment rule |
| WORK_PATTERN_TEMPLATE_ID | NUMBER |  | 18 | Yes | Identifier of work pattern template to which the assignment rule is applicable |
| RULE_TYPE | VARCHAR2 | 30 |  |  | Type of assignment rule |
| LEVEL_TYPE | VARCHAR2 | 30 |  |  | Level for which assignment rule is applicable |
| LEVEL_OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the level for which assignment rule is applicable |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_WPT_ASSIGNMENT_RULES_N1 | Non Unique | Default | WORK_PATTERN_TEMPLATE_ID |
| HTS_WPT_ASSIGNMENT_RULES_N2 | Non Unique | Default | LEVEL_TYPE, LEVEL_OBJECT_ID |
| HTS_WPT_ASSIGNMENT_RULES_PK | Unique | Default | WPT_ASSIGNMENT_RULE_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
