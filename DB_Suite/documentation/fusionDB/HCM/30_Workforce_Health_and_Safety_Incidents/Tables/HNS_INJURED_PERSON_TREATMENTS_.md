# HNS_INJURED_PERSON_TREATMENTS_

HNS INJURED PERSON TREATMENTS. This table stores treatments information for an injured person.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersontreatments-12674.html#hnsinjuredpersontreatments-12674](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsinjuredpersontreatments-12674.html#hnsinjuredpersontreatments-12674)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INJURED_PERSON_TREATM_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, INJURED_PERSON_TREATMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INJURED_PERSON_TREATMENT_ID | NUMBER |  | 18 | Yes | Primary key identifier for table : INJURED_PERSON_TREATMENT_ID |  |
| INJURED_PERSON_ID | NUMBER |  | 18 |  | Injured person identifier. Foreign key for HNS_INJURED_PERSON_TREATMENTS table. |  |
| TREATMENT_TYPE_CODE | VARCHAR2 | 1000 |  |  | Injured person treatment identifer. Lookup key for  FND_LOOKUP HNS_TREATMENT_TYPE. |  |
| MED_PROF_NAME | VARCHAR2 | 200 |  |  | Name of the physician or medical professional treating the injury |  |
| FATALITY_DATE | TIMESTAMP |  |  |  | Date on which the fatality/injury occurred |  |
| DESCRIPTION_OF_TREATMENT | VARCHAR2 | 4000 |  |  | Description of the treatment of the injury |  |
| FACILITY_NAME | VARCHAR2 | 255 |  |  | Name of the facility where injury is treated |  |
| FACILITY_ADDRESS_LINE1 | VARCHAR2 | 255 |  |  | Address line 1 of the facility where injury is treated |  |
| FACILITY_ADDRESS_LINE2 | VARCHAR2 | 255 |  |  | Address line 2 of the facility where injury is treated |  |
| FACILITY_CITY | VARCHAR2 | 100 |  |  | City of the facility where injury is treated |  |
| FACILITY_STATE | VARCHAR2 | 100 |  |  | State of the facility where injury is treated |  |
| FACILITY_COUNTRY | VARCHAR2 | 100 |  |  | Country of the facility where injury is treated |  |
| FACILITY_ZIP_CODE | VARCHAR2 | 100 |  |  | Zip Code of the facility where injury is treated |  |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Flag to check whether is record is deleted. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INJURED_PERSON_TRTMNT_UK1 | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, INJURED_PERSON_TREATMENT_ID |
| HNS_INJ_PER_TRTMNTN1_ | Non Unique | FUSION_TS_TX_DATA | INJURED_PERSON_TREATMENT_ID, LAST_UPDATE_DATE |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
