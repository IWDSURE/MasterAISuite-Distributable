# WLF_RECOM_PROCESSING_DETAILS

Table to store reconciliation details of recommendation profile.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomprocessingdetails-19742.html#wlfrecomprocessingdetails-19742](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomprocessingdetails-19742.html#wlfrecomprocessingdetails-19742)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOM_PROCESSING_DTL_PK | PROCESSING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESSING_ID | NUMBER |  |  | Yes | System generated unique identifier. |
| RECOMMENDATION_PROFILE_ID | NUMBER |  |  | Yes | Reference to the recommendation profile id |
| IS_RECONCILE_READY | VARCHAR2 | 1 |  |  | Indicator to provide hint whether recommendation profile is ready to  be reconciled. |
| LATEST_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when recommendation profile is last reconciled. |
| LATEST_PROCESSING_STATUS | VARCHAR2 | 32 |  |  | The status of last reconciliation |
| LATEST_JOB_ID | NUMBER |  |  |  | The latest job id that processed the recommendation profile |
| LAST_SUCC_PROCESSED_DATE | TIMESTAMP |  |  |  | The date when recommendation profile is last reconciled successfully. |
| LAST_SUCC_JOB_ID | NUMBER |  |  |  | The job id of last successful reconcile of recommendation profile |
| JOB_NAME | VARCHAR2 | 32 |  |  | JOB_NAME |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOM_PROC_DETAILS_N1 | Non Unique | WLF_RECOM_PROC_DETAILS_N1 | RECOMMENDATION_PROFILE_ID |
| WLF_RECOM_PROC_DETAILS_U1 | Unique | WLF_RECOM_PROC_DETAILS_U1 | PROCESSING_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
