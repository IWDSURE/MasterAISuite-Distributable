# PAY_PAY_SECURITY_PROFILE_PAYS

This table holds information of payroll security profiles.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaysecurityprofilepays-27567.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypaysecurityprofilepays-27567.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAY_SECURITY_PROFILE_PK | PAY_SECURITY_PROFILE_PAY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PAY_SECURITY_PROFILE_PAY_ID | NUMBER |  | 18 | Yes | PAY_SECURITY_PROFILE_PAY_ID |  |
| PAY_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | PAY_SECURITY_PROFILE_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| PAYROLL_ID | NUMBER |  | 18 | Yes | PAYROLL_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PAY_SECURITY_PROFILE_PK | Unique | Default | PAY_SECURITY_PROFILE_PAY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
