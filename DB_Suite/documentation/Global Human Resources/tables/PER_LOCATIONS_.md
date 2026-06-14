# PER_LOCATIONS_

PER_LOCATIONS is the parent table.It stores generic location attributes.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocations-11452.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocations-11452.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOCATIONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SET_ID | NUMBER |  | 18 |  | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |
| INTERNAL_LOCATION_CODE | VARCHAR2 | 150 |  |  | Code of the Location |
| LOCATION_IMAGE_URL | VARCHAR2 | 1000 |  |  | Represents the web address for the location image. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | CATEGORY_CODE |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COUNTRY | VARCHAR2 | 60 |  |  | Country of the address |
| EMPLOYEE_LOCATION_FLAG | VARCHAR2 | 1 |  |  | Indicates the location is an employee location. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LOCATIONSN1_ | Non Unique | Default | LOCATION_ID, LAST_UPDATE_DATE |
| PER_LOCATIONS_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID |
| PER_LOCATIONS_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, BUSINESS_GROUP_ID, SET_ID, INTERNAL_LOCATION_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
