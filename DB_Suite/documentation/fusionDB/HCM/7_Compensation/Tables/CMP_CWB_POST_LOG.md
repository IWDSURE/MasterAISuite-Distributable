# CMP_CWB_POST_LOG

Stores Post Process Log information.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostlog-28285.html#cmpcwbpostlog-28285](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbpostlog-28285.html#cmpcwbpostlog-28285)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_POST_LOG_PK | RUN_LOG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_LOG_ID | NUMBER |  | 18 | Yes | Run Log Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| RUN_ID | NUMBER |  | 18 |  | RUN_ID |
| REQUESTID | NUMBER |  | 18 |  | REQUESTID |
| THREAD_ID | NUMBER |  |  |  | THREAD_ID |
| APP_NAME | VARCHAR2 | 30 |  |  | APP_NAME |
| LOG_TIMESTAMP | TIMESTAMP |  |  | Yes | LOG_TIMESTAMP |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PERSON_EVENT_ID | NUMBER |  | 18 |  | PERSON_EVENT_ID |
| PERSON_RUN_ID | NUMBER |  | 18 |  | PERSON_RUN_ID |
| ROW_TYPE | VARCHAR2 | 30 |  |  | ROW_TYPE |
| COMPONENT_ID | NUMBER |  | 18 |  | COMPONENT_ID |
| PLAN_ATTRIBUTE_ID | NUMBER |  | 18 |  | PLAN_ATTRIBUTE_ID |
| ATTRIBUTE_ELEMENT_ID | NUMBER |  | 18 |  | ATTRIBUTE_ELEMENT_ID |
| LOG_SOURCE | VARCHAR2 | 250 |  | Yes | LOG_SOURCE |
| LOG_SEVERITY | VARCHAR2 | 30 |  |  | LOG_SEVERITY |
| APPLICATION_ID | NUMBER |  |  |  | APPLICATION_ID |
| MESSAGE_NAME | VARCHAR2 | 30 |  |  | MESSAGE_NAME |
| MESSAGE_TEXT | VARCHAR2 | 240 |  |  | MESSAGE_TEXT |
| MESSAGE_ADMIN_DETAILS | VARCHAR2 | 4000 |  |  | MESSAGE_ADMIN_DETAILS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_POST_LOG_N1 | Non Unique | Default | RUN_ID, PERSON_RUN_ID |
| CMP_CWB_POST_LOG_PK | Unique | Default | RUN_LOG_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
