# PAY_BAL_EXCEP_REPORT_ENTRIES

This table contains information of balance exception report entries.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalexcepreportentries-17108.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalexcepreportentries-17108.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_EXCEP_RPRT_ENTR_PK | BAL_EXCEP_REPORT_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_EXCEP_REPORT_ENTRY_ID | NUMBER |  | 18 | Yes | BAL_EXCEP_REPORT_ENTRY_ID |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BAL_EXCEPTION_REPORT_ID | NUMBER |  | 18 | Yes | BAL_EXCEPTION_REPORT_ID |
| BAL_EXCEPTION_ID | NUMBER |  | 18 | Yes | BAL_EXCEPTION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_EXCEP_RPRT_ENTR_PK | Unique | Default | BAL_EXCEP_REPORT_ENTRY_ID, ORA_SEED_SET1 |
| PAY_BAL_EXCEP_RPRT_ENTR_PK1 | Unique | Default | BAL_EXCEP_REPORT_ENTRY_ID, ORA_SEED_SET2 |
| PAY_BAL_EXCEP_RPRT_ENTR_UK1 | Unique | Default | BAL_EXCEPTION_REPORT_ID, BAL_EXCEPTION_ID, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET1 |
| PAY_BAL_EXCEP_RPRT_ENTR_UK11 | Unique | Default | BAL_EXCEPTION_REPORT_ID, BAL_EXCEPTION_ID, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
