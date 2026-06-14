# PER_DATA_SEC_PROCESS_DTLS_

per_data_sec_process_dlts to track the last successful runtime for the dataSecurity  ess processes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdatasecprocessdtls-11267.html#perdatasecprocessdtls-11267](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdatasecprocessdtls-11267.html#perdatasecprocessdtls-11267)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DATA_SEC_PROCESS_DTLS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DATA_SEC_PROCESS_DTLS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_SEC_PROCESS_DTLS_ID | NUMBER |  |  | Yes | primary key for ACL Ess process |
| DATA_SEC_PROCESS_NAME | VARCHAR2 | 64 |  |  | process name for the ACL ESS process(Unique) |
| PROCESS_JOB_ID | NUMBER |  |  |  | id for the ACL Ess process |
| RUN_DATE_TIME | VARCHAR2 | 4000 |  |  | RUN_DATE_TIME |
| START_DATE_TIME | VARCHAR2 | 4000 |  |  | START_DATE_TIME |
| PROCESS_JOB_DETAILS | VARCHAR2 | 4000 |  |  | additional job details if any |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DATA_SEC_PROCESSN1_ | Non Unique | Default | DATA_SEC_PROCESS_DTLS_ID, LAST_UPDATE_DATE |
| PER_DATA_SEC_PROCESS_DTLS_U_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DATA_SEC_PROCESS_DTLS_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
