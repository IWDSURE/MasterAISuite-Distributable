# HNS_INJURED_PERSON_ABSENCES

HNS INJURED PERSON ABSENCES This table stores lost time and return to work information for an injured person.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersonabsences-3308.html#hnsinjuredpersonabsences-3308](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersonabsences-3308.html#hnsinjuredpersonabsences-3308)

## Primary Key

| Name | Columns |
|------|----------|
| hns_injured_person_absenc_PK | INJURED_PERSON_ABSENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INJURED_PERSON_ABSENCE_ID | NUMBER |  | 18 | Yes | Primary key identifier for table : 
INJURED_PERSON_ABSENCE_ID |  |
| INJURED_PERSON_ID | NUMBER |  | 18 | Yes | Injured person identifier. Foreign key for HNS_INJURED_PERSON_ABSENCES table. |  |
| LOST_TIME_IN_HRS | VARCHAR2 | 10 |  |  | Number of hours lost due to the incident. This is asociated with the inury. | Active |
| LOST_TIME_TYPE_CODE | VARCHAR2 | 100 |  |  | Type of lost time in the incident. This is asociated with the inury. | Active |
| PER_UNABLE_TO_WRK_FLAG | VARCHAR2 | 1 |  |  | Was the person unable to work for at least one full day after the injury or illness. |  |
| DAYS_AWAY_FROM_WRK | NUMBER |  | 18 |  | Number of Days Away from Work. |  |
| DISAB_DAYS_AWY_FRM_WRK_DT | TIMESTAMP |  |  |  | Date that Disability or Days Away from Work Began. |  |
| EMP_RTN_TO_WRK_FLAG | VARCHAR2 | 1 |  |  | Has the employee returned to work Flag. |  |
| RTN_TO_WRK_DATE | TIMESTAMP |  |  |  | Return to Work Date. |  |
| JOB_TRANSFER_FLAG | VARCHAR2 | 1 |  |  | Job Transfer or Restriction Flag Column. Lookup from FND_LOOKUP.YES_NO. | Active |
| RTN_TO_WRK_TYPE_CD | VARCHAR2 | 30 |  |  | Return to Work Type.Lookup from FND_LOOKUP.ORA_HNS_RETURN_TO_WORK. |  |
| XFR_RESTRICTN_DAYS | NUMBER |  | 18 |  | Number of Days on Transfer or Restriction. |  |
| MOD_DUTIES_RESTRICTN_DESCR | VARCHAR2 | 4000 |  |  | Describe Modified Duties or Restrictions. |  |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INJ_PER_ABSCS_U1 | Unique | FUSION_TS_TX_DATA | INJURED_PERSON_ABSENCE_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
