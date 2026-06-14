# WLF_EVENT_INCIDENTS

Table to store learning item object event incidents.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventincidents-13494.html#wlfeventincidents-13494](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventincidents-13494.html#wlfeventincidents-13494)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EVENT_INCIDENTS_PK | EVENT_INCIDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_INCIDENT_ID | NUMBER |  | 18 | Yes | EVENT_ATTEMPT_ID |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| COMMENTS | VARCHAR2 | 255 |  |  | COMMENTS |
| REASON_CODE | VARCHAR2 | 30 |  |  | REASON_CODE |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| EVENT_DISPOSITION_ID | NUMBER |  | 18 |  | EVENT_DISPOSITION_ID |
| STATUS_LAST_MODIFIED | TIMESTAMP |  |  |  | STATUS_LAST_MODIFIED |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| EVENT_INCIDENT_NUMBER | VARCHAR2 | 30 |  |  | EVENT_INCIDENT_NUMBER |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EVENT_INCIDENTS_N1 | Non Unique | Default | EVENT_ID |
| WLF_EVENT_INCIDENTS_N2 | Non Unique | Default | EVENT_INCIDENT_NUMBER |
| WLF_EVENT_INCIDENTS_PK | Unique | Default | EVENT_INCIDENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
