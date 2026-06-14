# HRC_TXN_SEC_PROF_SUB_CAT

Sub Category Securiity Profile Table: This tables stores the Sub Category Selections made by user from the UI with respect to each securoty profile entry. There is one to many relationship between this and entry table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofsubcat-28170.html#hrctxnsecprofsubcat-28170](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofsubcat-28170.html#hrctxnsecprofsubcat-28170)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_SEC_PROF_SUB_CAT_PK | TXN_SUB_CAT_SEC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_SUB_CAT_SEC_ID | NUMBER |  | 18 | Yes | Primary Key to the current table. |
| TXN_SEC_PROF_ENTRY_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_TXN_SEC_PROF_ENTRY table |
| SUB_CATEGORY_CODE | VARCHAR2 | 100 |  |  | Specified sub category within application family and category combination. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_SEC_PROF_SUB_CAT_U1 | Unique | Default | TXN_SUB_CAT_SEC_ID, ORA_SEED_SET1 |
| HRC_TXN_SEC_PROF_SUB_CAT_U11 | Unique | Default | TXN_SUB_CAT_SEC_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
