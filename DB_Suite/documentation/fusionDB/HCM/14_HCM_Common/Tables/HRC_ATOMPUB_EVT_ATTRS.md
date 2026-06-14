# HRC_ATOMPUB_EVT_ATTRS

Store atom collection feed/event attributes

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubevtattrs-21042.html#hrcatompubevtattrs-21042](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcatompubevtattrs-21042.html#hrcatompubevtattrs-21042)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ATOMPUB_EVT_ATTRS_PK | EVT_ATTRIBUTE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Uniquely identifies an atom feed attributes row |
| COLLECTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_ATOMPUB_COLLECTIONS.COLLECTION_ID |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_EVT_SOURCE_OBJECTS.SOURCE_OBJECT_ID |
| SOURCE_OBJECT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_EVT_SRC_OBJ_ATTRIBUTES.SOURCE_OBJECT_ATTRIBUTE_ID |
| DELETED_FLAG | VARCHAR2 | 30 |  | Yes | Used to identify for soft delete. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ATOMPUB_EVT_ATTRS_N20 | Non Unique | Default | SGUID |
| HRC_ATOMPUB_EVT_ATTRS_U1 | Unique | Default | EVT_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_EVT_ATTRS_U11 | Unique | Default | EVT_ATTRIBUTE_ID, ORA_SEED_SET2 |
| HRC_ATOMPUB_EVT_ATTRS_U2 | Unique | Default | COLLECTION_ID, SOURCE_OBJECT_ATTRIBUTE_ID, SOURCE_OBJECT_ID, ORA_SEED_SET1 |
| HRC_ATOMPUB_EVT_ATTRS_U21 | Unique | Default | COLLECTION_ID, SOURCE_OBJECT_ATTRIBUTE_ID, SOURCE_OBJECT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
