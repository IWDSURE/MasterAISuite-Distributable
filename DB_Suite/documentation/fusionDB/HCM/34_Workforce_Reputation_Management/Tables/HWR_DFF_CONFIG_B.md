# HWR_DFF_CONFIG_B

This table is for Descriptive flex field configuration

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdffconfigb-19797.html#hwrdffconfigb-19797](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdffconfigb-19797.html#hwrdffconfigb-19797)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DFF_CONFIG_B_PK | DFF_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DFF_CONFIG_ID | NUMBER |  | 18 | Yes | This is the Dff Config Id identifying the Dff Config entry in this table. |
| DFF_CONFIG | CLOB |  |  | Yes | The is the descriptive flex field configuration. should be an xml. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DFF_CONFIG_B_U1 | Unique | Default | DFF_CONFIG_ID, ORA_SEED_SET1 |
| HWR_DFF_CONFIG_B_U11 | Unique | Default | DFF_CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
