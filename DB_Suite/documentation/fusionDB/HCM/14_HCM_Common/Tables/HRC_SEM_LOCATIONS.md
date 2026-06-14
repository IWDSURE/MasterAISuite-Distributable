# HRC_SEM_LOCATIONS

This table is to store the address

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocations-29920.html#hrcsemlocations-29920](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemlocations-29920.html#hrcsemlocations-29920)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_LOCATIONS_PK | LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LOCATION_ID | NUMBER |  | 18 | Yes | This is the primary key of the location table. |  |
| URI | VARCHAR2 | 1024 |  | Yes | This column contains the URI of the location. |  |
| GEOGRAPHY_ID | VARCHAR2 | 80 |  | Yes | This columns is for the TCA Geography ID of the location. |  |
| COUNTRY_ID | VARCHAR2 | 80 |  | Yes | This is the country id of the address. |  |
| STATE_ID | VARCHAR2 | 80 |  |  | This is the state id of the address. |  |
| CITY_ID | VARCHAR2 | 80 |  |  | This is the city id of the address. |  |
| POSTALCODE | VARCHAR2 | 80 |  |  | This is the postal code of the address. | Obsolete |
| LEAF_NAME | VARCHAR2 | 1024 |  |  | This indicates the leaf name of the location. | Obsolete |
| FQN | VARCHAR2 | 4000 |  |  | This column indicates the fully qualified name of the location. |  |
| LATITUDE | VARCHAR2 | 80 |  |  | This is the lattitude of the location. |  |
| LONGITUDE | VARCHAR2 | 80 |  |  | This is the longitude of the location. |  |
| STATUS | NUMBER |  | 8 |  | This column contains the status of the indexing event. |  |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in indexing event. |  |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |  |
| INDEXING_EVENT_ID | NUMBER |  | 18 |  | This column contains the indexing event id. | Obsolete |
| BATCH_ID | NUMBER |  | 18 |  | This column contains the batch id. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRC_SEM_LOCATIONS_N1 | Non Unique | FUSION_TS_TX_DATA | INDEXING_EVENT_ID | Obsolete |
| HRC_SEM_LOCATIONS_N2 | Non Unique | FUSION_TS_TX_DATA | STATE_ID |  |
| HRC_SEM_LOCATIONS_N3 | Non Unique | FUSION_TS_TX_DATA | CITY_ID | Obsolete |
| HRC_SEM_LOCATIONS_N4 | Non Unique | FUSION_TS_TX_DATA | POSTALCODE | Obsolete |
| HRC_SEM_LOCATIONS_N5 | Non Unique | FUSION_TS_TX_DATA | GEOGRAPHY_ID |  |
| HRC_SEM_LOCATIONS_N6 | Non Unique | FUSION_TS_TX_DATA | FQN |  |
| HRC_SEM_LOCATIONS_N7 | Non Unique | FUSION_TS_TX_DATA | COUNTRY_ID |  |
| HRC_SEM_LOCATIONS_N8 | Non Unique | Default | BATCH_ID |  |
| HRC_SEM_LOCATIONS_N9 | Non Unique | Default | LAST_UPDATE_DATE |  |
| HRC_SEM_LOCATIONS_U1 | Unique | FUSION_TS_TX_DATA | LOCATION_ID |  |
| HRC_SEM_LOCATIONS_U2 | Unique | FUSION_TS_TX_DATA | URI |  |
| HRC_SEM_LOCATIONS_U3 | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LOCATION_ID | Obsolete |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
