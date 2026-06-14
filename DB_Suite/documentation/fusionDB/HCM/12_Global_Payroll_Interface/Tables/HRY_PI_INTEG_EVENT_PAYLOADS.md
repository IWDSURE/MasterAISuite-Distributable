# HRY_PI_INTEG_EVENT_PAYLOADS

Table for saving payroll interface integration event pay load details

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiintegeventpayloads-26703.html#hrypiintegeventpayloads-26703](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiintegeventpayloads-26703.html#hrypiintegeventpayloads-26703)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_INTEG_EVENT_PAYLOADS_PK | INTEGRATION_EVENT_PAYLOADS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTEGRATION_EVENT_PAYLOADS_ID | NUMBER |  | 18 | Yes | Primary Key for Integration event Payloads |
| INTEGRATION_PAYEVENT_MAP_ID | NUMBER |  | 18 |  | Foreign Key to HRY_PI_INTEG_PAYEVENTS_MAPPING |
| CONFIG_EVENTS_MAPPING_ID | NUMBER |  | 18 |  | Foreign key to HRY_PI_CONFIG_EVENTS_MAPPING |
| EVENT_CATEGORY_ID | NUMBER |  | 18 |  | Foreign key ID Mapping to hry_event_categories table. |
| EXT_DEFINITION_ID | NUMBER |  | 18 |  | Foreign Key ID Mapping Column to per_Ext_definitions_b |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_INTEG_EVENT_PAYLOADS_PK | Unique | Default | INTEGRATION_EVENT_PAYLOADS_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
