# HRT_RATING_DISTRIBUTIONS

This table contains the rating distribution for a specific rating level.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingdistributions-12122.html#hrtratingdistributions-12122](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingdistributions-12122.html#hrtratingdistributions-12122)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_RATING_DISTRIBUTIONS_PK | RATING_DISTRIBUTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATING_DISTRIBUTION_ID | NUMBER |  | 18 | Yes | Unique identifier for rating distribution |
| OBJ_RATING_DIST_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_OBJ_RATING_DIST_B |
| RATING_LEVEL_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_RATING_LEVELS_B |
| DISTRIBUTION_PCT | NUMBER |  | 5 | Yes | Distribution percentage for the rating level |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRT_RATING_DISTRIBUTIONS_N1 | Non Unique | Default | OBJ_RATING_DIST_ID | Obsolete |
| HRT_RATING_DISTRIBUTIONS_PK | Unique | Default | RATING_DISTRIBUTION_ID |  |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
