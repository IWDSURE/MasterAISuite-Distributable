# HRQ_SUBSCRIBER_ROLE_MAPS

Table storing role access information for a subscriber.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqsubscriberrolemaps-25579.html#hrqsubscriberrolemaps-25579](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqsubscriberrolemaps-25579.html#hrqsubscriberrolemaps-25579)

## Primary Key

| Name | Columns |
|------|----------|
| hrq_subscriber_role_maps_PK | SUBSCRIBER_ROLE_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIBER_ROLE_MAP_ID | NUMBER |  | 18 | Yes | Unique identifier for a role configured for a subscriber. System generated id. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | Identifies the subscriber for the role map. |
| ROLE_ID | NUMBER |  | 18 | Yes | Identifies the role for the role map. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_SUBSCRIBER_ROLE_MAPS_N1 | Non Unique | Default | ROLE_ID, SUBSCRIBER_ID |
| HRQ_SUBSCRIBER_ROLE_MAPS_N2 | Non Unique | Default | SUBSCRIBER_ID |
| HRQ_SUBSCRIBER_ROLE_MAPS_PK | Unique | Default | SUBSCRIBER_ROLE_MAP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
