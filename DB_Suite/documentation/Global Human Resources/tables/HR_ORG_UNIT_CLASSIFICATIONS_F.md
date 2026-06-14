# HR_ORG_UNIT_CLASSIFICATIONS_F

This holds the classification IDs for a given organization ID.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsf-24582.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsf-24582.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ORG_UNIT_CLASSIFICATION_PK | ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_UNIT_CLASSIFICATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS_F |
| CLASSIFICATION_CODE | VARCHAR2 | 40 |  | Yes | Foreign key to HR_ORG_CLASSIFICATIONS table. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| STATUS | VARCHAR2 | 30 |  | Yes | Indicates if an organization is active or inactive. |
| SET_ID | NUMBER |  | 18 |  | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | Extensible Flexfield Category Code |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ORG_UNIT_CLASSIFCATION_N1 | Non Unique | Default | CLASSIFICATION_CODE, CATEGORY_CODE, ORGANIZATION_ID |
| HR_ORG_UNIT_CLASSIFICATION_N2 | Non Unique | Default | SET_ID |
| HR_ORG_UNIT_CLASSIFICATION_PK | Unique | Default | ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_UNIT_CLASS_N3 | Non Unique | Default | LEGISLATION_CODE |
| HR_ORG_UNIT_CLASS_U1 | Unique | Default | LAST_UPDATE_DATE, ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORG_UNIT_CLASS_U2 | Unique | Default | ORGANIZATION_ID, CLASSIFICATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
