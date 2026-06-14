# HRC_TXN_CONDITIONS_LOVUSAGE

HRC_TXN_CONDITIONS_LOVUSAGE is a mapping table which maps a participar attribute, identified by the CONDITION_OPERAND column of this table, to its metadata information, identified by the reference to the HRC_TXN_CONDITIONS_LOVMETADATA table, in a particual UI context, which is identified by a reference to HRC_TXN_CONDITIONS_CONTEXT. So essentially the Condition Builder component can generate an LOV query from the metadata table(referred through LOV_METADATA_ID) for an attribute that is present in a particular context (referred through CONDITIONS_CONTEXT_ID).

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionslovusage-16497.html#hrctxnconditionslovusage-16497](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconditionslovusage-16497.html#hrctxnconditionslovusage-16497)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_CON_LOVUSAGE_PK | LOV_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOV_USAGE_ID | NUMBER |  | 18 | Yes | Primary key and unique identifier required by the Seed data framework. |
| CONDITIONS_CONTEXT_ID | NUMBER |  | 18 | Yes | Column referencing the PK column of HRC_TXN_CONDITIONS_CONTEXT. This reference provides the context details of where the attribute identified by CONDITION_OPERAND is going to be present. |
| LOV_METADATA_ID | NUMBER |  | 18 | Yes | References the HRC_TXN_CONDITIONS_LOVMETADATA table. This column provides the metadata information from where the query is to be extracted for the attribute contained in CONDITION_OPERAND column. |
| CONDITION_OPERAND | VARCHAR2 | 240 |  | Yes | Unique identifier of the attribute, which is used as an operand during the condition building and for which the LOV is to be enabled. Details from other columns are used to generate the LOV query. The column is large enough to accomodate the complete package path name or fact path name of the identifier. Typicaly attributes in Approvals UI can go beyond 100 characters. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the composite belongs.Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| HRC_TXN_CONDITIONS_LOVUSAGE_PK | Unique | Default | LOV_USAGE_ID, ORA_SEED_SET1 |
| HRC_TXN_CONDITIONS_LOVUSAG_PK1 | Unique | Default | LOV_USAGE_ID, ORA_SEED_SET2 |
| HRC_TXN_CONDITIONS_LOVUSA_N20 | Non Unique | Default | SGUID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
