# HXT_GEOFENCE_ASSIGNMENTS

Stores geofences assigned to workers using HCM groups.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofenceassignments-4022.html#hxtgeofenceassignments-4022](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtgeofenceassignments-4022.html#hxtgeofenceassignments-4022)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_GEOFENCE_ASSIGNMENTS_PK | GEOFENCE_ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEOFENCE_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Unique Identifier for geofence assignment. |
| GEOFENCE_ID | NUMBER |  | 18 |  | Geofence ID. Reference to hxt_geofences_b.GEOFENCE_ID.. |
| GRP_ID | NUMBER |  | 18 |  | HCM Group ID. Reference to hwm_grps_b.GRP_ID. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_GEOFENCE_ASSIGNMENTS_N1 | Non Unique | Default | GEOFENCE_ID, GRP_ID |
| HXT_GEOFENCE_ASSIGNMENTS_PK | Unique | Default | GEOFENCE_ASSIGNMENT_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
