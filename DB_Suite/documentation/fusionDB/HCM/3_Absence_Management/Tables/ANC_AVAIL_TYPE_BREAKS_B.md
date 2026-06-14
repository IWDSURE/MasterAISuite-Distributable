# ANC_AVAIL_TYPE_BREAKS_B

This table stores availability type breaks.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailtypebreaksb-6128.html#ancavailtypebreaksb-6128](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailtypebreaksb-6128.html#ancavailtypebreaksb-6128)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_AVAIL_TYPE_BREAKS_B_PK | AVAILABILITY_TYPE_BREAK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_TYPE_BREAK_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type Break. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| AVAILABILITY_TYPE_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type. |
| BREAK_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The Availability Shift Break Type:
1. Fixed
2. Anytime during range
3. Anytime during shift |
| BREAK_DURATION | NUMBER |  | 22 | Yes | The minutes defining a break period. |
| BREAK_PAID | VARCHAR2 | 30 |  | Yes | Paid/Unpaid |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_AVAIL_TYPE_BREAKS_B_N1 | Non Unique | Default | AVAILABILITY_TYPE_ID |
| ANC_AVAIL_TYPE_BREAKS_B_PK | Unique | Default | AVAILABILITY_TYPE_BREAK_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
