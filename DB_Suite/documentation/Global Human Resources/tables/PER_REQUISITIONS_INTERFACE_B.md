# PER_REQUISITIONS_INTERFACE_B

The Main table to store Requisition data.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrequisitionsinterfaceb-15633.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrequisitionsinterfaceb-15633.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_REQ_INTERFACE_B_PK | REQUISITION_INTERFACE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUISITION_INTERFACE_ID | NUMBER |  | 18 | Yes | System generated Primary Key |
| REQUISITION_INTERFACE_CODE | VARCHAR2 | 30 |  | Yes | Requisition Interface code |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterpprise Id |
| INTERFACE_TYPE | VARCHAR2 | 30 |  |  | Describes type of request. |
| INTERFACE_SOURCE | VARCHAR2 | 30 |  |  | Describes source of request |
| INTERFACE_SOURCE_ID | NUMBER |  | 18 |  | Interface Source Id |
| VACANCY_STATUS | VARCHAR2 | 30 |  |  | Status of Vacancy |
| REQUISITION_NUMBER | VARCHAR2 | 20 |  |  | Request Number |
| REQUISITION_STATUS | VARCHAR2 | 30 |  |  | Status of Request |
| REQUISITION_JUSTIFICATION | VARCHAR2 | 30 |  |  | Need for Requisition |
| REQUISITION_TEMPLATE_CODE | VARCHAR2 | 30 |  |  | Request Name |
| TARGET_START_DATE | DATE |  |  |  | Target Start Date |
| JOB_SCHEDULE | VARCHAR2 | 30 |  |  | Type of Job |
| TOTAL_OPEN_HEADCOUNT | NUMBER |  | 18 |  | Total number of open head counts |
| TOTAL_HIRED_HEADCOUNT | NUMBER |  | 18 |  | Total number of hired head count |
| TOTAL_AVAILABLE_HEADCOUNT | NUMBER |  | 18 |  | Total number of available head counts |
| MANAGER_USER_NAME | VARCHAR2 | 100 |  |  | Manager User Name |
| MANAGER_ID | NUMBER |  | 18 |  | Manager Id |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Manager Assignment Id |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Type of Manager |
| JOB_ID | NUMBER |  | 18 |  | Job Id |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Organization Id |
| PRIMARY_LOCATION_ID | NUMBER |  | 18 |  | Location Id |
| POSITION_ID | NUMBER |  | 18 |  | Position Id |
| EMPLOYEE_STATUS | VARCHAR2 | 30 |  |  | Type Of Employee |
| UNLIMITED_HIRE | VARCHAR2 | 30 |  |  | Unlimited hire |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_REQ_INTERFACE_B_N1 | Non Unique | Default | REQUISITION_NUMBER |
| PER_REQ_INTERFACE_B_N2 | Non Unique | Default | MANAGER_ID, MANAGER_ASSIGNMENT_ID, MANAGER_TYPE |
| PER_REQ_INTERFACE_B_N3 | Non Unique | Default | JOB_ID |
| PER_REQ_INTERFACE_B_N4 | Non Unique | Default | PRIMARY_LOCATION_ID |
| PER_REQ_INTERFACE_B_N5 | Non Unique | Default | POSITION_ID |
| PER_REQ_INTERFACE_B_PK | Unique | Default | REQUISITION_INTERFACE_ID |
| PER_REQ_INTERFACE_B_U1 | Unique | Default | REQUISITION_INTERFACE_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
