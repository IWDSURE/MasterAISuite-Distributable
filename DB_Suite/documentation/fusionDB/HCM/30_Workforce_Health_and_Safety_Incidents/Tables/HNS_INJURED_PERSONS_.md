# HNS_INJURED_PERSONS_

HNS INJURED PERSONS. This table stores injured person related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersons-11828.html#hnsinjuredpersons-11828](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersons-11828.html#hnsinjuredpersons-11828)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INJURED_PERSONS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, INJURED_PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INJURED_PERSON_ID | NUMBER |  | 18 | Yes | INJURED_PERSON_ID unique identifier. Primary key for HNS_INJURED_PERSON table. | Active |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 |  | Incident Detail identifier. Foreign key for HNS_INCIDENTS_DETAIL table. |  |
| INJ_PERSON_SUMMARY_ID | NUMBER |  | 18 |  | Foreign key for hns_injured_persons_summary table. | Active |
| INCI_INJ_PERSON_ID | NUMBER |  | 18 |  | Employee ID of the injured person . The column will be blank if the injured person is not an employee. | Active |
| INCI_INJ_PERSON_ASSIGN_ID | NUMBER |  | 18 |  | Assignment ID of the injured person . The column will be blank if the injured person is not an employee. | Active |
| INJURED_NAME | VARCHAR2 | 200 |  |  | The name of the person (employee/non employee) who got injured. | Active |
| INJURED_EMAIL | VARCHAR2 | 250 |  |  | The email ID of the person (employee/ non employee) injured. | Active |
| INJURED_COUNTRY_CODE_NUM | VARCHAR2 | 30 |  |  | INJURED_COUNTRY_CODE_NUM column : Injured Person phone country code number. | Active |
| INJURED_AREA_CODE | VARCHAR2 | 30 |  |  | INJURED_AREA_CODE column : Injured Person phone area code. | Active |
| INJURED_PHONENO | VARCHAR2 | 18 |  |  | The phone number of the person (employee/ non employee) injured. | Active |
| INJ_PERSON_TYPE_CODE | VARCHAR2 | 30 |  |  | Injured person type. Lookup from FND_LOOKUP EMP/NON EMP lookup. | Active |
| ILLNESS_NATURE_CODE | VARCHAR2 | 1000 |  |  | Injured Person Illness nature Code. This column is optional and populated if the nature is illness. | Active |
| CLASSIFICATION_CODE | VARCHAR2 | 30 |  |  | Type of injury (injury/ illness/fatality). Lookup FND_LOOKUP CLASSIFICATION_ID | Active |
| INJ_PER_NONEMP_TYPE_CD | VARCHAR2 | 30 |  |  | Lookup column for non employee type code. FND_Lookup HNS_NON_EMPLOYEE_TYPE | Active |
| REPORTABLE_FLAG | VARCHAR2 | 1 |  |  | REPORTABLE flag. This column signifies whether the injury is reportable. | Active |
| WORKRELATED_FLAG | VARCHAR2 | 1 |  |  | WORK RELATED flag. Is the injury work related. | Active |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. | Active |
| TIME_STARTED_WORK | TIMESTAMP |  |  |  | Time when the injured person started the work. | Active |
| LOSTTIME_FLAG | VARCHAR2 | 1 |  |  | lost time flag. Signifies whether there was a lost of time due to injury. | Active |
| LOST_TIME_IN_HRS | VARCHAR2 | 10 |  |  | Number of hours lost due to the incident. This is asociated with the inury. | Active |
| RECURRING_FLAG | VARCHAR2 | 1 |  |  | Recurring flag.This column signifies whetherthe injury/incident is  recurring. | Active |
| TREATMENT_FLAG | VARCHAR2 | 1 |  |  | Treatment flag.This column signifies whether there was a treatment. | Active |
| TREATMENT_TYPE_CODE | VARCHAR2 | 1000 |  |  | Treatment Type identifier. Lookup FND_LOOKUP TREATMENT_TYPE. | Active |
| FATALITY_DATE | TIMESTAMP |  |  |  | The date the fatality occured if any. This column is related to injury/illness incident. | Active |
| MED_PROF_NAME | VARCHAR2 | 200 |  |  | Medical profession name incase there was a treatment. | Active |
| FACILITY_ADDRESS_LINE1 | VARCHAR2 | 255 |  |  | Facility address Line1 of the medical professional. | Active |
| FACILITY_ADDRESS_LINE2 | VARCHAR2 | 255 |  |  | Facility address Line2 of the medical professional. | Active |
| FACILITY_CITY | VARCHAR2 | 100 |  |  | Facility city of the medical professional. | Active |
| FACILITY_COUNTRY | VARCHAR2 | 100 |  |  | Facility country of the medical professional. | Active |
| FACILITY_STATE | VARCHAR2 | 100 |  |  | Facility state of the medical professional. | Active |
| FACILITY_ZIP_CODE | NUMBER |  |  |  | Facility zipcode of the medical professional. | Active |
| PERSON_ACTIVITY_DESCR | CLOB |  |  |  | Description of the activity for the injuried person. | Active |
| PER_INFORMED_INJ_ILL_DATE | TIMESTAMP |  |  |  | Date and Time Person was Informed about the Injury, Illness or Fatality. |  |
| INJ_ILL_INFRMD_BY_PER_NAME | NUMBER |  | 18 |  | Name of the Person Informed about the Injury, Illness or Fatality. |  |
| INJ_ILL_OCCURED_DATE | TIMESTAMP |  |  |  | Date and Time Injury, Illness or Fatality Occurred. |  |
| TIME_FINISHED_WORK | TIMESTAMP |  |  |  | Date and Time Finished Work. |  |
| HRS_AT_WRK_BEFORE_INJ_ILL | NUMBER |  | 18 |  | Number of Hours at Work Before Injury, Illness or Fatality Occurred. |  |
| REGULATOR_NOTIFIED_FLAG | VARCHAR2 | 20 |  |  | Regulator Notified Flag. |  |
| REGULATOR_NOTIFIED_DATE | TIMESTAMP |  |  |  | Date and Time Regulator Notified. |  |
| REGULATOR_NOTIFIED_BY | NUMBER |  | 18 |  | Regulator Notified by Whom. |  |
| REGULATR_NOTIFIED_MEDIUM_CD | VARCHAR2 | 1000 |  |  | How was the regulator notified.Lookup from FND_LOOKUP.ORA_HNS_HOW_NOTIFIED. |  |
| RECORDABLE_TYPE_CD | VARCHAR2 | 2000 |  |  | Recordable Type.Lookup from FND_LOOKUP.ORA_HNS_RECORDABLE_TYPE. |  |
| DESCRIPTION_OF_TREATMENT | VARCHAR2 | 4000 |  |  | Description of Treatment. |  |
| FACILITY_NAME | VARCHAR2 | 255 |  |  | Facility Name. |  |
| PREV_INJ_ILL_DATE | TIMESTAMP |  |  |  | Date of Previous Injury or Illness. |  |
| INJ_ILL_DEV_OVER_TIME_FLAG | VARCHAR2 | 1 |  |  | Did the injury or illness develop over time. |  |
| SYM_FIRST_NOTICED_DATE | TIMESTAMP |  |  |  | Date Symptoms First Noticed. |  |
| PER_UNABLE_TO_WRK_FLAG | VARCHAR2 | 1 |  |  | Was the person unable to work for at least one full day after the injury or illness. |  |
| DAYS_AWAY_FROM_WRK | NUMBER |  | 18 |  | Number of Days Away from Work. |  |
| DISAB_DAYS_AWY_FRM_WRK_DT | TIMESTAMP |  |  |  | Date that Disability or Days Away from Work Began. |  |
| EMP_RTN_TO_WRK_FLAG | VARCHAR2 | 1 |  |  | Has the employee returned to work Flag. |  |
| RTN_TO_WRK_DATE | TIMESTAMP |  |  |  | Return to Work Date. |  |
| RTN_TO_WRK_TYPE_CD | VARCHAR2 | 30 |  |  | Return to Work Type.Lookup from FND_LOOKUP.ORA_HNS_RETURN_TO_WORK. |  |
| XFR_RESTRICTN_DAYS | NUMBER |  | 18 |  | Number of Days on Transfer or Restriction. |  |
| MOD_DUTIES_RESTRICTN_DESCR | VARCHAR2 | 4000 |  |  | Describe Modified Duties or Restrictions. |  |
| SOURCE_OF_INJURY_LVL2_CODE | VARCHAR2 | 30 |  |  | Source of Injury Level 2. Used to declare the level 2 sources for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_SOURCE_II. |  |
| SOURCE_OF_INJURY_LVL3_CODE | VARCHAR2 | 30 |  |  | Source of Injury Level 3. Used to declare the level 3 sources for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_SOURCE_LEVEL_III. |  |
| SOURCE_OF_INJURY_LVL4_CODE | VARCHAR2 | 30 |  |  | Source of Injury Level 4. Used to declare the level 4 sources for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_SOURCE_LEVEL_IV. |  |
| INJURY_MECHANISM_LVL2_CODE | VARCHAR2 | 30 |  |  | Mechanism of Injury Level 2. Used to declare the level 2 mechanisms for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_MECHANISM_II. |  |
| INJURY_MECHANISM_LVL3_CODE | VARCHAR2 | 30 |  |  | Mechanism of Injury Level 3. Used to declare the level 3 mechanisms for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_MECHANISM_III. |  |
| INJURY_MECHANISM_LVL4_CODE | VARCHAR2 | 30 |  |  | Mechanism of Injury Level 4. Used to declare the level 4 mechanisms for injury or illness analysis. Lookup from FND_LOOKUP.ORA_HNS_MECHANISM_IV. |  |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| RECORDABLE_FLAG | VARCHAR2 | 1 |  |  | Recordable Flag Column. Lookup from FND_LOOKUP.YES_NO. | Active |
| JOB_TRANSFER_FLAG | VARCHAR2 | 1 |  |  | Job Transfer or Restriction Flag Column. Lookup from FND_LOOKUP.YES_NO. | Active |
| INJURY_MECHANISM_CODE | VARCHAR2 | 30 |  |  | Mechanism of Injury Column. Lookup from FND_LOOKUP.ORA_HNS_MECHANISM. | Active |
| SOURCE_OF_INJURY_CODE | VARCHAR2 | 30 |  |  | Source of Injury Column. Lookup from FND_LOOKUP.ORA_HNS_SOURCE. | Active |
| CASE_NUMBER | VARCHAR2 | 256 |  |  | Unique system generated sequential case number of injured or ill person record. |  |
| TX_FACILITY_ZIP_CODE | VARCHAR2 | 100 |  |  | Treatment Facility zipcode of the medical professional. |  |
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
| HNS_INJURED_PERSONSN1_ | Non Unique | Default | INJURED_PERSON_ID, LAST_UPDATE_DATE |  |
| HNS_INJURED_PERSONS_UK1_ | Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE, LAST_UPDATED_BY, INJURED_PERSON_ID | Active |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
