# WLF_PROPERTIES

Table to store name/value pairs for the Learn system configuration

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproperties-9729.html#wlfproperties-9729](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproperties-9729.html#wlfproperties-9729)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROPERTIES_PK | PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROPERTY_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| NAME | VARCHAR2 | 256 |  | Yes | Property name to uniquely identifies the property. |
| VALUE | VARCHAR2 | 4000 |  |  | Property value in string format. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROPERTIES_PK | Unique | Default | PROPERTY_ID, ORA_SEED_SET1 |
| WLF_PROPERTIES_PK1 | Unique | Default | PROPERTY_ID, ORA_SEED_SET2 |
| WLF_PROPERTIES_U1 | Unique | Default | NAME, ORA_SEED_SET1 |
| WLF_PROPERTIES_U2 | Unique | Default | NAME, ORA_SEED_SET2 |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
