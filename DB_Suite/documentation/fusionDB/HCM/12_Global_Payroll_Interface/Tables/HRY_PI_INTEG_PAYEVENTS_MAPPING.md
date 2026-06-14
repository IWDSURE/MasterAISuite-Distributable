# HRY_PI_INTEG_PAYEVENTS_MAPPING

Table for saving payroll interface integration pay load details

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiintegpayeventsmapping-25457.html#hrypiintegpayeventsmapping-25457](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrypiintegpayeventsmapping-25457.html#hrypiintegpayeventsmapping-25457)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_PI_INTEG_PAYEVENTS_MAP_PK | INTEGRATION_PAYEVENT_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTEGRATION_PAYEVENT_MAP_ID | NUMBER |  | 18 | Yes | Primary Key for Integration Payload |
| INTEGRATION_SETUP_ID | NUMBER |  | 18 |  | Foreign Key to HRY_PI_INTEG_SETUP |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to PAY_ALL_PAYROLLS_F |
| PAY_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PAY_OBJECT_GROUPS |
| CONFIG_EVENTS_MAPPING_ID | NUMBER |  | 18 |  | Foreign key to HRY_PI_CONFIG_EVENTS_MAPPING |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES_B. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PARENT_RULE_PROPERTY_ID | NUMBER |  | 18 |  | Assigning Rule Name Configuration to integration setup |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_PI_INTEG_PAYEVENTS_MAP_PK | Unique | Default | INTEGRATION_PAYEVENT_MAP_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
