# HNS_FIRE_INC_EVENT_DETAIL

HNS_FIRE_INC_EVENT_DETAIL. This table stores fire or explosion incident event related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsfireinceventdetail-16123.html#hnsfireinceventdetail-16123](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsfireinceventdetail-16123.html#hnsfireinceventdetail-16123)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_FIRE_INC_EVENT_DETAIL_PK | FIRE_INC_EVT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| FIRE_INC_EVT_DETAIL_ID | NUMBER |  | 18 | Yes | FIRE_INC_EVT_DETAIL_ID unique identifier. Primary key for HNS_FIRE_INC_EVENT_DETAIL table. |  |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 | Yes | Incident Detail identifier. Foreign key for HNS_INCIDENTS_DETAIL table. |  |
| FIRE_FLAG | VARCHAR2 | 1 |  |  | This column signifies if there was a fire event. Lookup from FND_LOOKUP.YES_NO. |  |
| TYPE_OF_FIRE_CODE | VARCHAR2 | 30 |  |  | Type of Fire. Lookup from FND_LOOKUP.ORA_HNS_TYPE_OF_FIRE. |  |
| FIRE_ORIGIN_CODE | VARCHAR2 | 30 |  |  | Fire Origin. Lookup from FND_LOOKUP.ORA_HNS_FIRE_ORIGIN. |  |
| FIRE_IGNITION_SOURCE_CODE | VARCHAR2 | 30 |  |  | Fire Ignition Source. Lookup from FND_LOOKUP.ORA_HNS_FIRE_IGNIT_SOURCE. |  |
| FIRE_FUEL_OR_ENERGY_CODE | VARCHAR2 | 30 |  |  | Fire Fuel or Energy. Lookup from FND_LOOKUP.ORA_HNS_FIRE_FUEL_OR_ENERGY. |  |
| MATERIAL_FIRST_IGNITED_CODE | VARCHAR2 | 30 |  |  | Material First Ignited. Lookup from FND_LOOKUP.ORA_HNS_FIRE_MAT_FIRST_IGNIT. |  |
| POSSIBLE_CAUSE_OF_FIRE_CODE | VARCHAR2 | 30 |  |  | Possible Cause of Fire. Lookup from FND_LOOKUP.ORA_HNS_FIRE_POSSIBLE_CAUSE. |  |
| EXPLOSION_FLAG | VARCHAR2 | 1 |  |  | This column signifies if there was a explosion event. Lookup from FND_LOOKUP.YES_NO. |  |
| TYPE_OF_EXPLOSION_CODE | VARCHAR2 | 30 |  |  | Type of Explosion. Lookup from FND_LOOKUP.ORA_HNS_TYPE_OF_EXPLOSION. |  |
| EXPLOSION_ORIGIN_CODE | VARCHAR2 | 30 |  |  | Explosion Origin. Lookup from FND_LOOKUP.ORA_HNS_EXPLOSION_ORIGIN. |  |
| EXPLOSION_IGNITION_SOURCE_CODE | VARCHAR2 | 30 |  |  | Explosion Ignition Source. Lookup from FND_LOOKUP.ORA_HNS_EXPLOSION_IGNIT_SOURCE. |  |
| EXPLOSION_FUEL_OR_ENERGY_CODE | VARCHAR2 | 30 |  |  | Explosion Fuel or Energy. Lookup from FND_LOOKUP.ORA_HNS_EXPLOS_FUEL_OR_ENERGY. |  |
| POSSIBLE_CAUSE_OF_EXPLOSION_CD | VARCHAR2 | 30 |  |  | Possible Cause of Explosion. Lookup from FND_LOOKUP.ORA_HNS_EXPLOS_POSSIBLE_CAUSE. |  |
| REPLN_FIRE_FIGHTING_EQUIP_FLAG | VARCHAR2 | 1 |  |  | Replenish Fire Fighting Equipment. |  |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the Fire Or Explosion incident event is checked for deletion. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_FIRE_INC_EVENT_DETAIL_N1 | Non Unique | FUSION_TS_TX_IDX | INCIDENT_DETAIL_ID |
| HNS_FIRE_INC_EVENT_DETAIL_UK1 | Unique | FUSION_TS_TX_IDX | FIRE_INC_EVT_DETAIL_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
