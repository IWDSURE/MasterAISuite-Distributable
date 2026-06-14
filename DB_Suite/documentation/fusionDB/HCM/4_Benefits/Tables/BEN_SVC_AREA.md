# BEN_SVC_AREA

Service area definition. Each service area is made up of one or more postal zip ranges.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bensvcarea-21277.html#bensvcarea-21277](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bensvcarea-21277.html#bensvcarea-21277)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_SVC_AREA_PK | SVC_AREA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SVC_AREA_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| START_DATE | DATE |  |  | Yes | Start date for the record validity. |
| END_DATE | DATE |  |  |  | End date for the record validity. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the service area. |
| ORG_UNIT_PRDCT | VARCHAR2 | 90 |  |  | The provider category of the service area. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_SVC_AREA_N1 | Non Unique | Default | UPPER("NAME") |
| BEN_SVC_AREA_PK | Unique | Default | SVC_AREA_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
