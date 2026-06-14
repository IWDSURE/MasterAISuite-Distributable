# IRC_GEOGRAPHY_LOCATIONS

Extension Table for IRC_GEOGRAPHIES.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographylocations-16727.html#ircgeographylocations-16727](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographylocations-16727.html#ircgeographylocations-16727)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GEOGRAPHY_LOCATIONS_PK | IRC_GEOGRAPHY_ID, LANGUAGE_CODE, FQN_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IRC_GEOGRAPHY_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. Foreign key to IRC_GEOGRAPHIES table. |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Part of the Primary Key for this table. Indicates the code of the language into which the contents of the translatable columns are translated. |
| FQN | VARCHAR2 | 4000 |  |  | Fully Qualified Name of a location.  This is the primary location. |
| FQN_TYPE | VARCHAR2 | 32 |  | Yes | Identifies the type of FQN whether it is primary or alternate. |
| CITY | VARCHAR2 | 360 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| STATE | VARCHAR2 | 360 |  |  | Element based on hierarchy structure from HZ_GEOGRAPHIES table. |
| COUNTRY | VARCHAR2 | 360 |  |  | The country name from the FND_TERRITORIES table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GEOGRAPHY_LOCATIONS_PK | Unique | Default | IRC_GEOGRAPHY_ID, LANGUAGE_CODE, FQN_TYPE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
