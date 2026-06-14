# PER_EXCLUSION_RULES_

PER_EXCLUSION_RULES to store Manager exclusion relates security preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexclusionrules-17445.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perexclusionrules-17445.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EXCLUSION_RULES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, EXCLUSION_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXCLUSION_RULE_ID | NUMBER |  | 18 | Yes | Primary key. |
| NAME | VARCHAR2 | 30 |  |  | Name of the exclusion rule. |
| DESCRIPTION | VARCHAR2 | 200 |  |  | Description of the exclusion rule. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This field represents whether a exclusion rule is enabled or disabled. When it is enabled, it can be associated with a person security profile. |
| EXCLUSION_TYPE | VARCHAR2 | 30 |  |  | Exclusion pattern selected for exclusion configuration. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EXCLUSION_RULESN1_ | Non Unique | Default | EXCLUSION_RULE_ID, LAST_UPDATE_DATE |
| PER_EXCLUSION_RULES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, EXCLUSION_RULE_ID |
| PER_EXCLUSION_RULES_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, UPPER("NAME") |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
