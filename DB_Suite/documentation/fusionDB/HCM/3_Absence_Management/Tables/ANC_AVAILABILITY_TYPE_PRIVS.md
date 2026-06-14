# ANC_AVAILABILITY_TYPE_PRIVS

This table stores availability type privileges.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailabilitytypeprivs-4769.html#ancavailabilitytypeprivs-4769](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailabilitytypeprivs-4769.html#ancavailabilitytypeprivs-4769)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_AVAIL_TYPE_PRIVS_PK | AVAILABILITY_TYPE_PRIVS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_TYPE_PRIVS_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type Privileges. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| AVAILABILITY_TYPE_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type. |
| ROLE_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type Role. |
| ROLE_ACCESS_LEVEL | VARCHAR2 | 30 |  |  | The Role Access Level of Availability Type: 1. View, 2. View and Edit |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_AVAIL_TYPE_PRIVS_PK | Unique | Default | AVAILABILITY_TYPE_PRIVS_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
