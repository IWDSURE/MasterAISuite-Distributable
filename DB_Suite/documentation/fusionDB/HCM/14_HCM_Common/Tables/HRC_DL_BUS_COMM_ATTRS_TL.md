# HRC_DL_BUS_COMM_ATTRS_TL

HRC_DL_BUS_COMM_ATTRS_TL is an MLS table containing translatable labels and description for common attributes that are used by more than one view object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbuscommattrstl-23149.html#hrcdlbuscommattrstl-23149](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbuscommattrstl-23149.html#hrcdlbuscommattrstl-23149)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_COMM_ATTRS_TL_PK | BUS_COMM_ATTR_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BUS_COMM_ATTR_ID | NUMBER |  | 18 | Yes | BUS_COMM_ATTR_ID |
| ATTRIBUTE_LABEL | VARCHAR2 | 250 |  | Yes | ATTRIBUTE_LABEL |
| ATTRIBUTE_DESCRIPTION | VARCHAR2 | 1000 |  | Yes | ATTRIBUTE_DESCRIPTION |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_BUS_COMM_ATTRS_TL_U1 | Unique | Default | BUS_COMM_ATTR_ID, LANGUAGE, ORA_SEED_SET1 |
| HRC_DL_BUS_COMM_ATTRS_TL_U11 | Unique | Default | BUS_COMM_ATTR_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
