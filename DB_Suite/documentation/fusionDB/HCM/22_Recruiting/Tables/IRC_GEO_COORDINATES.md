# IRC_GEO_COORDINATES

Table for Recruiting Geography Coordinates

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeocoordinates-14676.html#ircgeocoordinates-14676](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeocoordinates-14676.html#ircgeocoordinates-14676)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEO_COORDINATES_PK | GEO_COORDINATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GEO_COORDINATE_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Foreign key to HZ_GEOGRAPHIES table. |
| LONGITUDE | NUMBER |  |  |  | Used to store Longitude Information for the Geography for Spatial Proximity and containment purposes |
| LATITUDE | NUMBER |  |  |  | Used to store Latitude Information for the Geography for Spatial Proximity and containment purposes |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEO_COORDINATES_FK1 | Unique | Default | GEOGRAPHY_ID |
| IRC_GEO_COORDINATES_PK | Unique | Default | GEO_COORDINATE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
