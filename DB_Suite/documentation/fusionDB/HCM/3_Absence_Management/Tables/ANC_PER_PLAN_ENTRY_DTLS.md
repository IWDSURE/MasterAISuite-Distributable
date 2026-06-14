# ANC_PER_PLAN_ENTRY_DTLS

This table holds information of  the person absence plan entry details.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperplanentrydtls-13129.html#ancperplanentrydtls-13129](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperplanentrydtls-13129.html#ancperplanentrydtls-13129)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_PLAN_ENTRY_DTLS_PK | PER_PLAN_ENTRY_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_PLAN_ENTRY_DTL_ID | NUMBER |  | 18 | Yes | person absence plan entry detail identifier |
| PLAN_ID | NUMBER |  | 18 | Yes | Absence Plan Identifier |
| PAY_FACTOR | NUMBER |  |  | Yes | Pay Factor |
| WORK_TERM_ASG_ID | NUMBER |  | 18 | Yes | Employee Work Terms Identifier |
| PROCD_DATE | DATE |  |  |  | Date of the Transaction |
| START_DATE | DATE |  |  |  | Entitlement Start Date |
| END_DATE | DATE |  |  |  | Entitlement End Date |
| VALUE | NUMBER |  |  | Yes | Entitlement Value |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_PLAN_ENTRY_DTLS_N1 | Non Unique | Default | WORK_TERM_ASG_ID, PLAN_ID, PAY_FACTOR |
| ANC_PER_PLAN_ENTRY_DTLS_N2 | Non Unique | Default | PERSON_ID |
| ANC_PER_PLAN_ENTRY_DTLS_U1 | Unique | Default | PER_PLAN_ENTRY_DTL_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
