# PAY_FLW_SECURITY_PROFILE_PAYS

This table holds information of payroll flow security profiles.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflwsecurityprofilepays-11124.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflwsecurityprofilepays-11124.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLW_SECURITY_PROFILE_PK | FLW_SECURITY_PROFILE_FLW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLW_SECURITY_PROFILE_FLW_ID | NUMBER |  | 18 | Yes | FLW_SECURITY_PROFILE_FLW_ID |
| FLW_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | FLW_SECURITY_PROFILE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| FLOW_ID | NUMBER |  | 18 | Yes | FLOW_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_FLW_SECURITY_PROFILE_PK | Unique | Default | FLW_SECURITY_PROFILE_FLW_ID, ORA_SEED_SET1 |
| PAY_FLW_SECURITY_PROFILE_PK1 | Unique | Default | FLW_SECURITY_PROFILE_FLW_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
