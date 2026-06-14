# ANC_PER_ABS_CERTS

Person Absence Certifications Base Table

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabscerts-19358.html#ancperabscerts-19358](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabscerts-19358.html#ancperabscerts-19358)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_CERTS_PK | PER_CERT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_CERT_ID | NUMBER |  | 18 | Yes | Person Certification Evidence Identifier |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| CASE_ID | NUMBER |  | 18 |  | CASE_ID |
| CLASS_CD | VARCHAR2 | 30 |  |  | Stores class type of the certification which will be consumed by the processing code. |
| DESCRIPTION | VARCHAR2 | 200 |  |  | DESCRIPTION |
| REV_PAY_START_DT | DATE |  |  |  | Revised Payment Start Date |
| REV_PAY_END_DT | DATE |  |  |  | Revised Payment End Date |
| CONFIRM_RSN_CD | VARCHAR2 | 30 |  |  | Confirm Reason Code |
| VOID_RSN_CD | VARCHAR2 | 30 |  |  | Void Reason Code |
| REV_PAY_PCT | NUMBER |  | 18 |  | Revised Payment Percentage |
| CERT_CREATION_DATE | DATE |  |  |  | Certification creation date (This field does not hold the record creation date) |
| ABSENCE_CERTIFICATION_ID | NUMBER |  | 18 | Yes | Evidence identifier references setup evidence id |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 |  | reference to Person Absence Entry Identifier |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| CTFN_CREATION_MODE | VARCHAR2 | 30 |  |  | CTFN_CREATION_MODE |
| REQUIRED_BY_DATE | DATE |  |  |  | certification required by |
| VALID_UPTO_DATE | DATE |  |  |  | certification valid upto |
| RECEIVED_YN | VARCHAR2 | 1 |  |  | certification recieved flag |
| RECEIVED_DATE | DATE |  |  |  | certification received data |
| RECEIVED_LATE_YN | VARCHAR2 | 1 |  |  | Certification recieved late flag |
| ACCEPTED_YN | VARCHAR2 | 1 |  |  | Certification accepted flag |
| ACCEPTED_BY | VARCHAR2 | 64 |  |  | Certification accepted by |
| ACCEPTED_DATE | DATE |  |  |  | Cerfication accepted date |
| LATE_REASON | VARCHAR2 | 100 |  |  | Reason for late certification |
| EVIDENCE_SOURCE | VARCHAR2 | 30 |  |  | Certification source |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| COMPLETE_YN | VARCHAR2 | 30 |  |  | COMPLETE_YN |
| COMPLETED_DATE | DATE |  |  |  | COMPLETED_DATE |
| VOID_YN | VARCHAR2 | 30 |  |  | VOID_YN |
| VOIDED_DATE | DATE |  |  |  | VOIDED_DATE |
| TARGET_PLAN_ID | NUMBER |  | 18 |  | Target Plan Id |
| TARGET_PLAN_ALL_FLAG | VARCHAR2 | 30 |  |  | All Target Plan Selection |
| COMMENTS | VARCHAR2 | 250 |  |  | COMMENTS |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_TYPE | VARCHAR2 | 64 |  |  | This column will specify which process/source has changed the record...like ESS/Admin Login/User Login/Loaders |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ABS_AGGREGATION_ID | NUMBER |  | 18 |  | To store the aggregation id against which certificate needs to be applied |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_CERTS_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_CERTS_N2 | Non Unique | Default | STATUS |
| ANC_PER_ABS_CERTS_N3 | Non Unique | Default | PERSON_ID |
| ANC_PER_ABS_CERTS_N4 | Non Unique | Default | CASE_ID |
| ANC_PER_ABS_CERTS_U1 | Unique | Default | PER_CERT_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
