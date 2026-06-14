# HWR_LOOKUP_TYPE_B

The lookup type table is used to store the types that lookup items are grouped by.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookuptypeb-20064.html#hwrlookuptypeb-20064](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrlookuptypeb-20064.html#hwrlookuptypeb-20064)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_LOOKUP_TYPE_B_PK | LOOKUP_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LOOKUP_TYPE_ID | NUMBER |  | 18 | Yes | This is the primary key for the lookup tables. The number should be generated from the sequence. | Active |
| LOOKUP_TYPE_CODE | VARCHAR2 | 120 |  | Yes | This is the alpha code identifying the lookup type. | Active |
| IS_SEEDED_DATA | VARCHAR2 | 4 |  |  | A flag indicating seeded data. Use Y for seeded data or N for customer data | Active |
| DISPLAY_TEXT | VARCHAR2 | 1000 |  | Yes | The display value for the lookup type. | Active |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | A description that allows space for more details than the display text. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_LOOKUP_TYPE_B_U1 | Unique | FUSION_TS_TX_DATA | LOOKUP_TYPE_ID, ORA_SEED_SET1 | Active |
| HWR_LOOKUP_TYPE_B_U11 | Unique | FUSION_TS_TX_DATA | LOOKUP_TYPE_ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
