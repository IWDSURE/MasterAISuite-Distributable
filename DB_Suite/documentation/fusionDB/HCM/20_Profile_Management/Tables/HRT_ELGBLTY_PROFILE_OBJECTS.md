# HRT_ELGBLTY_PROFILE_OBJECTS

Stores the linkage between templates/document periods and eligibility profiles.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtelgbltyprofileobjects-12006.html#hrtelgbltyprofileobjects-12006](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtelgbltyprofileobjects-12006.html#hrtelgbltyprofileobjects-12006)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_ELGBLTY_PROFILE_OBJECT_PK | ELGBLTY_PROFILE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELGBLTY_PROFILE_OBJECT_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Different objects which will be attached to eligibility profiles. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Primary key of corresponding object type. |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIGY_PRFL |
| REQUIRED_FLAG | VARCHAR2 | 1 |  | Yes | REQUIRED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_ELGBLTY_PROFILE_OBJECTS_PK | Unique | Default | ELGBLTY_PROFILE_OBJECT_ID |
| HRT_ELGBLTY_PROFILE_OBJECTS_U1 | Unique | Default | OBJECT_ID, OBJECT_TYPE, ELIGY_PRFL_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
