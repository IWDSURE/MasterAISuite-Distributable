# HRA_TMPL_ROLES

This table stores roles that can be part of the appraisal process for documents created with this template. For example Reviewer, Other Participant, Appraiser.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplroles-16296.html#hratmplroles-16296](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplroles-16296.html#hratmplroles-16296)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_ROLES_PK | TMPL_ROLE_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TMPL_ROLE_ID | NUMBER |  | 18 | Yes | Primary key of the Template Roles. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| TEMPLATE_DEFN_ID | NUMBER |  | 18 | Yes | Foreign key of the Template Definition. |  |
| ROLE_ID | NUMBER |  | 18 | Yes | Foreign key of the Role Definition. |  |
| ROLE_TYPE_CODE | VARCHAR2 | 30 |  |  | Indicates the type of role i.e manager or worker or participant etc. |  |
| MINIMUM_NUM_PCPNS | NUMBER |  | 18 |  | Stores minimum number of participants required per role |  |
| MAXIMUM_NUM_PCPNS | NUMBER |  | 18 |  | Stores maximum number of participants required per role |  |
| MATRIX_PARTICIPANT_FLAG | VARCHAR2 | 30 |  |  | Indicates that role is matrix participant role |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_ROLES_PK | Unique | Default | TMPL_ROLE_ID, BUSINESS_GROUP_ID |
| HRA_TMPL_ROLES_UK1 | Unique | Default | TEMPLATE_DEFN_ID, TMPL_ROLE_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
