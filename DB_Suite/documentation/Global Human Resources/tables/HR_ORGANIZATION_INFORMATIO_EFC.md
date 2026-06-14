# HR_ORGANIZATION_INFORMATIO_EFC

This table only contains a subset of the columns from the base table. Contains a copy of the NCU (National Currency Unit) and currency code values prior to EFC. The table is only maintained by the EFC process.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformatioefc-12238.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformatioefc-12238.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ORGANIZATION_INFORMA_EFC_PK | ORG_INFORMATION_ID, EFC_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_INFORMATION_ID | NUMBER |  |  | Yes | Refer to column comment  on base table. |
| EFC_ACTION_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_EFC_ACTIONS table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ORG_INFORMATION5 | VARCHAR2 | 150 |  |  | Refer to column comment  on base table. |
| ORG_INFORMATION6 | VARCHAR2 | 150 |  |  | Refer to column comment  on base table. |
| ORG_INFORMATION10 | VARCHAR2 | 150 |  |  | Refer to column comment  on base table. |
| EFC_BG_CURRENCY | VARCHAR2 | 30 |  |  | Refer to column comment  on base table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ORGANIZATION_INFORMA_EFC_PK | Unique | Default | ORG_INFORMATION_ID, EFC_ACTION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
