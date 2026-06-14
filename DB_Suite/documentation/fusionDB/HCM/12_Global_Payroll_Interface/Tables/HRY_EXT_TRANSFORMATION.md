# HRY_EXT_TRANSFORMATION

Stores information related to transformation.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryexttransformation-30626.html#hryexttransformation-30626](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryexttransformation-30626.html#hryexttransformation-30626)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EXT_TRANSFORMATION_PK | TRANSFORMATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRANSFORMATION_ID | NUMBER |  | 18 | Yes | Primary key for HRY_EXT_TRANSFORMATION |
| FLOW_INSTANCE_ID | NUMBER |  | 18 |  | For storing FLOW_INSTANCE_ID |
| SEQUENCE | NUMBER |  | 18 |  | For storing the sequence number. |
| INSTANCE_NAME | VARCHAR2 | 200 |  |  | For storing instance name entered by the usr as input paameter to the ESS job |
| EXT_DEFINITION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_EXT_DEFINITIONS_B |
| LIBRARY_OPTION | VARCHAR2 | 40 |  |  | For storing library used for transformation.This parameter is entered by the user. |
| SPLIT_KEY | VARCHAR2 | 800 |  |  | For storing xpath of the xml tag that is needed for parsing |
| PROCESSING_TYPE | VARCHAR2 | 80 |  |  | For storing processing type which can be either TRANSFORMATION or VALUEMAP |
| STATUS | VARCHAR2 | 200 |  |  | For storing overall all status of the process.It can hold one of the values. PARSING_IN_PROGRESS/PARSING_COMPLETED/TRANSFORMATION_NOT_STARTED/TRANSFORMATION_IN_PROGRESS/TRANSFORMATION_COMPLETED/APPEND_NOT_STARTED/APPEND_IN_PROGRESS/APPEND_COMPLETED/CLEANUP_NOT_STARTED/CLEANUP_IN_PROGRESS/CLEANUP_COMPLETED |
| TRANSFORMED_FILE | CLOB |  |  |  | For storing large xml that is formed after appending all the transformed sub xmls as a result of VALUE MAP transformation |
| IS_RETENTION_REQUIRED | VARCHAR2 | 1 |  |  | For storing retention flag which if true will reten the data for the number of days saved under retention_days column else data will be deleted as soon as the prcoess is completed. |
| RETENTION_DAYS | NUMBER |  | 2 | Yes | For storing number of retention days.Maximum can be 30. |
| REQUESTID | NUMBER |  | 18 |  | For storing the request ID of the job that created or last updated the row. |
| SOURCE_ID | NUMBER |  | 18 |  | For storing payroll_action_id value that will be required for Value map transformation. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EXT_TRANSFORMATION_PK | Unique | Default | TRANSFORMATION_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
