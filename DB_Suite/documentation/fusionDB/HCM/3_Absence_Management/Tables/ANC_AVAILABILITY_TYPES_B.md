# ANC_AVAILABILITY_TYPES_B

This table stores availability types.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailabilitytypesb-15238.html#ancavailabilitytypesb-15238](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailabilitytypesb-15238.html#ancavailabilitytypesb-15238)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_AVAILABILITY_TYPES_B_PK | AVAILABILITY_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_TYPE_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | The Status of Availability Type: 1 Active, 2 Inactive |
| CONTRACTED_HOURS | VARCHAR2 | 30 |  | Yes | 1. Contracted Availability, 2. Other Availability |
| WORK_SHIFT_TYPE | VARCHAR2 | 30 |  | Yes | The work shift type: 1 Time, 2. Elapsed |
| REPEATED_PATTERN_TYPE | VARCHAR2 | 30 |  | Yes | The work shift Repeated Pattern Type:
1. Every week
2. Every 2 weeks
3. Every 3 weeks
4. Every 4 weeks |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | User can select from UI. |
| IS_WORK_PATTERN_FLAG | VARCHAR2 | 1 |  |  | Flag would be null for availability pattern and Yes for work pattern setup. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_AVAILABILITY_TYPES_B_PK | Unique | Default | AVAILABILITY_TYPE_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
