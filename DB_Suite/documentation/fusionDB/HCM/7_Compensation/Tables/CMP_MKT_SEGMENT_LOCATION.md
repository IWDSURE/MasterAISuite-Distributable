# CMP_MKT_SEGMENT_LOCATION

Stores Segment Location Mapping data in the database.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsegmentlocation-13201.html#cmpmktsegmentlocation-13201](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsegmentlocation-13201.html#cmpmktsegmentlocation-13201)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_SEGMENT_LOCATION_PK | SEGMENT_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEGMENT_LOCATION_ID | NUMBER |  | 18 | Yes | Primary Table Key |
| SEGMENT_ID | NUMBER |  | 18 | Yes | Foreign Table Key |
| LOCATION_ID | NUMBER |  | 18 | Yes | Location Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_SEGMENT_LOCATION_U1 | Unique | Default | SEGMENT_LOCATION_ID |
| CMP_MKT_SEGMENT_LOCATION_U2 | Unique | Default | SEGMENT_LOCATION_ID, LOCATION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
