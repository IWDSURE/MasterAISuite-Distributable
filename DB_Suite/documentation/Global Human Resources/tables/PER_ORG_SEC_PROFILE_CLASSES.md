# PER_ORG_SEC_PROFILE_CLASSES

Organization Security Profile Organization Classifications.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecprofileclasses-13683.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecprofileclasses-13683.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ORG_SEC_PROFILE_CLS_PK | ORG_SEC_PROFILE_CLASS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ORG_SEC_PROFILE_CLASS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ORG_SECURITY_PROFILES table. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| CLASSIFICATION_CD | VARCHAR2 | 40 |  | Yes | This field represents the id of the organization classification secured in an organization security profile. |  |
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
| PER_ORG_SEC_PROFILE_CLS_FK1 | Non Unique | FUSION_TS_TX_DATA | ORG_SECURITY_PROFILE_ID |
| PER_ORG_SEC_PROFILE_CLS_PK | Unique | FUSION_TS_TX_DATA | ORG_SEC_PROFILE_CLASS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
