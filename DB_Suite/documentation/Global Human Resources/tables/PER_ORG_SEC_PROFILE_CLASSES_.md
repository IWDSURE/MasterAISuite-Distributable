# PER_ORG_SEC_PROFILE_CLASSES_

Organization Security Profile Organization Classifications.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecprofileclasses-23920.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perorgsecprofileclasses-23920.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ORG_SEC_PROFILE_CLS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_SEC_PROFILE_CLASS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_SEC_PROFILE_CLASS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ORG_SECURITY_PROFILES table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CLASSIFICATION_CD | VARCHAR2 | 40 |  |  | This field represents the id of the organization classification secured in an organization security profile. |
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
| PER_ORG_SEC_PROFILE_CLAN1_ | Non Unique | Default | ORG_SEC_PROFILE_CLASS_ID |
| PER_ORG_SEC_PROFILE_CLS_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, ORG_SEC_PROFILE_CLASS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
