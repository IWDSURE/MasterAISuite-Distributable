# BEN_BAND_DETAILS

BEN_BAND_DETAILS defines band, percentage pay info.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbanddetails-14505.html#benbanddetails-14505](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbanddetails-14505.html#benbanddetails-14505)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BAND_DETAILS_PK | BAND_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAND_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAND_ENTITLEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BAND_ABS_ENTITLEMENT.BAND_ENTITLEMENT_ID. |
| BAND_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | Band Code as in lookup. |
| BAND_SEQUENCE | NUMBER |  | 18 | Yes | Band Sequence used in processing entitlements. |
| BAND_NAME | VARCHAR2 | 30 |  |  | Identifies name of the band. |
| ELIGIBLE_PAY_PERCENT | NUMBER |  |  | Yes | Defines the eligible pay percentage for each band. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BAND_DETAILS_PK | Unique | FUSION_TS_TX_DATA | BAND_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
