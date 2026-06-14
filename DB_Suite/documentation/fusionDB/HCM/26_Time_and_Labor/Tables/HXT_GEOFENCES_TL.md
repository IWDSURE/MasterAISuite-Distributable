# HXT_GEOFENCES_TL

The hxt_geofences_tl table is translation table for the hxt_geofences_b table to store transaltable data such geofence name, description.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencestl-23930.html#hxtgeofencestl-23930](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencestl-23930.html#hxtgeofencestl-23930)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_GEOFENCES_TL_PK | GEOFENCE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOFENCE_ID | NUMBER |  | 18 | Yes | Foreign key to hxt_geofences_b.GEOFENCE_ID. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of the geofence. |
| NAME | VARCHAR2 | 256 |  | Yes | Name of the geofence. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_GEOFENCES_TL_PK | Unique | Default | GEOFENCE_ID, LANGUAGE |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
