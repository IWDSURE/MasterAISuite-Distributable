# PER_POS_SEC_PROFILE_POSITIONS

Position Security Profile Positions

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpossecprofilepositions-28874.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpossecprofilepositions-28874.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_POS_SEC_PROF_POS_PK | POS_SEC_PROFILE_POSITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| POS_SEC_PROFILE_POSITION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| POSITION_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_POSITION_SECURITY_PROFILES table. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| INCLUDE_EXCLUDE_FLAG | VARCHAR2 | 1 |  | Yes | This option either enables security for particular positions or disables positions when securing by a position tree. |  |
| POSITION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_POSITIONS_F table. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_POS_SEC_PROFILE_POSIT_N20 | Non Unique | Default | SGUID |
| PER_POS_SEC_PROF_POS_FK2 | Non Unique | FUSION_TS_TX_DATA | POSITION_SECURITY_PROFILE_ID |
| PER_POS_SEC_PROF_POS_PK | Unique | FUSION_TS_TX_DATA | POS_SEC_PROFILE_POSITION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
