# HRC_TXN_SEC_PROF_ENTRY_

This table stores the data corressponding to each Transaction Security Profile by the user. This is a child table with respect to HRC_TXN_SEC_PROFILE table. Family, category and other details are stored here.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofentry-4642.html#hrctxnsecprofentry-4642](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofentry-4642.html#hrctxnsecprofentry-4642)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_SEC_PROF_ENTRY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TXN_SEC_PROF_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_SEC_PROF_ENTRY_ID | NUMBER |  | 18 | Yes | Primary Key to the current table. |
| TXN_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to HRC_TXN_SEC_PROFILE table |
| FAMILY | VARCHAR2 | 100 |  |  | Application family of the approval process. |
| CATEGORY_CODE | VARCHAR2 | 100 |  |  | Specified category within application family. |
| EXCLUDE_SELECTED_SUB_CAT | VARCHAR2 | 1 |  |  | Flag to indicate if selected sub categories are excluded or not. |
| ALL_SUB_CAT_SELECTED | VARCHAR2 | 1 |  |  | Flag to indicate if all sub categories are selected or not. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_SEC_PROF_ENTRYN1_ | Non Unique | Default | TXN_SEC_PROF_ENTRY_ID, LAST_UPDATE_DATE |
| HRC_TXN_SEC_PROF_ENTRY_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TXN_SEC_PROF_ENTRY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
