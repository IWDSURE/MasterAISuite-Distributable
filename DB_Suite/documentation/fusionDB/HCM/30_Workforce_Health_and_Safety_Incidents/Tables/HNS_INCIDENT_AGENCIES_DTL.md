# HNS_INCIDENT_AGENCIES_DTL

HNS INCIDENT AGENGIES DETAIL. This table stores Notified agencies related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentagenciesdtl-19629.html#hnsincidentagenciesdtl-19629](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsincidentagenciesdtl-19629.html#hnsincidentagenciesdtl-19629)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_INCIDENT_AGENCIES_DTL_PK | INCIDENT_AGENCY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INCIDENT_ID | NUMBER |  | 18 | Yes | Incident Identifier. Foreign key for HNS_INCIDENTS_SUMMARY table. |
| NOTIFIED_AGENCY_CODE | VARCHAR2 | 30 |  | Yes | Agencies notified identifier. Lookup FND_LOOKUP NOTIFIED_AGENCY. |
| INCIDENT_AGENCY_ID | NUMBER |  | 18 | Yes | Primary key for HNS_INCIDENT_AGENCIES_DTL table. |
| DATE_NOTIFIED | TIMESTAMP |  |  |  | DATE_NOTIFIED column : Date the agencies are notified. |
| NOTIFIED_BY | VARCHAR2 | 64 |  |  | NOTIFIED_BY column : Agencies notified by person(employee) |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the incident agency  is checked for deletion. |
| ATTENDED_SITE_FLAG | VARCHAR2 | 1 |  |  | Attended Site flag. To check if the agencies attended the site. |
| DATE_SITE_ATTENDED | TIMESTAMP |  |  |  | The date the site was attended by the notified agency. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_INCIDENT_AGENCIES_DTL_N1 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_ID |
| HNS_INCIDENT_AGENCIES_DTL_UK1 | Unique | FUSION_TS_TX_DATA | INCIDENT_AGENCY_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
