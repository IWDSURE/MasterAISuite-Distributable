# HNS_VEH_INC_EVENT_PASSENGERS

HNS VEHICLE INCIDENT EVENT PASSENGERS. This table stores Passenger information related to an vehicle incident event.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventpassengers-5487.html#hnsvehinceventpassengers-5487](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventpassengers-5487.html#hnsvehinceventpassengers-5487)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_VEH_INC_EVT_PAX_PK | PASSENGER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PASSENGER_ID | NUMBER |  | 18 | Yes | Unique Passenger Identifier.Primary key for HNS_VEH_INC_EVENT_PASSENGERS table. |
| VEH_INC_EVT_DETAIL_ID | NUMBER |  | 18 | Yes | Vehicle Incident Event Detail identifier. Foreign key for HNS_VEH_INC_EVENT_DETAIL table. |
| EMPLOYEE_ID | NUMBER |  |  |  | EMPLOYEE_ID column  : Employee ID. If Passenger is an employee. |
| EMPLOYEE_ASSIGN_ID | NUMBER |  | 18 |  | ASSIGNMENT_ID column  : Assignment ID. If Passenger is an employee. |
| PASSENGER_PER_TYPE_CODE | VARCHAR2 | 30 |  |  | FND_LOOKUP.ORA_HNS_PERSON lookup. To check whether the Passenger is an employee or not. |
| PASSENGER_NAME | VARCHAR2 | 200 |  |  | Passenger Name (for Non Employee). |
| PASSENGER_EMAIL | VARCHAR2 | 250 |  |  | Email id of non employee. |
| PASSENGER_COUNTRY_CODE_NUM | VARCHAR2 | 30 |  |  | PASSENGER_COUNTRY_CODE_NUM : Passenger phone country code number. |
| PASSENGER_AREA_CODE | VARCHAR2 | 30 |  |  | PASSENGER_AREA_CODE column : Passenger phone area code number. |
| PASSENGER_PHONE_NUM | VARCHAR2 | 18 |  |  | Passenger phone number. This is for non employee only. |
| PASSENGER_ADDR_LINE1 | VARCHAR2 | 255 |  |  | Address Line1 of the Passenger (non employee). |
| PASSENGER_ADDR_LINE2 | VARCHAR2 | 255 |  |  | Address Line2 of the Passenger (non employee). |
| PASSENGER_ADDR_CITY | VARCHAR2 | 100 |  |  | Address city of the Passenger (non employee). |
| PASSENGER_ADDR_STATE | VARCHAR2 | 100 |  |  | Address State of the Passenger (non employee). |
| PASSENGER_ZIP_CODE | VARCHAR2 | 100 |  |  | Address Zip code of the Passenger (non employee). |
| PASSENGER_COUNTRY | VARCHAR2 | 100 |  |  | Address Country of the Passenger (non employee). |
| PASSENGER_INJURED_FLAG | VARCHAR2 | 1 |  |  | PASSENGER_INJURED_FLAG column : Was passenger Injured Flag. Lookup from FND_LOOKUP.YES_NO. |
| WEARING_SEAT_BELT_FLAG | VARCHAR2 | 1 |  |  | Seat Belt in Use by passenger Flag. Lookup from FND_LOOKUP.YES_NO. |
| TAKEN_TO_HOSPITAL_FLAG | VARCHAR2 | 1 |  |  | TAKEN_TO_HOSPITAL_FLAG column : Taken to Hospital Flag. Lookup from FND_LOOKUP.YES_NO. |
| PASSENGER_FATALITY_FLAG | VARCHAR2 | 1 |  |  | PASSENGER_FATALITY_FLAG column : Fatality Flag. Lookup from FND_LOOKUP.YES_NO. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the Vehicle Passenger is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| POSITION_OF_PASSENGER_CODE | VARCHAR2 | 30 |  |  | Position code of passenger at Time of Accident. Lookup from ORA_HNS_PASSENGER_POSITION |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_VEH_INC_EVT_PAX_N1 | Non Unique | FUSION_TS_TX_IDX | VEH_INC_EVT_DETAIL_ID |
| HNS_VEH_INC_EVT_PAX_UK1 | Unique | FUSION_TS_TX_IDX | PASSENGER_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
