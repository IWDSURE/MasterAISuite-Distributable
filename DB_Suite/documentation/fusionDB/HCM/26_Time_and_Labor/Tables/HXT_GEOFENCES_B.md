# HXT_GEOFENCES_B

The hxt_geofence_b table stores the geofence information such as geofence code, location, geoJSON for geofence. Geofence is used to enforce the punch in and punch out while capturing the time for the workers.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencesb-16490.html#hxtgeofencesb-16490](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofencesb-16490.html#hxtgeofencesb-16490)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_GEOFENCES_B_PK | GEOFENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOFENCE_ID | NUMBER |  | 18 | Yes | Unique identifier for the geofence. |
| CODE | VARCHAR2 | 256 |  | Yes | Code of the geofence. |
| LOCATION_ID | NUMBER |  | 18 |  | Location of the geofence. |
| GEOMETRY | UDT |  |  |  | Specifies coordinates of the geofence. |
| REF_LATITUDE | NUMBER |  | 6 |  | Latitude of geofence coordinate. |
| REF_LONGITUDE | NUMBER |  | 7 |  | Longitude of geofence coordinate. |
| SOURCE | VARCHAR2 | 32 |  |  | Source of geofence. SYSTEM/USER. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RADIUS | NUMBER |  | 9 |  | Radius of the geofence. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_GEOFENCES_B_N1 | Non Unique | Default | REF_LATITUDE, REF_LONGITUDE |
| HXT_GEOFENCES_B_PK | Unique | Default | GEOFENCE_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
