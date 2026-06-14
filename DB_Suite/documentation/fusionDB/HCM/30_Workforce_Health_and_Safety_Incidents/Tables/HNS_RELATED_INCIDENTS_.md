# HNS_RELATED_INCIDENTS_

HNS RELATED INCIDENTS. This table stores all related incidents. Parent child relationship.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsrelatedincidents-26624.html#hnsrelatedincidents-26624](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsrelatedincidents-26624.html#hnsrelatedincidents-26624)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_RELATED_INCIDENTS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, INCIDENT_ID, RELATED_INCIDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INCIDENT_ID | NUMBER |  | 18 | Yes | Unique Incident identifier. Foreign key for HNS_INCIDENTS_SUMMARY table. |
| RELATED_INCIDENT_ID | NUMBER |  | 18 | Yes | RELATED_INCIDENT_ID column : Thes are the incidents related to the base incident. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the related incident is checked for deletion. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_RELATED_INCIDENTSN1_ | Non Unique | Default | INCIDENT_ID, RELATED_INCIDENT_ID, LAST_UPDATE_DATE |
| HNS_RELATED_INCIDENTS_UK1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, INCIDENT_ID, RELATED_INCIDENT_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
