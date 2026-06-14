# PAY_ENTRY_USAGES

This table contains the periods of time that an element entry is active and therefore may be processed. It also specifies at which level within the three tier employee assignment hierarchy an element entry is attached.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentryusages-23345.html#payentryusages-23345](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payentryusages-23345.html#payentryusages-23345)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ENTRY_USAGES_PK | ENTRY_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTRY_USAGE_ID | NUMBER |  | 18 | Yes | ENTRY_USAGE_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | ELEMENT_ENTRY_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| DATE_FROM | DATE |  |  | Yes | DATE_FROM |
| DATE_TO | DATE |  |  | Yes | DATE_TO |
| USAGE_LEVEL | VARCHAR2 | 30 |  | Yes | USAGE_LEVEL |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | PAYROLL_TERM_ID |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | PAYROLL_ASSIGNMENT_ID |
| ASSIGNED_PAYROLL_ID | NUMBER |  | 18 |  | ASSIGNED_PAYROLL_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ENTRY_USAGES_N1 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID |
| PAY_ENTRY_USAGES_N2 | Non Unique | Default | ELEMENT_ENTRY_ID, PAYROLL_ASSIGNMENT_ID, USAGE_LEVEL |
| PAY_ENTRY_USAGES_N3 | Non Unique | Default | PAYROLL_ASSIGNMENT_ID |
| PAY_ENTRY_USAGES_N4 | Non Unique | Default | PAYROLL_TERM_ID |
| PAY_ENTRY_USAGES_N5 | Non Unique | Default | ASSIGNED_PAYROLL_ID |
| PAY_ENTRY_USAGES_PK | Unique | Default | ENTRY_USAGE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
