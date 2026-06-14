# IRC_JA_PREF_LOCATIONS

This table contains the Preferred Locations Information for submissions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjapreflocations-30757.html#ircjapreflocations-30757](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjapreflocations-30757.html#ircjapreflocations-30757)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_PREF_LOCATIONS_PK | JA_PREF_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_PREF_LOCATION_ID | NUMBER |  | 18 | Yes | Primary key for this table. System Generated. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | This column would be the foriegn key for IRC_SUBMISSIONS Table. It would store the submission ids of the candidates. |
| LOCATION_ID | NUMBER |  | 18 | Yes | This column will store the preferred location id of the submissions. The location id will be generic and it could be any one of work locations or posting locations. |
| LOCATION_TYPE | VARCHAR2 | 1 |  | Yes | This column stores what type of location it is. It could possibly have only two values , either 'W' or 'P'. 
'W' stands for representing a work location.
'P' stands for representing a posting location. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_PREF_LOCATIONS_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_JA_PREF_LOCATIONS_FK2 | Non Unique | Default | LOCATION_ID |
| IRC_JA_PREF_LOCATIONS_U1 | Unique | Default | JA_PREF_LOCATION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
