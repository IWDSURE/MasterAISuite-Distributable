# HNS_INCIDENTS_SUMMARY

HNS INCIDENTS SUMMARY. This tables stores all incident related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentssummary-17882.html#hnsincidentssummary-17882](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentssummary-17882.html#hnsincidentssummary-17882)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INCIDENTS_SUMMARY_PK | INCIDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INCIDENT_ID | NUMBER |  | 18 | Yes | Incidents Summary table primary key. |
| LOCATION_ID | NUMBER |  | 18 |  | Location ID :  Foreign key for Location table. |
| INCIDENT_NO | VARCHAR2 | 32 |  | Yes | User defined unique Incidents Identifier. |
| EMERGENCY_FLAG | VARCHAR2 | 1 |  | Yes | Is Emergency Flag.This column signifies whether the incident has an emergency. |
| CONFIDENTIAL_FLAG | VARCHAR2 | 1 |  | Yes | Is Confidential flag. This column signifies whether the incident is checked confidential. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the incident is checked for deletion. |
| REPORTER_TYPE_CODE | VARCHAR2 | 30 |  |  | EMP/NON EMP lookup. To check whether the witness is an employee or not. |
| REPTR_NONEMP_TYPE_CODE | VARCHAR2 | 30 |  |  | Lookup column for non employee type code. FND_Lookup HNS_NON_EMPLOYEE_TYPE |
| EMPLOYEE_ID | NUMBER |  | 18 |  | Employee ID. From HCM. This column saves the employee id if the reporter is an employee. |
| REPTR_NAME | VARCHAR2 | 200 |  |  | The full name of the person reported the incident. |
| REPTR_AREA_CODE | VARCHAR2 | 30 |  |  | REPTR_AREA_CODE column : Reporter phone area code. |
| REPTR_COUNTRY_CODE_NUM | VARCHAR2 | 30 |  |  | REPTR_COUNTRY_CODE_NUM column: Reporter phone country code number. |
| REPTR_PHONE_NO | VARCHAR2 | 18 |  |  | REPTR_PHONE_NO column : Incident Reporter phone number. |
| REPTR_EMAIL | VARCHAR2 | 250 |  |  | The email id of the person who reported the incident. |
| INCIDENT_DATE | TIMESTAMP |  |  | Yes | The date the incident occured. This column is an user entered column. |
| INCIDENT_CREATE_DATE | TIMESTAMP |  |  |  | The date incident was created in the system. |
| INCIDENT_REPORTED_DATE | TIMESTAMP |  |  |  | This is the date that the incident reporter informed a person in authority eg a supervisor |
| LOCATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Incident location type (Onsite/Offsite). |
| OFFSITE_LOC_TYPE_CODE | VARCHAR2 | 30 |  |  | Offsite Location Type Identifier. |
| REPTR_SPECIFIC_LOCATION | VARCHAR2 | 255 |  | Yes | Incident specific location reported by the reporter. |
| REPTR_ADDR_LINE1 | VARCHAR2 | 255 |  |  | REPTR_ADDR_LINE1 column : Incident  Address Line 1 reported by the reporter. |
| REPTR_ADDR_LINE2 | VARCHAR2 | 255 |  |  | REPTR_ADDR_LINE2 column : Incident  Address Line 2 reported by the reporter. |
| REPTR_CITY | VARCHAR2 | 100 |  |  | REPTR_CITY column : Incident  location city reported by the reporter. |
| REPTR_STATE | VARCHAR2 | 100 |  |  | REPTR_STATE column : Incident state reported by the reporter. |
| REPTR_ZIP_CODE | VARCHAR2 | 100 |  |  | REPTR_ZIP_CODE column : Incident zipcode reported by the reporter. |
| REPTR_COUNTRY | VARCHAR2 | 100 |  |  | REPTR_COUNTRY column : Incident  location country reported by the reporter. |
| INCIDENT_SUMMARY | VARCHAR2 | 1000 |  | Yes | The Summary information entered by the reporter for the incident. |
| INCIDENT_DESCRIPTION | CLOB |  |  |  | INCIDENT_DESCRIPTION column : Description entered by the user for the incident. |
| INCIDENT_IMME_ACT_DESCR | CLOB |  |  |  | Description of the immediate action taken if any. |
| SEVERITY_LEVEL_CODE | VARCHAR2 | 30 |  |  | Severity level for the incident. This column is a drop down selected by the incident reporter. |
| INCIDENT_OWNER_ID | NUMBER |  | 18 |  | INCIDENT_OWNER_ID column : Unique identifier for ther person/employee who owns the incident. |
| INCIDENT_OWNER_ASSIGN_ID | NUMBER |  | 18 |  | INCIDENT_OWNER_ASSIGN_ID column : Assignment Id for ther person/employee who owns the incident. |
| TARGET_COMPLETION_DATE | TIMESTAMP |  |  | Yes | Target completion date set for the incident. |
| COMPLETED_FLAG | VARCHAR2 | 1 |  |  | COMPLETED flag.This signifies if the incident is completed or not. |
| ACTUAL_COMPLETION_DATE | TIMESTAMP |  |  |  | Actual completion date for the incident. |
| INCIDENT_STATUS_CODE | VARCHAR2 | 30 |  | Yes | INCIDENT_STATUS_CODE column: Current Incident Status. Lookup to FND_LOOKUP STATUS. |
| INCIDENT_TYPE_CODE | VARCHAR2 | 30 |  |  | INCIDENT_TYPE_CODE column : Current Incident Type. Lookup to FND_LOOKUP ORA_HNS_INCIDENT_TYPE. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| INCIDENT_APPROVER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to incident approver . |
| INCIDENT_REVIEWER_EMAIL_FLAG | VARCHAR2 | 1 |  |  | The flag  to send email notification to incident reviewer . |
| BIZ_CONT_PLAN_ACTIVATED_AT | TIMESTAMP |  |  |  | At what time the business continuity plan is activated. |
| BIZ_CONT_PLAN_ACTIVATED_FLAG | VARCHAR2 | 1 |  |  | Business continuity plan activated flag. Lookup from FND_LOOKUP.YES_NO. |
| BIZ_CONT_PLAN_ACT_BY_EMPID | NUMBER |  | 18 |  | Employee Id of the person who activated the business continuity plan. |
| EMERG_ACTION_PLAN_ACTIVATED_AT | TIMESTAMP |  |  |  | At what time the Emergency Action Plan is Activated. |
| EMERG_ACTION_PLAN_ACT_BY_EMPID | NUMBER |  | 18 |  | Employee Id of the person who activated the emergency action plan. |
| EMERG_ACTION_PLAN_ACT_FLAG | VARCHAR2 | 1 |  |  | Emergency Action Plan Activated. Lookup from FND_LOOKUP.YES_NO. |
| EVACUATION_FLAG | VARCHAR2 | 1 |  |  | Evacuation Flag. Lookup from FND_LOOKUP.YES_NO. |
| EVACUATION_LENGTH_OF_TIME | VARCHAR2 | 10 |  |  | Length of Time(Hrs) the evacuation is happened for. |
| EVACUATION_ORDERED_AT | TIMESTAMP |  |  |  | At what time the evacuation is ordered. |
| EVACUATION_ORDERED_BY_EMP_ID | NUMBER |  | 18 |  | Employee Id of the person who ordered the evacuation. |
| EVACUATION_TYPE_CODE | VARCHAR2 | 30 |  |  | Evacuation Type. Lookup from FND_LOOKUP.ORA_HNS_EVACUATION_TYPE. |
| FACILITY_CLOSED_AT | TIMESTAMP |  |  |  | At what time the facility is closed. |
| FACILITY_CLOSED_BY_EMP_ID | NUMBER |  | 18 |  | Employee Id of the person who closed the facility. |
| FACILITY_CLOSED_FLAG | VARCHAR2 | 1 |  |  | Facility Closed or Operations Ceased. Lookup from FND_LOOKUP.YES_NO. |
| FACILITY_CLOSED_LENGTH_OF_TIME | VARCHAR2 | 10 |  |  | Length of Time(Hrs) the facility is closed. |
| RADIUS | NUMBER |  |  |  | Distance in terms of radiating circles from the facility where the fire or explosion occurred. |
| RADIUS_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measure for distance. Lookup from FND_LOOKUP.ORA_HNS_RADIUS_UNIT_CD. |
| LESSONS_LEARNED | VARCHAR2 | 4000 |  |  | Lessons Learned. |
| INCIDENT_SOURCE_CODE | VARCHAR2 | 30 |  |  | INCIDENT_SOURCE_CODE column: Source for Incident creation. Lookup to FND_LOOKUP ORA_HNS_INCIDENT_SOURCE. |
| NOTIFIED_PERSON_ID | NUMBER |  | 18 |  | Employee ID of the person who was notified about the incident. Non-Mandatory field. |
| NOTIFIED_PER_ASSIGN_ID | NUMBER |  | 18 |  | Assignment ID of the person who was notified about the incident. Non-Mandatory field. |
| REPORTER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment ID of the reporter (employee) at the time when Incident happened. Non-Mandatory field. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
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
| ACTION_REQUIRED_FLAG | VARCHAR2 | 1 |  |  | Action Required Flag Column : Check box to confirm whether an action is required. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INCIDENTS_SUMMARY_UK1 | Unique | FUSION_TS_TX_DATA | INCIDENT_NO |
| HNS_INCIDENTS_SUMMARY_UK2 | Unique | FUSION_TS_TX_DATA | INCIDENT_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
