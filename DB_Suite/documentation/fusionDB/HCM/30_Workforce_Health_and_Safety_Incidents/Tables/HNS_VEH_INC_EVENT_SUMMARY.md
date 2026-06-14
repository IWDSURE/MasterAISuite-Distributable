# HNS_VEH_INC_EVENT_SUMMARY

HNS_VEH_INC_EVENT_SUMMARY. This table stores vehicle incident event related summary data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventsummary-30929.html#hnsvehinceventsummary-30929](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventsummary-30929.html#hnsvehinceventsummary-30929)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_VEH_INC_EVENT_SUMMARY_PK | VEH_INC_EVT_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VEH_INC_EVT_SUMMARY_ID | NUMBER |  | 18 | Yes | VEH_INC_EVT_SUMMARY_ID unique identifier. Primary key for HNS_VEH_INC_EVENT_SUMMARY table. |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 | Yes | Incident Detail identifier. Foreign key for HNS_INCIDENTS_DETAIL table. |
| VEHICLE_STRUCK_CODE | VARCHAR2 | 30 |  |  | Vehicle Struck code. Lookup from FND_LOOKUP.ORA_HNS_VEHICLE_STRUCK. |
| VEHICLE_COLLISION_TYPE_CODE | VARCHAR2 | 30 |  |  | Vehicle Collision Type code. Lookup from FND_LOOKUP.ORA_HNS_COLLISION_TYPE. |
| VEHICLE_STRUCK_BY_CODE | VARCHAR2 | 30 |  |  | Vehicle Struck by code. Lookup from FND_LOOKUP.ORA_HNS_VEHICLE_STRUCK_BY. |
| VEHICLE_ACC_CATEGORY_CODE | VARCHAR2 | 30 |  |  | Vehicle Accident Category code. Lookup from FND_LOOKUP.ORA_HNS_ACCIDENT_CATEGORY. |
| TRAFFIC_CONTROLS_CODE | VARCHAR2 | 30 |  |  | Traffic Controls code. Lookup from FND_LOOKUP.ORA_HNS_TRAFFIC_CONTROLS. |
| VEHICLE_SPEED_LIMIT | NUMBER |  |  |  | Vehicle Speed Limit. |
| VEHICLE_SPEED_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Vehicle Speed. Lookup from FND_LOOKUP.ORA_HNS_SPEED_UOM. |
| POLICE_REPORT_FLAG | VARCHAR2 | 1 |  |  | This column signifies whether the Police Agency has been notified. |
| POLICE_AGENCY_LOCATION | VARCHAR2 | 1000 |  |  | Police Agency Location. |
| POLICE_BADGE_NUM | VARCHAR2 | 100 |  |  | Police Badge Number. |
| CITATION_NUM | VARCHAR2 | 100 |  |  | Citation Number. |
| ROAD_CONDITION_CODE | VARCHAR2 | 30 |  |  | Road condition type identifier.Lookup from FND_LOOKUP ROAD CONDITION. |
| LIGHT_CONDITION_CODE | VARCHAR2 | 30 |  |  | Light condition type identifier.Lookup from FND_LOOKUP LIGHT_CONDITION. |
| TRAFFIC_CONDITION_CODE | VARCHAR2 | 30 |  |  | Traffic condition type identifier.Lookup from FND_LOOKUP TRAFFIC CONDITION. |
| WEATHER_CONDITION_CODE | VARCHAR2 | 30 |  |  | Weather condition type identifier.Lookup from FND_LOOKUP WEATHER CONDITION. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the Vehicle incident event is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_VEH_INC_EVENT_SUMMARY_N1 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_DETAIL_ID |
| HNS_VEH_INC_EVENT_SUMMARY_UK1 | Unique | Default | VEH_INC_EVT_SUMMARY_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
