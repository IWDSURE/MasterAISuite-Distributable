# HNS_INCIDENT_WITNESSES

HNS INCIDENT WITNESSES. This table stores witness information related to an incident event.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentwitnesses-21193.html#hnsincidentwitnesses-21193](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentwitnesses-21193.html#hnsincidentwitnesses-21193)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INCIDENT_WITNESSES_PK | WITNESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WITNESS_ID | NUMBER |  | 18 | Yes | Unique Witness Identifier.Primary key for HNS_INCIDENT_WITNESSES table. |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 | Yes | Incident Detail identifier. Foreign key for HNS_INCIDENTS_DETAIL table. |
| EMPLOYEE_ID | NUMBER |  |  |  | EMPLOYEE_ID column  : Employee ID if witness is an employee. |
| EMPLOYEE_ASSIGN_ID | NUMBER |  | 18 |  | EMPLOYEE_ASSIGN_ID column  : Assignment ID if witness is an employee. |
| WITNESS_PER_TYPE_CODE | VARCHAR2 | 30 |  |  | EMP/NON EMP lookup. To check whether the witness is an employee or not. |
| WITNESS_TYPE_CODE | VARCHAR2 | 30 |  |  | Unique Witness type id. Foreign key for WITNESS_TYPE_ID |
| WITNESS_NAME | VARCHAR2 | 200 |  |  | Witness Name (for both Employee and Non Employee) |
| WITNESS_EMAIL | VARCHAR2 | 250 |  |  | Witness email id when employee is an non employee. |
| WITNESS_COUNTRY_CODE_NUM | VARCHAR2 | 30 |  |  | WITNESS_COUNTRY_CODE_NUM : Witness phoney country code number. |
| WITNESS_AREA_CODE | VARCHAR2 | 30 |  |  | WITNESS_AREA_CODE column : Witness phone area code number. |
| WITNESS_PHONE | VARCHAR2 | 18 |  |  | Witness phone number. This is for non employee only. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the incident witness is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INCIDENT_WITNESSES_N1 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_DETAIL_ID |
| HNS_INCIDENT_WITNESSES_UK1 | Unique | FUSION_TS_TX_DATA | WITNESS_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
