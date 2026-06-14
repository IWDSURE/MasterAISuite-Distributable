# HWR_CFG_CONFIGURATION_B

The configuration table stores information about configuration properties for applications used in HWR project.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcfgconfigurationb-19668.html#hwrcfgconfigurationb-19668](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcfgconfigurationb-19668.html#hwrcfgconfigurationb-19668)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CFG_CONFIGURATION_B_PK | KEY |

## Columns

| Name | Datatype | Length | Not-null | Comments |
|---|---|---|---|---|
| KEY | VARCHAR2 | 255 | Yes | This is the primary key for this table. It identifies the key to associate the properties to |
| VALUE | VARCHAR2 | 4000 |  | This represents the configuration property values |
| DESCRIPTION | VARCHAR2 | 1024 |  | This describes the key for which the configuration properties are created. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CFG_CONFIGURATION_B_U1 | Unique | FUSION_TS_SEED | KEY, ORA_SEED_SET1 |
| HWR_CFG_CONFIGURATION_B_U11 | Unique | FUSION_TS_SEED | KEY, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
