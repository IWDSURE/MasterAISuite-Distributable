# PER_GENERATED_DATA_ROLES_

This table stores the information related to data roles created on a Job Role.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergenerateddataroles-30396.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergenerateddataroles-30396.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GENERATED_DATA_ROLES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GENERATED_DATA_ROLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GENERATED_DATA_ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| BASE_ROLE_ID | NUMBER |  | 18 |  | This field represents an internal ID for the job role inherited by a data role. |
| DATA_ROLE_ID | NUMBER |  | 18 |  | This field represents an internal ID for the role to which security profiles are assigned via the data roles UI. |
| DATA_ROLE_NAME | VARCHAR2 | 240 |  |  | Internal name for the role to which security profiles are assigned via the data roles UI. |
| DATA_ROLE_DISPLAY_NAME | VARCHAR2 | 240 |  |  | Display name for the role to which security profiles are assigned via the data roles UI. |
| DATA_ROLE_DESCRIPTION | VARCHAR2 | 240 |  |  | Role description of the role to which security profiles are assigned via the data roles UI. |
| APP_ROLE_NAME | VARCHAR2 | 240 |  |  | Role name of an internal application role. |
| APP_ROLE_DISPLAY_NAME | VARCHAR2 | 240 |  |  | Display name of an internal application role. |
| APP_ROLE_DESCRIPTION | VARCHAR2 | 240 |  |  | Role description of an internal application role. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DELEGATION_ALLOWED | VARCHAR2 | 30 |  |  | DELEGATION_ALLOWED |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_GENERATED_DATA_ROLESN1_ | Non Unique | Default | GENERATED_DATA_ROLE_ID |
| PER_GENERATED_DATA_ROLES_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, GENERATED_DATA_ROLE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
