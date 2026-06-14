# HWM_DS_API_CLASSES_B

Stores API Class for Dynamic Script

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdsapiclassesb-12319.html#hwmdsapiclassesb-12319](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdsapiclassesb-12319.html#hwmdsapiclassesb-12319)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_DS_API_CLASSES_B_PK | DS_CLASS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DS_CLASS_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLASS_NAME | VARCHAR2 | 80 |  | Yes | PROCESS_INPUT |
| CLASS_PATH | VARCHAR2 | 240 |  | Yes | CLASS_PATH |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
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
| HWM_DS_API_CLASSES_B_U1 | Unique | FUSION_TS_TX_DATA | DS_CLASS_ID, ORA_SEED_SET1 |
| HWM_DS_API_CLASSES_B_U11 | Unique | FUSION_TS_TX_DATA | DS_CLASS_ID, ORA_SEED_SET2 |
| HWM_DS_API_CLASSES_B_U2 | Unique | FUSION_TS_TX_DATA | CLASS_NAME, ORA_SEED_SET1 |
| HWM_DS_API_CLASSES_B_U21 | Unique | FUSION_TS_TX_DATA | CLASS_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
