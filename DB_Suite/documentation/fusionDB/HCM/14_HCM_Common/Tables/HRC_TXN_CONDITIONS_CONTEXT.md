# HRC_TXN_CONDITIONS_CONTEXT

This table contains information to identify a particular usage of Condition Builder. When product teams uptake Condition Builder feature, they create entries in this table to denote that they have up-taken Condition Builder and have metadata associated with that particular uptake. This table has two main columns, CONDITIONS_CONTEXT_MODULE and CONTEXT_PROCESS_NAME which identifies the usage of the Condition Builder component. CONDITIONS_CONTEXT_MODULE contains information about the UI (like Approvals UI) and CONDITIONS_PROCESS_NAME further contains a sub-process in that UI, if applicable, which provides more information about where the Condition Builder is used. As an eg, for Approvals UI, CONDITIONS_CONTEXT_MODULE would contain the code for Approvals UI and the CONDITIONS_PROCESS_NAME would contain the Human task name. These two fields together would provide the exact context information to the Condition Builder Task Flow.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionscontext-22165.html#hrctxnconditionscontext-22165](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionscontext-22165.html#hrctxnconditionscontext-22165)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_CON_CONTEX_PK | CONDITIONS_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONDITIONS_CONTEXT_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier required by Seed data framework. |
| CONDITIONS_CONTEXT_MODULE | VARCHAR2 | 30 |  | Yes | CONDITIONS_CONTEXT_MODULE: Denotes the UI context in which condition builder is being used. This is not based on any other referential data but entries into this column are tightly controlled though seed data. Product teams who wish to uptake Condition Builder feature use this column to populate the string that identifies the context of their UI. For eg. For Approvals UI it would be APP_UI. The uptaking team needs to pass this information to Condition Builder TF, so that it can retrieve metadata relevant to that UI. |
| CONTEXT_PROCESS_NAME | VARCHAR2 | 80 |  | Yes | CONTEXT_PROCESS_NAME: Denotes the UI process in which condition builder is being used. This is not based on any other referential data but entries into this column are tightly controlled though seed data. Product teams who wish to uptake Condition Builder feature use this column to populate the string that identifies a process in context of their UI. For eg. For Approvals UI it would be the Human task name that can be edited in the UI, like TransfersApprovalTask. The uptaking team needs to pass this information to Condition Builder TF, so that it can retrieve metadata relevant to that UI. This field applies only to those uptaking teams who have multiple sub-processes under their UI, like Approvals UI. In case of teams with no sub-process, this can be populated with the same data of CONDITIONS_CONTEXT_MODULE. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the composite belongs.Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_CONDITIONS_CONTEXT_PK | Unique | Default | CONDITIONS_CONTEXT_ID, ORA_SEED_SET1 |
| HRC_TXN_CONDITIONS_CONTEXT_PK1 | Unique | Default | CONDITIONS_CONTEXT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
