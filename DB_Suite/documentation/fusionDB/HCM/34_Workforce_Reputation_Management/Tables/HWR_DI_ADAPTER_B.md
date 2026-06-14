# HWR_DI_ADAPTER_B

The adapter table stores serialized adapter objects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiadapterb-14266.html#hwrdiadapterb-14266](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiadapterb-14266.html#hwrdiadapterb-14266)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_ADAPTER_B_PK | ADAPTER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADAPTER_ID | NUMBER |  | 18 | Yes | This is the primary key for the adapter table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. |
| ADAPTER_NAME | VARCHAR2 | 256 |  |  | This is the human readable representation of this adapter. |
| UUID | VARCHAR2 | 64 |  |  | This is the UUID identifying the adapter. |
| ADAPTER_QUERY | CLOB |  |  |  | This is the serialized query of the adapter. |
| SOURCE_OBJECT_DEF | NUMBER |  | 18 |  | This is the source object definition of the adapter. |
| TARGET_OBJECT_DEF | NUMBER |  | 18 |  | This is the target object definition of the adapter. |
| QUERY_NAME | VARCHAR2 | 256 |  |  | This is the human readable name of the query of the adapter. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_ADAPTER_B_N1 | Non Unique | Default | SOURCE_OBJECT_DEF |
| HWR_DI_ADAPTER_B_N2 | Non Unique | Default | TARGET_OBJECT_DEF |
| HWR_DI_ADAPTER_B_U1 | Unique | Default | ADAPTER_ID |
| HWR_DI_ADAPTER_B_U2 | Unique | Default | UUID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
