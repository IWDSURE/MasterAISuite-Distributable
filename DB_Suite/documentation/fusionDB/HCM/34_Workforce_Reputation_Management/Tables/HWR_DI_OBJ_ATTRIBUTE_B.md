# HWR_DI_OBJ_ATTRIBUTE_B

This is the base table for Object Definition names

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjattributeb-14053.html#hwrdiobjattributeb-14053](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjattributeb-14053.html#hwrdiobjattributeb-14053)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_OBJ_ATTRIBUTE_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for the object attribute tables. The number should be generated from the sequence. |  |
| REF_ID | NUMBER |  | 18 | Yes | The referenced object definition ID |  |
| SOURCE_ID | NUMBER |  | 18 | Yes | The source ID. |  |
| ATTRIBUTE_ID | VARCHAR2 | 512 |  | Yes | This is the name id of the Object definition. |  |
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
| HWR_DI_OBJ_ATTRIBUTE_B_U1 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET1 | Active |
| HWR_DI_OBJ_ATTRIBUTE_B_U11 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET2 |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
