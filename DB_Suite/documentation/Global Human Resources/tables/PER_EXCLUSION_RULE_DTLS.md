# PER_EXCLUSION_RULE_DTLS

PER_EXCLUSION_RULE_DTLS to store Manager Type relates security preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexclusionruledtls-6383.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexclusionruledtls-6383.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXCLUSION_RULE_DTLS_PK | EXCLUSION_RULE_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXCLUSION_RULE_DTL_ID | NUMBER |  | 18 | Yes | Primary key. |
| EXCLUSION_RULE_ID | NUMBER |  | 18 | Yes | Foreign Key to Exclusion Rule. |
| FLEX_CONTEXT | VARCHAR2 | 80 |  |  | Flex Context name. |
| TABLE_NAME | VARCHAR2 | 80 |  |  | Table Name. |
| COLUMN_NAME | VARCHAR2 | 80 |  |  | Column Name. |
| OPERATOR | VARCHAR2 | 80 |  |  | Operator for condition. |
| ID_VALUE | NUMBER |  | 18 |  | Object Id.  For example, Position, Job, Business Unit Id. |
| VALUE | VARCHAR2 | 80 |  |  | Value to be used for condition. |
| TREE_CODE | VARCHAR2 | 80 |  |  | Tree code of tree to be used in hierarchy type exclusion. |
| TOP_NODE_VALUE | NUMBER |  | 18 |  | Top node in tree selected. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXCLUSION_RULE_DTLS_FK1 | Non Unique | Default | EXCLUSION_RULE_ID |
| PER_EXCLUSION_RULE_DTLS_PK | Unique | Default | EXCLUSION_RULE_DTL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
