# PAY_CONNECTED_FLOWS

A record will be inserted into this table when a user creates a connection rule for a flow using connector tag.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payconnectedflows-16732.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payconnectedflows-16732.html)

## Primary Key

| Name | Columns |
|------|----------|
| pay_connected_flows_PK | CONNECTED_FLOW_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONNECTED_FLOW_ID | NUMBER |  | 18 | Yes | CONNECTED_FLOW_ID |
| BASE_FLOW_ID | NUMBER |  | 18 | Yes | BASE_FLOW_ID |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | SOURCE_FLOW_ID |
| CONNECTOR_TAG | VARCHAR2 | 200 |  |  | CONNECTOR_TAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| pay_connected_flows_U1 | Unique | Default | CONNECTED_FLOW_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
