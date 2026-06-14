# PAY_EVENT_USAGES

This table contains the intersection between PAY_PROCESS_EVENTS and PAY_EVENT_RELATIONSHIPS. Thus it identifies the events that cause the reprocessing of an action.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventusages-4992.html#payeventusages-4992](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventusages-4992.html#payeventusages-4992)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_USAGES_PK | EVENT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_USAGE_ID | NUMBER |  | 18 | Yes | EVENT_USAGE_ID |
| PROCESS_EVENT_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_PROCESS_EVENTS |
| USAGE_ID | NUMBER |  | 18 | Yes | Foreign key for the type of usage. |
| USAGE_TYPE | VARCHAR2 | 30 |  | Yes | The type of usage |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_USAGES_N1 | Non Unique | Default | PROCESS_EVENT_ID |
| PAY_EVENT_USAGES_N2 | Non Unique | Default | USAGE_ID, USAGE_TYPE |
| PAY_EVENT_USAGES_U1 | Unique | Default | EVENT_USAGE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
