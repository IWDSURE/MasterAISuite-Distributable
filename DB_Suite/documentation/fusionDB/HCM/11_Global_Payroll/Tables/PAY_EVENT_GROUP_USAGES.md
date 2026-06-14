# PAY_EVENT_GROUP_USAGES

This associates the Event Group to the Products that use the Event Group

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroupusages-22962.html#payeventgroupusages-22962](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroupusages-22962.html#payeventgroupusages-22962)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_GROUP_USAGES_PK | EVENT_GROUP_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_GROUP_USAGE_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| EVENT_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to Pay Event Groups |
| APPLICATION_CODE | VARCHAR2 | 5 |  | Yes | Application Code of the application allowed to use the Event Group |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_GROUP_USAGES_PK | Unique | Default | EVENT_GROUP_USAGE_ID |
| PAY_EVENT_GROUP_USAGES_UK1 | Unique | Default | EVENT_GROUP_ID, APPLICATION_CODE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
