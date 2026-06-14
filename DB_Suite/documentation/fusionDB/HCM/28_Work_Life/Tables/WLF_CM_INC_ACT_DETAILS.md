# WLF_CM_INC_ACT_DETAILS

Table to store incidents reported on a content.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmincactdetails-26470.html#wlfcmincactdetails-26470](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmincactdetails-26470.html#wlfcmincactdetails-26470)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CM_INC_ACT_DETAILS_PK | INCIDENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INCIDENT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ACTIVITY_ID | NUMBER |  | 18 | Yes | Foreign Key reference to WLF_CM_ACITITIES.ACTIVITY_ID. |
| CONTENT_ID | NUMBER |  | 18 | Yes | Associated content object. Foreign key to WLF_CM_CONTENTS_B. |
| INCIDENT_COMMENTS | VARCHAR2 | 4000 |  | Yes | Reason for reporting the incident. |
| INCIDENT_REASON_CODE | VARCHAR2 | 30 |  | Yes | Reason code will be a Standard or the extended lookup codes of a specific lookup type. |
| REPORTING_PERSON_ID | NUMBER |  | 18 | Yes | Person who reported the Content. |
| INCIDENT_REPORTED_DATE | TIMESTAMP |  |  | Yes | Date and Time at which the incident is reported. |
| INCIDENT_STATUS | VARCHAR2 | 30 |  | Yes | Status of the incident reported. {NEW, INPROGRESS , COMPLETE}. |
| ACTION_STATUS | VARCHAR2 | 30 |  |  | Action Status of the incident reported. {DISCARD, SUSPEND, DELETED}. |
| ACTION_TAKENBY_ID | NUMBER |  | 18 |  | Admin Person Id who acted on this incident. |
| LAST_ACTION_TAKEN_DATE | TIMESTAMP |  |  |  | Latest Date on which action taken. |
| ACTION_COMMENTS | VARCHAR2 | 4000 |  |  | Comments given by the Admin. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CM_INC_ACT_DETAILS_N1 | Non Unique | Default | CONTENT_ID |
| WLF_CM_INC_ACT_DETAILS_N2 | Non Unique | FUSION_TS_TX_DATA | INCIDENT_STATUS |
| WLF_CM_INC_ACT_DETAILS_U1 | Unique | Default | INCIDENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
