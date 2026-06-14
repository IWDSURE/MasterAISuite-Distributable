# CMP_ADDRESS_ZONES

Address Zones contains the zones that each address maps to based on the geography naming reference data.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpaddresszones-25611.html#cmpaddresszones-25611](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpaddresszones-25611.html#cmpaddresszones-25611)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_ADDRESS_ZONES_PK | ADDRESS_ZONE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADDRESS_ZONE_ID | NUMBER |  | 18 | Yes | Address Zone Id. |
| ZONE_TYPE_FOR | VARCHAR2 | 30 |  |  | Zone Type For. |
| ADDRESS_ID | NUMBER |  | 18 |  | Address Id. |
| ADDRESS_TYPE | VARCHAR2 | 30 |  |  | Address Type. |
| START_DATE | DATE |  |  |  | Start Date. |
| END_DATE | DATE |  |  |  | End Date. |
| PERSON_ID | NUMBER |  | 18 |  | Person Id. |
| LOCATION_ID | NUMBER |  | 18 |  | Location Id. |
| GEOGRAPHY_TYPE_ID | NUMBER |  | 18 |  | Geography Type Id. |
| GEOGRAPHY_ID | NUMBER |  | 18 |  | Geography Id. |
| GEOGRAPHY_NAME | VARCHAR2 | 360 |  |  | Geography Name. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ZONE_START_DATE | DATE |  |  |  | Start date of Zone |
| ZONE_END_DATE | DATE |  |  |  | End date of Zone |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_ADDRESS_ZONES_N1 | Non Unique | Default | PERSON_ID, ADDRESS_ID, GEOGRAPHY_TYPE_ID, ADDRESS_TYPE, ZONE_TYPE_FOR |
| CMP_ADDRESS_ZONES_N2 | Non Unique | Default | LOCATION_ID, ADDRESS_ID, GEOGRAPHY_TYPE_ID, ADDRESS_TYPE, ZONE_TYPE_FOR |
| CMP_ADDRESS_ZONES_PK | Unique | Default | ADDRESS_ZONE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
