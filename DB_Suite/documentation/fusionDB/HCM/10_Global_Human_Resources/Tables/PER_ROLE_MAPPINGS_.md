# PER_ROLE_MAPPINGS_

Stores the mappings of the different roles.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappings-27353.html#perrolemappings-27353](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolemappings-27353.html#perrolemappings-27353)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ROLE_MAPPINGS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_MAPPING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ASSIGNMENT_STATUS | VARCHAR2 | 30 |  |  | Defines whether Assignment Status is active or inactive. |
| DATE_FROM | DATE |  |  |  | Date from which the Role Mapping is active. |
| DATE_TO | DATE |  |  |  | Date till when the Role Mapping is active. |
| MAPPING_NAME | VARCHAR2 | 255 |  |  | Name for the Role Mapping |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Foreign key to HRW_BUSINESS_UNITS table. |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | Foreign Key to PER_LEGAL_EMPLOYERS table. |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Department Identifier for Matching to Person Assignment |
| JOB_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOBS_F table. |
| POSITION_ID | NUMBER |  | 18 |  | Foreign Key to HR_ALL_POSITIONS_F table. |
| GRADE_ID | NUMBER |  | 18 |  | Foreign Key to PER_GRADES_F table. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |
| CURRENT_MANAGER_FLAG | VARCHAR2 | 30 |  |  | ?Flag to Indicate Matching to Manager Assignments |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Manager Type for Matching to Person Assignment |
| USER_PERSON_TYPE_ID | NUMBER |  | 18 |  | User Person Type Identifier for Matching to Person Assignment |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | System Person Type for Matching to Person Assignment |
| ASSIGNMENT_STATUS_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ASSIGNMENT_STATUS_TYPES table. |
| ASSIGNMENT_TYPE | VARCHAR2 | 30 |  |  | Assignment Type for Matching to Person Assignment |
| ALL_ROLES_REQUESTABLE_FLAG | VARCHAR2 | 30 |  |  | Flag to Indicate That All Roles are Requestable for Persons with Matching Assignment |
| RESOURCE_ROLE_ID | NUMBER |  | 18 |  | ?Resource Role Identifier for Matching |
| PARTY_USAGE_CODE | VARCHAR2 | 30 |  |  | ?Party Usage Code for Matching |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | Responsibility Type for Matching to Person Area of Responsibility |
| CONTACT_ROLE | VARCHAR2 | 30 |  |  | Contact Role for Matching to Role of Contacts |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RULE_TYPE | VARCHAR2 | 30 |  |  | autoprovisioning rule type |
| COUNTRY | VARCHAR2 | 30 |  |  | The country for which this role mapping applies. Implies all Locations within the specified country. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | The Legislative Data Group for which this role mapping applies |
| COLUMN_NAME1 | VARCHAR2 | 80 |  |  | Column name corresponding to flexfield segment. |
| OPERATOR1 | VARCHAR2 | 80 |  |  | Operator for condition. |
| VALUE1 | VARCHAR2 | 150 |  |  | Value to be used for condition. |
| COLUMN_NAME2 | VARCHAR2 | 80 |  |  | Column name corresponding to flexfield segment. |
| OPERATOR2 | VARCHAR2 | 80 |  |  | Operator for condition. |
| VALUE2 | VARCHAR2 | 150 |  |  | Value to be used for condition. |
| COLUMN_NAME3 | VARCHAR2 | 80 |  |  | Column name corresponding to flexfield segment. |
| OPERATOR3 | VARCHAR2 | 80 |  |  | Operator for condition. |
| VALUE3 | VARCHAR2 | 150 |  |  | Value to be used for condition. |
| COLUMN_NAME4 | VARCHAR2 | 80 |  |  | Column name corresponding to flexfield segment. |
| OPERATOR4 | VARCHAR2 | 80 |  |  | Operator for condition. |
| VALUE4 | VARCHAR2 | 150 |  |  | Value to be used for condition. |
| COLUMN_NAME5 | VARCHAR2 | 80 |  |  | Column name corresponding to flexfield segment. |
| OPERATOR5 | VARCHAR2 | 80 |  |  | Operator for condition. |
| VALUE5 | VARCHAR2 | 150 |  |  | Value to be used for condition. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ROLE_MAPPINGSN1_ | Non Unique | Default | ROLE_MAPPING_ID |
| PER_ROLE_MAPPINGSU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ROLE_MAPPING_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
