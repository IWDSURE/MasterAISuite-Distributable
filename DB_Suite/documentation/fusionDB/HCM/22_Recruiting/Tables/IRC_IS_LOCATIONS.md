# IRC_IS_LOCATIONS

IRC_IS_LOCATIONS will contain all the interview scheduling locations.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircislocations-9256.html#ircislocations-9256](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircislocations-9256.html#ircislocations-9256)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_LOCATIONS_PK | SCHEDULE_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHEDULE_LOCATION_ID | NUMBER |  | 18 | Yes | The primary key for this table |
| LOCATION_CODE | VARCHAR2 | 240 |  |  | Unique identifier for locations |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign key to a location. (PER_LOCATIONS) |
| LOCATION_TYPE | VARCHAR2 | 32 |  |  | Lookup defined by ORA_IRC_IS_LOCATION_TYPE which can be an interview in person, through phone or through a web conference. |
| PHONE_COUNTRY_CODE_NUMBER | VARCHAR2 | 30 |  |  | Country code of the Interview Phone Number |
| PHONE_COUNTRY_CODE_ID | NUMBER |  | 18 |  | Foreign key to a phone country code. (HZ_PHONE_COUNTRY_CODES) |
| PHONE_AREA_CODE | VARCHAR2 | 30 |  |  | Area Code of the Interview Phone Number |
| PHONE_NUMBER | VARCHAR2 | 60 |  |  | Interview Phone Number |
| PHONE_NUMBER_EXT | VARCHAR2 | 60 |  |  | Interview Phone Number Extension |
| PHONE_NUMBER_PASSCODE | VARCHAR2 | 30 |  |  | The phone number passcode for the Interview Schedule. |
| WEB_CONFERENCE_LINK | VARCHAR2 | 4000 |  |  | The web conference link for the Interview Schedule. |
| LOCATION_DETAILS | CLOB |  |  |  | The location details for the Interview Schedule. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_LOCATIONS_FK1 | Non Unique | Default | LOCATION_ID |
| IRC_IS_LOCATIONS_FK2 | Non Unique | Default | PHONE_COUNTRY_CODE_ID |
| IRC_IS_LOCATIONS_PK | Unique | Default | SCHEDULE_LOCATION_ID |
| IRC_IS_LOCATIONS_U1 | Unique | Default | LOCATION_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
