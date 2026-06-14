# HEX_PROCESS_METADATA

The table stores the metadata for the process being executed.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexprocessmetadata-30521.html#hexprocessmetadata-30521](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexprocessmetadata-30521.html#hexprocessmetadata-30521)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_PROCESS_METADATA_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | The column indicates a sequence generated value. |
| PROCESS_CODE | VARCHAR2 | 100 |  |  | The column indicates the Consumer Process Code. |
| PROCESS_NAME | VARCHAR2 | 400 |  |  | The column indicates the Consumer Process Name. |
| CLASS_NAME | VARCHAR2 | 4000 |  |  | The column indicates the Consumer Implementation Class Name. |
| SUB_CLASS_NAME | VARCHAR2 | 4000 |  |  | The column indicates the Consumer Implementation Sub Class Name. |
| PRE_PROCESS_PROCEDURE | VARCHAR2 | 4000 |  |  | The column indicates the Consumer Implementation pre process Procedure Name. |
| PROCESS_PROCEDURE | VARCHAR2 | 4000 |  |  | The column indicates the Consumer Implementation Procedure Name. |
| POST_PROCESS_PROCEDURE | VARCHAR2 | 4000 |  |  | The column indicates the Consumer Implementation post process Procedure Name. |
| ACTIVE_STATUS | VARCHAR2 | 1 |  |  | The column indicates if the specified process is active. |
| DEFAULT_THREADS | NUMBER |  | 18 |  | The column indicates the Default Thread Count value. |
| DEFAULT_CHUNK_SIZE | NUMBER |  | 18 |  | The column indicates the Default Chunk Size value. |
| DEFAULT_LOGGING | VARCHAR2 | 10 |  |  | The column indicates the Default Logging value. |
| DEFAULT_MAX_ERRORS | NUMBER |  | 18 |  | The column indicates the Default Max Errors Allowed value. |
| ALLOW_OVERRIDE_DEFAULTS | VARCHAR2 | 1 |  |  | The column indicates if the default values can be overridden with Payroll Configuration Group. |
| CONFIG_GROUP_TYPE | VARCHAR2 | 1 |  |  | The column indicates the type of configuration group used. |
| DEFAULT_CONFIG_GROUP | VARCHAR2 | 100 |  |  | The column indicates the default configuration group to be used for the process. |
| RETRIES | NUMBER |  |  |  | The column indicates the number of retries allowed. |
| ELEVATED | VARCHAR2 | 1 |  |  | The column indicates if the current process is elevated. Valid values are Y and N.Default value is N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_PROCESS_METADATA_PK | Unique | Default | PROCESS_ID, ORA_SEED_SET1 |
| HEX_PROCESS_METADATA_PK1 | Unique | Default | PROCESS_ID, ORA_SEED_SET2 |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
