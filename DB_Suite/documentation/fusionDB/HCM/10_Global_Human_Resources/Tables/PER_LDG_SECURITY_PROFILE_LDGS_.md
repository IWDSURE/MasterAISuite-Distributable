# PER_LDG_SECURITY_PROFILE_LDGS_

Legislative Data Groups Security Profile LDGs.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldgsecurityprofileldgs-18501.html#perldgsecurityprofileldgs-18501](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perldgsecurityprofileldgs-18501.html#perldgsecurityprofileldgs-18501)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LDG_SEC_PROF_LDGS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LDG_SECURITY_PROFILE_LDG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LDG_SECURITY_PROFILE_LDG_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LDG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_LDG_SECURITY_PROFILES table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
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
| PER_LDG_SEC_PROF_LDGSN1_ | Non Unique | Default | LDG_SECURITY_PROFILE_LDG_ID |
| PER_LDG_SEC_PROF_LDGS_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, LDG_SECURITY_PROFILE_LDG_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
