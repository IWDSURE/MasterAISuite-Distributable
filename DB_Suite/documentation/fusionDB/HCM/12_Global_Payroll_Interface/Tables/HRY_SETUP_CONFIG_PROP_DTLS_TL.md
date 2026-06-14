# HRY_SETUP_CONFIG_PROP_DTLS_TL

It is corresponding tl table for hry_setup_config_prop_details

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtlstl-29677.html#hrysetupconfigpropdtlstl-29677](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrysetupconfigpropdtlstl-29677.html#hrysetupconfigpropdtlstl-29677)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_SETUP_CNFG_PROP_DTL_TL_PK | PROPERTY_DETAIL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROPERTY_DETAIL_ID | NUMBER |  | 18 | Yes | Primary key to the table hry_setup_config_prop_dtls |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| PROPERTY_DETAILS_NAME | VARCHAR2 | 256 |  | Yes | It represents name of the detailed property |
| PROPERTY_DETAILS_DESC | VARCHAR2 | 256 |  |  | Description of the detailed property |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_SETUP_CNFG_PROP_DTL_TL_PK1 | Unique | Default | PROPERTY_DETAIL_ID, LANGUAGE, ORA_SEED_SET1 |
| HRY_SETUP_CNFG_PRO_DTL_TL_PK11 | Unique | Default | PROPERTY_DETAIL_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
