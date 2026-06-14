# HRE_TOUCHPT_EMPL_EVTS_INTRCNS

Employee interactions as defined in touchpoints like check-in, request feedback, anytime feedback, celebrations et all are stored in this table.

## Details

**Schema:** FUSION

**Object owner:** HRE

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptemplevtsintrcns-26425.html#hretouchptemplevtsintrcns-26425](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hretouchptemplevtsintrcns-26425.html#hretouchptemplevtsintrcns-26425)

## Primary Key

| Name | Columns |
|------|----------|
| HRE_TOUCHPT_EMPL_EVTS_INTR_PK | REFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REFERENCE_ID | NUMBER |  | 18 | Yes | Primary key, The copied primary key id of the engagement like checkin, request feedback et all. |
| TEMPLATE_ID | NUMBER |  | 18 |  | The template id of interactions. |
| REVIEW_PERIOD_ID | NUMBER |  | 18 |  | The review period of interactions. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | The status code of interactions like NEW or COMPLETED. |
| ENGAGEMENT_TYPE | VARCHAR2 | 30 |  | Yes | The event or interaction type like ORA_HRE_CHECK-IN, ORA_HRE_FEEDBACK, et all. |
| ENGAGEMENT_DATE | DATE |  |  |  | The date of engagement for example check-in date. |
| CREATED_FOR_PERSON_ID | NUMBER |  | 18 | Yes | The person_id for whom this engagement is created. |
| CREATED_FOR_ASSIGNMENT_ID | NUMBER |  | 18 |  | The assignment_id for whom this engagement is created. |
| CREATED_FOR_MANAGER_PERSON_ID | NUMBER |  | 18 |  | The manger_person_id of the person_id for whom this engagement is created. |
| CREATED_BY_PERSON_ID | NUMBER |  | 18 | Yes | The person_id who generated this engagement. |
| CREATED_BY_ASSIGNMENT_ID | NUMBER |  | 18 |  | The assignment_id who generated this engagement. |
| HIDDEN_FLAG | VARCHAR2 | 30 |  |  | Store data of type character . For example, 'Y' or 'N' for hidden flag from notes. |
| VISIBILITY | VARCHAR2 | 32 |  |  | The visbility level of this engagement. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_BUSINESS_GROUPS |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CHECKIN_TOPICS_DISCUSSED_COUNT | NUMBER |  | 18 |  | Store data of type number for the engagement type. For example, CHECKIN_TOPICS_DISCUSSED_COUNT for check-in engagements. |
| CHECKIN_TOPICS_TOTAL_COUNT | NUMBER |  | 18 |  | Store data of type number for the engagement type. For example, CHECKIN_TOPICS_TOTAL_COUNT for check-in engagements. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRE_TCHPT_EMP_EVTS_INTRCNS_N1 | Non Unique | hre_tchpt_emp_evts_intrcns_n1 | "ENGAGEMENT_DATE", "CREATED_FOR_PERSON_ID" |
| HRE_TCHPT_EMP_EVTS_INTRCNS_N2 | Non Unique | hre_tchpt_emp_evts_intrcns_n2 | "CREATED_BY_PERSON_ID" |
| HRE_TOUCHPT_EMPL_EVTS_INTR_PK | Unique | HRE_TOUCHPT_EMPL_EVTS_INTR_PK | REFERENCE_ID |

---

[← Back to Index](../27_Touchpoints_Tables_Index.md)
