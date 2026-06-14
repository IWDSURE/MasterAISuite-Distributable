# PAY_PAY_SECURITY_PROFILE_PAYS_

This table holds information of payroll security profiles.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaysecurityprofilepays-15795.html#paypaysecurityprofilepays-15795](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaysecurityprofilepays-15795.html#paypaysecurityprofilepays-15795)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAY_SECURITY_PROFILE_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PAY_SECURITY_PROFILE_PAY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_SECURITY_PROFILE_PAY_ID | NUMBER |  | 18 | Yes | PAY_SECURITY_PROFILE_PAY_ID |
| PAY_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | PAY_SECURITY_PROFILE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| PAYROLL_ID | NUMBER |  | 18 |  | PAYROLL_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PAY_SECURITY_PROFILE_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PAY_SECURITY_PROFILE_PAY_ID |
| PAY_PAY_SECURITY_PROFILN1_ | Non Unique | Default | PAY_SECURITY_PROFILE_PAY_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
