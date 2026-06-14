# PER_POS_SECPRF_AORSCOPE

Position Security Profile AOR Scopes Table: This table will hold scope of areas of responsibility preference selected by end-user when 'Secure by Areas Of Responsibility' option is enabled for position security profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpossecprfaorscope-19501.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpossecprfaorscope-19501.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POS_SECPRF_AORSCOPE_PK | POS_SEC_PROF_AOR_SCOPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POS_SEC_PROF_AOR_SCOPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| POSITION_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_POSITION_SECURITY_PROFILES. |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  | Yes | Responsibility type for areas of responsibility. |
| SCOPE_OF_RESPONSIBILITY | VARCHAR2 | 30 |  | Yes | Scope of areas of responsibility which will be used to identify secured access. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_POS_SECPRF_AORSCOPE_PK | Unique | FUSION_TS_TX_DATA | POS_SEC_PROF_AOR_SCOPE_ID |
| PER_POS_SECPRF_AORSCOPE_U1 | Unique | FUSION_TS_TX_DATA | POSITION_SECURITY_PROFILE_ID, RESPONSIBILITY_TYPE, SCOPE_OF_RESPONSIBILITY |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
