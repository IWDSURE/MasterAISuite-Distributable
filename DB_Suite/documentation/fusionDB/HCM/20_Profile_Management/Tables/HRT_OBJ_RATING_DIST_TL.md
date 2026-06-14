# HRT_OBJ_RATING_DIST_TL

This is the translated  table that contains the name and description for the target rating distribution for an object.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtobjratingdisttl-22649.html#hrtobjratingdisttl-22649](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtobjratingdisttl-22649.html#hrtobjratingdisttl-22649)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_OBJ_RATING_DIST_TL_PK | OBJ_RATING_DIST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJ_RATING_DIST_ID | NUMBER |  | 18 | Yes | Unique identifier for object rating distribution |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| RATING_DIST_NAME | VARCHAR2 | 240 |  | Yes | Name of object rating distribution |
| RATING_DIST_DESCR | VARCHAR2 | 2000 |  |  | Description of object rating distribution |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_OBJ_RATING_DIST_TL_PK | Unique | Default | OBJ_RATING_DIST_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
