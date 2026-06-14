# WLF_EVENT_SOURCES

Table to store learning item event sources.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsources-12421.html#wlfeventsources-12421](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsources-12421.html#wlfeventsources-12421)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EVENT_SOURCES_PK | EVENT_SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_SOURCE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| SOURCE_INFO | VARCHAR2 | 240 |  |  | To indicate the source for various events created in Fusion Learn Application. |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | To indicate the source for various events created in Fusion Learn Application. |
| SOURCE_ID | NUMBER |  | 18 |  | To indicate the source for various events created in Fusion Learn Application. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EVENT_SOURCES_N1 | Non Unique | Default | EVENT_ID |
| WLF_EVENT_SOURCES_U1 | Unique | Default | EVENT_SOURCE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
