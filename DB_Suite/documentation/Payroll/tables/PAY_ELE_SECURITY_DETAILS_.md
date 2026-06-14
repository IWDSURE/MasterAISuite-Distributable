# PAY_ELE_SECURITY_DETAILS_

This table holds information of payroll element security details.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelesecuritydetails-16770.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelesecuritydetails-16770.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELE_SECURITY_DETAILS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PAY_ELE_SECURITY_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_ELE_SECURITY_DETAIL_ID | NUMBER |  | 18 | Yes | PAY_ELE_SECURITY_DETAIL_ID |
| PAY_ELE_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | PAY_SECURITY_PROFILE_ID |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CLASSIFICATION_ID | NUMBER |  | 18 |  | CLASSIFICATION_ID |
| INCLUSION_FLAG | VARCHAR2 | 1 |  |  | INCLUSION_FLAG |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_ELE_SECURITY_DETAIL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PAY_ELE_SECURITY_DETAIL_ID |
| PAY_ELE_SECURITY_DETAILS_PK1_ | Non Unique | Default | PAY_ELE_SECURITY_DETAIL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
