# HRC_TXN_SEC_PROF_ENTRY

This table stores the data corressponding to each Transaction Security Profile by the user. This is a child table with respect to HRC_TXN_SEC_PROFILE table. Family, category and other details are stored here.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofentry-24603.html#hrctxnsecprofentry-24603](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofentry-24603.html#hrctxnsecprofentry-24603)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_SEC_PROF_ENTRY_PK | TXN_SEC_PROF_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_SEC_PROF_ENTRY_ID | NUMBER |  | 18 | Yes | Primary Key to the current table. |
| TXN_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRC_TXN_SEC_PROFILE table |
| FAMILY | VARCHAR2 | 100 |  |  | Application family of the approval process. |
| CATEGORY_CODE | VARCHAR2 | 100 |  |  | Specified category within application family. |
| EXCLUDE_SELECTED_SUB_CAT | VARCHAR2 | 1 |  |  | Flag to indicate if selected sub categories are excluded or not. |
| ALL_SUB_CAT_SELECTED | VARCHAR2 | 1 |  |  | Flag to indicate if all sub categories are selected or not. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_SEC_PROF_ENTRY_N20 | Non Unique | Default | SGUID |
| HRC_TXN_SEC_PROF_ENTRY_U1 | Unique | Default | TXN_SEC_PROF_ENTRY_ID, ORA_SEED_SET1 |
| HRC_TXN_SEC_PROF_ENTRY_U11 | Unique | Default | TXN_SEC_PROF_ENTRY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
