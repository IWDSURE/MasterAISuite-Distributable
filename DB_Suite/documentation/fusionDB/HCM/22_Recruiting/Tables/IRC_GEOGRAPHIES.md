# IRC_GEOGRAPHIES

This table contains location related data. The values stored in this table may come from different tables like hz_geography, irc_geo_coordinates etc

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographies-8935.html#ircgeographies-8935](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographies-8935.html#ircgeographies-8935)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEOGRAPHIES_PK | IRC_GEOGRAPHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IRC_GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System Generated. |
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to HZ_GEOGRAPHIES table for generating the FQN.  Reference the geography_id in HZ_GEOGRAPHY_IDENTIFIERS to create the FQN alternates. |
| LATITUDE | NUMBER |  |  |  | Used to store Latitude  Information for the Geography for Spatial Proximity and containment purposes. |
| LONGITUDE | NUMBER |  |  |  | Used to store Longitude Information for the Geography for Spatial Proximity and containment purposes. |
| WEIGHT | NUMBER |  |  |  | A numeric value used to rank the relevance of search results. |
| CITY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| STATE_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to  the element in HZ_GEOGRAPHIES table. |
| COUNTRY_ID | NUMBER |  | 18 |  | Foreign key to the GEOGRAPHY_ELEMENT1_ID referencing the country Id in HZ_GEOGRAPHIES table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEOGRAPHIES_N1 | Non Unique | Default | COUNTRY_ID, STATE_ID |
| IRC_GEOGRAPHIES_PK | Unique | Default | IRC_GEOGRAPHY_ID |
| IRC_GEOGRAPHIES_U1 | Unique | Default | GEOGRAPHY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
