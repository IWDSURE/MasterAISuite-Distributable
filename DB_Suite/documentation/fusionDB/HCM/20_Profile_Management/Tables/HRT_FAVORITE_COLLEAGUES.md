# HRT_FAVORITE_COLLEAGUES

This table holds the person id's who are marked favorite for a given person.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfavoritecolleagues-29801.html#hrtfavoritecolleagues-29801](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfavoritecolleagues-29801.html#hrtfavoritecolleagues-29801)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_FAVORITE_COLLEAGUES_PK | PERSON_FAV_COLLEAGUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_FAV_COLLEAGUE_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PERSONS |
| FAVORITE_COLLEAGUE_ID | NUMBER |  | 18 | Yes | Person ID of a favorite colleague |
| PRIVACY_FLAG | VARCHAR2 | 30 |  |  | Flag to check if others have access to the favorite colleagues of a person |
| REQUEST_CONTEXT | VARCHAR2 | 30 |  |  | Requesting flow which is calling the favorite colleague flow |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_FAVORITE_COLLEAGUES_U1 | Unique | Default | PERSON_FAV_COLLEAGUE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
