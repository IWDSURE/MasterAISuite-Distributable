# PER_COUNTRY_SEC_PROF_COUNTRIES

Country Security Profile Countries.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecprofcountries-24344.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecprofcountries-24344.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_COUNTRY_SEC_PROF_CNTRY_PK | COUNTRY_SEC_PROF_COUNTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| COUNTRY_SEC_PROF_COUNTRY_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |  |
| COUNTRY_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_COUNTRY_SEC_PROFILES. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| COUNTRY_CODE | VARCHAR2 | 2 |  | Yes | The code representing the country to be included in the country security profile. |  |
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
| PER_COUNTRY_SEC_PROF_CNTRY_FK1 | Non Unique | FUSION_TS_TX_DATA | COUNTRY_SECURITY_PROFILE_ID |
| PER_COUNTRY_SEC_PROF_CNTRY_PK | Unique | FUSION_TS_TX_DATA | COUNTRY_SEC_PROF_COUNTRY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
