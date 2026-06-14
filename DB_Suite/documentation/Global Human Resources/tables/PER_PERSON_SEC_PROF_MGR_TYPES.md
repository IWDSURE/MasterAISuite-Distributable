# PER_PERSON_SEC_PROF_MGR_TYPES

PER_PERSON_SEC_PROF_MGR_TYPES to store Manager Type relates security preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecprofmgrtypes-12967.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecprofmgrtypes-12967.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PRSN_SEC_PROF_MGR_TYP_PK | PERSON_SEC_PROF_MGR_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_SEC_PROF_MGR_TYPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| PERSON_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PERSON_SECURITY_PROFILES table. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| MANAGER_TYPE_VALUE | VARCHAR2 | 30 |  | Yes | Denotes the value for manager type. |  |
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
| PER_PRSN_SEC_PROF_MGR_TYP_FK1 | Non Unique | FUSION_TS_TX_DATA | PERSON_SECURITY_PROFILE_ID |
| PER_PRSN_SEC_PROF_MGR_TYP_PK | Unique | FUSION_TS_TX_DATA | PERSON_SEC_PROF_MGR_TYPE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
