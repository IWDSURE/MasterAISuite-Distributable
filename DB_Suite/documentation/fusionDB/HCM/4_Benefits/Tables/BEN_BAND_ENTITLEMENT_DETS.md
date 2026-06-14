# BEN_BAND_ENTITLEMENT_DETS

BEN_BAND_ENTITLEMENT_DETS defines entitled leave for each band.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbandentitlementdets-26530.html#benbandentitlementdets-26530](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbandentitlementdets-26530.html#benbandentitlementdets-26530)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BAND_ENTITLEMENT_DETS_PK | BAND_ENTITILEMENT_DET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAND_ENTITILEMENT_DET_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BAND_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BAND_DETAILS.BAND_ID. |
| BAND_ENTITLEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BAND_ABS_ENTITLEMENT.BAND_ENTITLEMENT_ID. |
| LOS_LOWER_BOUND | NUMBER |  |  | Yes | Length of service lower range. |
| LOS_UPPER_BOUND | NUMBER |  |  | Yes | Length of service upper range. |
| ENTITLED_LEAVE | NUMBER |  |  | Yes | Eligible leave. |
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
| BEN_BAND_ENTIT_DETS_PK | Unique | FUSION_TS_TX_DATA | BAND_ENTITILEMENT_DET_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
