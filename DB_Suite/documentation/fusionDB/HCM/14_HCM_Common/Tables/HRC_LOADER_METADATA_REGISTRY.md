# HRC_LOADER_METADATA_REGISTRY

This table contains metadata about Fusion data objects used during a data load.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloadermetadataregistry-28783.html#hrcloadermetadataregistry-28783](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcloadermetadataregistry-28783.html#hrcloadermetadataregistry-28783)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_LOADER_METADATA_REG_PK | METADATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| METADATA_ID | NUMBER |  | 18 | Yes | Metadata ID |  |
| OBJECT_NAME | VARCHAR2 | 100 |  | Yes | Object name |  |
| OBJECT_ADR_NAME | VARCHAR2 | 100 |  | Yes | LBO name in ADR |  |
| OBJECT_FULL_NAME | VARCHAR2 | 256 |  | Yes | Fully qualified VO name, representing this Logical Business Object. |  |
| OWNING_APP_NAME | VARCHAR2 | 256 |  | Yes | Fully qualified application module name |  |
| OWNING_APP_CONFIG | VARCHAR2 | 100 |  | Yes | Application module configuration name |  |
| OWNING_APP_ROOT_VO | VARCHAR2 | 100 |  | Yes | Application module VO slot name |  |
| OBJECT_MODE | VARCHAR2 | 100 |  |  | LBO loading mode: ServiceWriter, FusionWriter, etc. |  |
| PROCESSING_ORDER | NUMBER |  | 18 |  | LBO processing order |  |
| HASH_VALUE | VARCHAR2 | 100 |  |  | LBO hash value |  |
| CALLBACK_CLASS_NAME | VARCHAR2 | 2000 |  |  | Callback class name |  |
| ODI_SCENARIO_NAME | VARCHAR2 | 256 |  |  | ODI scenario name |  |
| ODI_SCENARIO_VERSION | VARCHAR2 | 100 |  |  | ODI scenario version |  |
| WS_CONNECTION_QNAME | VARCHAR2 | 256 |  |  | Web service connection name |  |
| WS_QNAME | VARCHAR2 | 256 |  |  | Web service fully qualified name |  |
| WS_PORT_QNAME | VARCHAR2 | 256 |  |  | Web service port fully qualified name |  |
| CALLBACK_CONNECTION_QNAME | VARCHAR2 | 256 |  |  | Callback connection name |  |
| CALLBACK_QNAME | VARCHAR2 | 256 |  |  | Callback service fully qualified name |  |
| CALLBACK_PORT_QNAME | VARCHAR2 | 256 |  |  | Callback service fully qualified port name |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| DISPLAY_ORDER | NUMBER |  | 18 |  | The order in which the spreadsheet loaders will be listed in launch UI. |  |
| SL_OPERATION | VARCHAR2 | 32 |  |  | To identify the default operation supported in spreadsheet loader. |  |
| OBJECT_DESCRIPTION | VARCHAR2 | 2000 |  |  | To describe the object as in FSM launch UI. |  |
| LEGISLATION_CODE | VARCHAR2 | 32 |  |  | To support Legislation specific spreadsheets. |  |
| HR2HR_OBJECT | VARCHAR2 | 1 |  |  | To identify HR2HR objects. |  |
| SPREADSHEET_OBJECT | VARCHAR2 | 1 |  |  | To identify Spreadsheet Loader objects. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_LOADER_META_REGISTRY_N1 | Non Unique | Default | ODI_SCENARIO_NAME, ODI_SCENARIO_VERSION, ENTERPRISE_ID |
| HRC_LOADER_META_REGISTRY_PK | Unique | Default | METADATA_ID |
| HRC_LOADER_META_REGISTRY_U1 | Unique | Default | OBJECT_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
