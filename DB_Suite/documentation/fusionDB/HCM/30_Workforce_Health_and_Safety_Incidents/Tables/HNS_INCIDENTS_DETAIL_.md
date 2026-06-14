# HNS_INCIDENTS_DETAIL_

HNS INCIDENT DETAIL. This table stores the incident event related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentsdetail-25885.html#hnsincidentsdetail-25885](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentsdetail-25885.html#hnsincidentsdetail-25885)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INCIDENTS_DETAIL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, INCIDENT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INCIDENT_DETAIL_ID | NUMBER |  | 18 | Yes | Unique identifier for the Incident detail.Primary key for HNS_INCIDENTS_DETAIL table. | Active |
| INCIDENT_ID | NUMBER |  | 18 |  | Incident identifier. Primary key for Incidents Summary table. | Active |
| INCIDENT_EVENT_CODE | VARCHAR2 | 30 |  |  | Unique Identifier for each Incident Event. Connect to FND_LOOKUP_VALUES_VL to get Incident Events. | Active |
| INCIDENT_EVENT_NO | VARCHAR2 | 32 |  |  | Unique user generated Incident Event Number. | Active |
| INCIDENT_EVENT_OWNER_ID | NUMBER |  | 18 |  | Owner identifier for an Incident Event. Owner is an employee. | Active |
| INC_EVENT_OWNER_ASSIGN_ID | NUMBER |  | 18 |  | Assignment id of the incident event owner | Active |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | Incident event completed flag. This signifies if the incident event is completed. | Active |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the incident event is checked for deletion. | Active |
| INCI_EVENT_STATUS_CODE | VARCHAR2 | 30 |  |  | INCI_EVENT_STATUS_ID column: Current Incident Event Status. Lookup to FND_LOOKUP INCIDENT_STATUS. | Active |
| TARGET_COMPLETION_DATE | TIMESTAMP |  |  |  | Target completion date set for each incident event. | Active |
| ACTUAL_COMPLETION_DATE | TIMESTAMP |  |  |  | Actual Completion date set per incident event. | Active |
| SEVERITY_LEVEL_CODE | VARCHAR2 | 30 |  |  | Severity level set per incident event. | Active |
| INCIDENT_EVENT_SUMMARY | VARCHAR2 | 1000 |  |  | The Summary information entered by the reporter for each incident event. | Active |
| INCI_DETAIL_DESCR | CLOB |  |  |  | Description for each incident event. | Active |
| THIRD_PARTY_DETAILS | CLOB |  |  |  | Details per incident event from the third party. | Active |
| NOTICE_OF_VIOLATION_CD | VARCHAR2 | 30 |  |  | Notice of violation sent per incident event. | Active |
| SPILL_RELEASE_CODE | VARCHAR2 | 30 |  |  | Spill Release Identifier. This column is related to Spill / Release incident event type. | Active |
| SPILLKIT_DEPLOYED_FLAG | VARCHAR2 | 1 |  |  | Spill kit deployed flag. This column is related to spill/release incident event. | Active |
| CLEANUP_TEAM_NOTIFIED | VARCHAR2 | 1 |  |  | Cleanup team notified flag. This column is related to Spill/ Release incident event. | Active |
| AMOUNT_SPILLED | NUMBER |  |  |  | Amount in volume spilled during the incident.. This column is related to Spill/Relase incident event. | Active |
| AMOUNT_SPILLED_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Amount spilled. | Active |
| AMOUNT_RECOVERED | NUMBER |  |  |  | Amount in volume recovred during the event. This column is related to Spill/Release incident event. | Active |
| AMOUNT_RECOVERED_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Amount recovered. | Active |
| PROPERTY_DAMAGE_CODE | VARCHAR2 | 30 |  |  | Property damage type  identifier. Lookup from FND_LOOKUP PROPERTY_DAMAGE. | Active |
| NEAR_MISS_CODE | VARCHAR2 | 30 |  |  | Near miss type identifier.Lookup from FND_LOOKUP NEAR_MISS. | Active |
| UNSAFE_CONDITION_CODE | VARCHAR2 | 30 |  |  | Unsafe condition type identifier.Lookup from FND_LOOKUP UNSAFE CONDITION. | Active |
| ROAD_CONDITION_CODE | VARCHAR2 | 30 |  |  | Road condition type identifier.Lookup from FND_LOOKUP ROAD CONDITION. | Active |
| LIGHT_CONDITION_CODE | VARCHAR2 | 30 |  |  | Light condition type identifier.Lookup from FND_LOOKUP LIGHT_CONDITION. | Active |
| TRAFFIC_CONDITION_CODE | VARCHAR2 | 30 |  |  | Traffic condition type identifier.Lookup from FND_LOOKUP TRAFFIC CONDITION. | Active |
| WEATHER_CONDITION_CODE | VARCHAR2 | 30 |  |  | Weather condition type identifier.Lookup from FND_LOOKUP WEATHER CONDITION. | Active |
| INCIDENT_EVENT_DATE | TIMESTAMP |  |  |  | INCIDENT_EVENT_DATE column : Date incident event was reported. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| VEHICLE_STRUCK_CODE | VARCHAR2 | 30 |  |  | Vehicle Struck code. Lookup from FND_LOOKUP.ORA_HNS_VEHICLE_STRUCK. | Active |
| VEHICLE_COLLISION_TYPE_CODE | VARCHAR2 | 30 |  |  | Vehicle Collision Type code. Lookup from FND_LOOKUP.ORA_HNS_COLLISION_TYPE. | Active |
| VEHICLE_STRUCK_BY_CODE | VARCHAR2 | 30 |  |  | Vehicle Struck by code. Lookup from FND_LOOKUP.ORA_HNS_VEHICLE_STRUCK_BY. | Active |
| VEHICLE_ACC_CATEGORY_CODE | VARCHAR2 | 30 |  |  | Vehicle Accident Category code. Lookup from FND_LOOKUP.ORA_HNS_ACCIDENT_CATEGORY. | Active |
| TRAFFIC_CONTROLS_CODE | VARCHAR2 | 30 |  |  | Traffic Controls code. Lookup from FND_LOOKUP.ORA_HNS_TRAFFIC_CONTROLS. | Active |
| VEHICLE_SPEED_LIMIT | NUMBER |  |  |  | Vehicle Speed Limit. | Active |
| VEHICLE_SPEED_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Vehicle Speed. Lookup from FND_LOOKUP.ORA_HNS_SPEED_UOM. | Active |
| POLICE_REPORT_FLAG | VARCHAR2 | 1 |  |  | This column signifies whether the Police Agency has been notified. | Active |
| POLICE_AGENCY_LOCATION | VARCHAR2 | 1000 |  |  | Police Agency Location. | Active |
| POLICE_BADGE_NUM | VARCHAR2 | 100 |  |  | Police Badge Number. | Active |
| CITATION_NUM | VARCHAR2 | 100 |  |  | Citation Number. | Active |
| UNSAFE_ACT_TYPE_CODE | VARCHAR2 | 30 |  |  | Unsafe Act Type code. Lookup from FND_LOOKUP.ORA_HNS_UNSAFE_ACT_TYPE. | Active |
| ISSUE_TYPE_CODE | VARCHAR2 | 30 |  |  | Issue Type code. Lookup from FND_LOOKUP.ORA_HNS_ISSUE_TYPE. | Active |
| IMPROVEMENT_TYPE_CODE | VARCHAR2 | 30 |  |  | Improvement Type code. Lookup from FND_LOOKUP.ORA_HNS_IMPROVEMENT_TYPE. | Active |
| LESSONS_LEARNED | VARCHAR2 | 4000 |  |  | Lessons Learned. | Active |
| EMPLOYEE_ID | NUMBER |  | 18 |  | Employee ID of the Employee. | Active |
| EMPLOYEE_ASSIGN_ID | NUMBER |  | 18 |  | Assignment ID of the Employee. | Active |
| AIR_QUALITY_TYPE_CODE | VARCHAR2 | 30 |  |  | Air Quality Type code. Lookup from FND_LOOKUP.ORA_HNS_AIR_QUALITY_TYPE. | Active |
| ERGONOMIC_TYPE_CODE | VARCHAR2 | 30 |  |  | Ergonomic Type code. Lookup from FND_LOOKUP.ORA_HNS_ERGONOMIC_TYPE. | Active |
| ERGONOMIC_ASS_REQ_CODE | VARCHAR2 | 1 |  |  | Request an Ergonomic Assessment. Lookup from FND_LOOKUP.YES_NO. | Active |
| RESULT_CODE | VARCHAR2 | 30 |  |  | Result Code Column : Incident Owner check result code. | Active |
| ACTION_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Action Required Flag Column : Check box to confirm whether an action is required. | Active |
| EVENT_CREATION_DATE | TIMESTAMP |  |  |  | The date incident event was created in the system. | Active |
| WHAT_WAS_SPILLED_OR_RELEASED | VARCHAR2 | 1000 |  |  | What was spilled or released. | Active |
| CLEANUP_TEAM_NOTIFIED_AT | TIMESTAMP |  |  |  | At what time Cleanup team or Contractor notified. | Active |
| SPILL_POSSIBLE_CAUSE_CODE | VARCHAR2 | 30 |  |  | Possible cause of the spill or release. Lookup from FND_LOOKUP.ORA_HNS_SPILL_POSSIBLE_CAUSE. | Active |
| SPILL_SOURCE_CODE | VARCHAR2 | 30 |  |  | Spill or release source. Lookup from FND_LOOKUP.ORA_HNS_SPILL_SOURCE. | Active |
| REPLN_SPILL_KIT_FLAG | VARCHAR2 | 1 |  |  | Replenish Spill Kit Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| DATE_DISCLOSED | TIMESTAMP |  |  |  | Date Disclosed Column : Date employee notified the organization about the event. | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HNS_INCIDENTS_DETAILN1_ | Non Unique | Default | INCIDENT_DETAIL_ID, LAST_UPDATE_DATE |  |
| HNS_INCIDENTS_DETAIL_UK1_ | Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE, LAST_UPDATED_BY, INCIDENT_DETAIL_ID | Active |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
