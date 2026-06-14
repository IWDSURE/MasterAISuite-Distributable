# PAY_AMER_INTERFACE_PARAMETERS

This table contains the file version and parameter details of various North America processes.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerinterfaceparameters-22810.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payamerinterfaceparameters-22810.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_AMER_INTERFACE_PARAME_PK | INTERFACE_PARAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERFACE_PARAM_ID | NUMBER |  | 18 | Yes | Unique Key to identify a record |
| CONTENT_PROVIDER | VARCHAR2 | 30 |  | Yes | Data Source Provider |
| VERSION_LOADED | VARCHAR2 | 30 |  | Yes | Version of file last loaded by the process |
| CONTENT_FILE_LOCATION | VARCHAR2 | 240 |  | Yes | Location of file last used by the process |
| CONTENT_FILE_NAME | VARCHAR2 | 240 |  | Yes | Name of the file last used by the process |
| UPLOADED_OLDER_VERSION | VARCHAR2 | 1 |  |  | Flag to indicate if the process uploaded previous or older version of file |
| PROCESS_NAME | VARCHAR2 | 30 |  | Yes | Unique Name to identify the process |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | Country Code |
| PROCESS_UPDATE_DATE | DATE |  |  | Yes | Identifies the date when the process has last loaded the latest version of file |
| CONTEXT_VALUE1 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE1 |
| CONTEXT_VALUE2 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE2 |
| CONTEXT_VALUE3 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE3 |
| CONTEXT_VALUE4 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE4 |
| CONTEXT_VALUE5 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE5 |
| CONTEXT_VALUE6 | VARCHAR2 | 30 |  |  | CONTEXT_VALUE6 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_AMER_INTERFACE_PARAME_U1 | Unique | Default | INTERFACE_PARAM_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
