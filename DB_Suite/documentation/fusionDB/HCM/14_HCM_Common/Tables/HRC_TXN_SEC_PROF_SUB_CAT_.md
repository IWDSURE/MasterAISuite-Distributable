# HRC_TXN_SEC_PROF_SUB_CAT_

Sub Category Securiity Profile Table: This tables stores the Sub Category Selections made by user from the UI with respect to each securoty profile entry. There is one to many relationship between this and entry table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofsubcat-30873.html#hrctxnsecprofsubcat-30873](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofsubcat-30873.html#hrctxnsecprofsubcat-30873)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_SEC_PROF_SUB_CAT_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TXN_SUB_CAT_SEC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_SUB_CAT_SEC_ID | NUMBER |  | 18 | Yes | Primary Key to the current table. |
| TXN_SEC_PROF_ENTRY_ID | NUMBER |  | 18 |  | Foreign Key to HRC_TXN_SEC_PROF_ENTRY table |
| SUB_CATEGORY_CODE | VARCHAR2 | 100 |  |  | Specified sub category within application family and category combination. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_SEC_PROF_SUB_CATN1_ | Non Unique | Default | TXN_SUB_CAT_SEC_ID, LAST_UPDATE_DATE |
| HRC_TXN_SEC_PROF_SUB_CAT_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TXN_SUB_CAT_SEC_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
