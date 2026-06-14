# PER_PERSON_SEC_PROF_PER_TYPES

Person Security Profile Person Types

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecprofpertypes-18779.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecprofpertypes-18779.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PRSN_SEC_PROF_PER_TYP_PK | PERSON_SEC_PROF_PER_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_SEC_PROF_PER_TYPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PERSON_SECURITY_PROFILES table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_TYPE_COLUMN | VARCHAR2 | 30 |  | Yes | This field allows a valid person type that is defined by the customer. |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | This field allows a valid person type that has been seeded by Fusion Development Teams. |
| PERSON_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSON_TYPES table. |
| ACCESS_TO | VARCHAR2 | 30 |  | Yes | Cannot find this, I think it's probably Access to Own Record.  Leave blank |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_SEC_PROF_PER_T_N20 | Non Unique | Default | SGUID |
| PER_PRSN_SEC_PROF_PER_TYP_FK1 | Non Unique | FUSION_TS_TX_DATA | PERSON_SECURITY_PROFILE_ID |
| PER_PRSN_SEC_PROF_PER_TYP_PK | Unique | FUSION_TS_TX_DATA | PERSON_SEC_PROF_PER_TYPE_ID, ORA_SEED_SET1 |
| PER_PRSN_SEC_PROF_PER_TYP_PK1 | Unique | FUSION_TS_TX_DATA | PERSON_SEC_PROF_PER_TYPE_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
