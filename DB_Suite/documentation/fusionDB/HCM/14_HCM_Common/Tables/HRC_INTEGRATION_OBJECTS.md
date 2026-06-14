# HRC_INTEGRATION_OBJECTS

HRC_INTEGRATION_OBJECTS stores the Object definitions. Stores ObjectName alsong with underlying BaseTableName

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcintegrationobjects-18546.html#hrcintegrationobjects-18546](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcintegrationobjects-18546.html#hrcintegrationobjects-18546)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_INTEGRATION_OBJECTS_PK | OBJECT_NAME, BASE_TABLE_NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_NAME | VARCHAR2 | 256 |  | Yes | OBJECT_NAME |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| BASE_TABLE_NAME | VARCHAR2 | 30 |  | Yes | BASE_TABLE_NAME |
| LOADER_KEY_MAP_VONAME | VARCHAR2 | 300 |  |  | LOADER_KEY_MAP_VONAME |
| SURROGATE_ID_COLUMN_NAME | VARCHAR2 | 256 |  | Yes | SURROGATE_ID_COLUMN_NAME |
| DESCRIPTION_COLUMN_NAME | VARCHAR2 | 256 |  | Yes | DESCRIPTION_COLUMN_NAME |
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
| HRC_INTEGRATION_OBJECTS_N20 | Non Unique | Default | SGUID |
| HRC_INTEGRATION_OBJECTS_U1 | Unique | FUSION_TS_TX_DATA | OBJECT_NAME, BASE_TABLE_NAME, ORA_SEED_SET1 |
| HRC_INTEGRATION_OBJECTS_U11 | Unique | FUSION_TS_TX_DATA | OBJECT_NAME, BASE_TABLE_NAME, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
