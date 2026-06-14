# PAY_DEDN_REPORT_USE

This table contains details of which deductions are reported by each tax reporting unit.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydednreportuse-23086.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydednreportuse-23086.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DEDN_REPORT_USE_PK | DEDN_REPORT_USE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEDN_REPORT_USE_ID | NUMBER |  | 18 | Yes | DEDN_REPORT_USE_ID |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 | Yes | DEDUCTION_TYPE_ID |
| TAX_UNIT_ID | NUMBER |  | 18 | Yes | TAX_UNIT_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DEDN_REPORT_USE_PK | Unique | Default | DEDN_REPORT_USE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
