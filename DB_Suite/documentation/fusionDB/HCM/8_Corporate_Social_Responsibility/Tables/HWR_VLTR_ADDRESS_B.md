# HWR_VLTR_ADDRESS_B

This table stores base address information

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltraddressb-21264.html#hwrvltraddressb-21264](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltraddressb-21264.html#hwrvltraddressb-21264)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_VLTR_ADDRESS_B_PK | ADDRESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADDRESS_ID | NUMBER |  | 18 | Yes | ADDRESS_ID |
| ADDRESS_TYPE | VARCHAR2 | 100 |  |  | ADDRESS_TYPE |
| GEOGRAPHY_KEY | VARCHAR2 | 1090 |  |  | GEOGRAPHY_KEY |
| ZIP | NUMBER |  | 10 |  | ZIP |
| ZIP_CODE | VARCHAR2 | 100 |  |  | ZIP_CODE |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |
| HCM_PERSON_ID | NUMBER |  | 18 |  | HCM_PERSON_ID |
| ENTITY_TYPE | VARCHAR2 | 100 |  |  | ENTITY_TYPE |
| LONGITUDE | NUMBER |  |  |  | Used to store Longitude Information for the Location for Spatial Proximity and containment purposes |
| LATITUDE | NUMBER |  |  |  | Used to store Latitude Information for the Location for Spatial Proximity and containment purposes |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_VLTR_ADDRESS_B_U1 | Unique | FUSION_TS_TX_IDX | ADDRESS_ID |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
