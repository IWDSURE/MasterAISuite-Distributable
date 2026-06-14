# IRC_CANDIDATES_DN

This table stores candidate denormalized information which will be used for Indexing.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidatesdn-31588.html#irccandidatesdn-31588](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandidatesdn-31588.html#irccandidatesdn-31588)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CANDIDATES_DN_PK | PERSON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_ID | NUMBER |  | 18 | Yes | Primary key of the table and also foreign Key to PER_PERSONS. |
| REHIRE_RECOMMENDATION | VARCHAR2 | 30 |  |  | Indicates whether candidate is recommendated for being rehired. This is a denormalized column derived from PER_PERIODS_OF_SERVICE.REHIRE_RECOMMENDATION. |
| WORKEXP_MONTHS | NUMBER |  | 18 |  | This indicates the cumulative months of experience. |
| LATEST_MKT_EMAIL_DATE | DATE |  |  |  | Stores the date and time when last recruiting marketing email was sent |
| ADDRESS_GEOGRAPHY_ID | NUMBER |  | 18 |  | Foreign key to HZ_GEOGRAPHIES table for generating the FQN. Reference the geography_id in HZ_GEOGRAPHY_IDENTIFIERS to create the FQN alternates. |
| ADDRESS_COUNTRY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_STATE_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_CITY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_COUNTY_ID | NUMBER |  | 18 |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_POSTAL_CODE | VARCHAR2 | 30 |  |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Element based on hierarchy structure and a foreign key to the element in HZ_GEOGRAPHIES table. |
| ADDRESS_LATITUDE | NUMBER |  |  |  | Used to store Latitude  Information for the Geography for Spatial Proximity and containment purposes. |
| ADDRESS_LONGITUDE | NUMBER |  |  |  | Used to store Longitude Information for the Geography for Spatial Proximity and containment purposes. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CANDIDATES_DN_FK1 | Non Unique | Default | ADDRESS_GEOGRAPHY_ID |
| IRC_CANDIDATES_DN_PK | Unique | Default | PERSON_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
