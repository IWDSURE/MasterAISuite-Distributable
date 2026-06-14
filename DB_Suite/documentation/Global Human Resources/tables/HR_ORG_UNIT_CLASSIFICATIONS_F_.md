# HR_ORG_UNIT_CLASSIFICATIONS_F_

This holds the classification IDs for a given organization ID.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsf-11727.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsf-11727.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ORG_UNIT_CLASSIFICATION_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_UNIT_CLASSIFICATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |
| CLASSIFICATION_CODE | VARCHAR2 | 40 |  |  | Foreign key to HR_ORG_CLASSIFICATIONS table. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| STATUS | VARCHAR2 | 30 |  |  | Indicates if an organization is active or inactive. |
| SET_ID | NUMBER |  | 18 |  | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extensible Flexfield Category Code |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ORG_UNIT_CLASSIFICATION_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_UNIT_CLASS_FN1_ | Non Unique | Default | ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_UNIT_CLASS_U1_ | Unique | Default | LAST_UPDATED_BY, LAST_UPDATE_DATE, ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_UNIT_CLASS_U2_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORGANIZATION_ID, CLASSIFICATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
