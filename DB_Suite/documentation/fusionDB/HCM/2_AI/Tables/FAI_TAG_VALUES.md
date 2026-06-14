# FAI_TAG_VALUES

This table contains the values assigned to the descriptive tags linked to prompt designs.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitagvalues-11688.html#faitagvalues-11688](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitagvalues-11688.html#faitagvalues-11688)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_TAG_VALUES_PK | TAG_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TAG_VALUE_ID | VARCHAR2 | 32 |  | Yes | The system generated surrogate key. |
| TAG_ID | VARCHAR2 | 32 |  | Yes | Foreign key referencing to FAI_TAGS table. |
| TAG_VALUE | VARCHAR2 | 80 |  | Yes | This column contains the value assigned to the descriptive tag linked to prompt designs. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_TAG_VALUES_U1 | Unique | Default | TAG_VALUE_ID, ORA_SEED_SET1 |
| FAI_TAG_VALUES_U11 | Unique | Default | TAG_VALUE_ID, ORA_SEED_SET2 |
| FAI_TAG_VALUES_U2 | Unique | Default | MODULE_ID, TAG_ID, TAG_VALUE, ORA_SEED_SET1 |
| FAI_TAG_VALUES_U21 | Unique | Default | MODULE_ID, TAG_ID, TAG_VALUE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
