# IRC_SEARCH_SYNONYM_CONFIG

Table used for tracking custom synonym configuration in Fusion Recruiting application.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchsynonymconfig-5891.html#ircsearchsynonymconfig-5891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchsynonymconfig-5891.html#ircsearchsynonymconfig-5891)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCH_SYNONYM_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CONFIG_CODE | VARCHAR2 | 64 |  | Yes | Unique code for the search synonym configuration |
| CONFIG_STATUS | VARCHAR2 | 30 |  |  | Status of this search synonyms configuration.Can be ORA_DRAFT,ORA_ACTIVE,ORA_INACTIVE,ORA_SEED. |
| CONTEXT | VARCHAR2 | 30 |  |  | The context of the index (ex: CE_JOBS_INDEX) for which the synonym configuration is applicable. |
| FILE_VALIDATION_STATUS | VARCHAR2 | 30 |  |  | Indicates the uploaded file validation status like ORA_ERROR, ORA_SUCCESS |
| FILE_VALIDATION_LOG | CLOB |  |  |  | Stores logs related to file validation. |
| SYNONYMS_CONTENT | CLOB |  |  |  | Stores the synonyms definition in json. |
| ACTIVATION_DATE | TIMESTAMP |  |  |  | Indicated the date and time of the first activation of this configuration. |
| ACTIVATION_FAILURE_REASON | VARCHAR2 | 2000 |  |  | Indicates the failure reason if any when Synonym update operations are performed on oracle search. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCH_SYNONYM_CONFIG_PK | Unique | FUSION_TS_SEED | CONFIG_ID, ORA_SEED_SET1 |
| IRC_SEARCH_SYNONYM_CONFIG_PK1 | Unique | FUSION_TS_SEED | CONFIG_ID, ORA_SEED_SET2 |
| IRC_SEARCH_SYNONYM_CONFIG_U1 | Unique | FUSION_TS_SEED | CONFIG_CODE, ORA_SEED_SET1 |
| IRC_SEARCH_SYNONYM_CONFIG_U11 | Unique | FUSION_TS_SEED | CONFIG_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
