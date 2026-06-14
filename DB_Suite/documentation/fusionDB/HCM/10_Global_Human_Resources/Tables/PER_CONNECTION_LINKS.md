# PER_CONNECTION_LINKS

This table contains information about the person connections.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perconnectionlinks-3626.html#perconnectionlinks-3626](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perconnectionlinks-3626.html#perconnectionlinks-3626)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CONNECTION_LINKS_PK | CONNECTION_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONNECTION_LINK_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies a connection. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person against whom has  the connection. |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment against whom has  the connections. |
| CONNECT_TYPE | VARCHAR2 | 40 |  |  | Connection type |
| CONNECT_PERSON_ID | NUMBER |  | 18 |  | Person of the person connected to. |
| CONNECT_ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment of the person connected to. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CONNECTION_LINKS_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID, ASSIGNMENT_ID, CONNECT_TYPE |
| PER_CONNECTION_LINKS_PK | Unique | FUSION_TS_TX_DATA | CONNECTION_LINK_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
