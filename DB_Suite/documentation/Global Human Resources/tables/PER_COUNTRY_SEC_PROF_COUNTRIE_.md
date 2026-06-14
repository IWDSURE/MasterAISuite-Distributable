# PER_COUNTRY_SEC_PROF_COUNTRIE_

Country Security Profile Countries.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecprofcountrie-3735.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecprofcountrie-3735.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_COUNTRY_SEC_PROF_CNTRY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, COUNTRY_SEC_PROF_COUNTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COUNTRY_SEC_PROF_COUNTRY_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| COUNTRY_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_COUNTRY_SEC_PROFILES. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| COUNTRY_CODE | VARCHAR2 | 2 |  |  | The code representing the country to be included in the country security profile. |
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
|-------|------------|------------|----------|
| PER_CNTRY_SEC_PROF_CNTRYN1_ | Non Unique | Default | COUNTRY_SEC_PROF_COUNTRY_ID |
| PER_COUNTRY_SEC_PROF_CNTRY_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, COUNTRY_SEC_PROF_COUNTRY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
