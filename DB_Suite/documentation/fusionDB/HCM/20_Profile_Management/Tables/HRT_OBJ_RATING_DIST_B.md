# HRT_OBJ_RATING_DIST_B

This base table stores the target rating distribution for an object.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtobjratingdistb-4050.html#hrtobjratingdistb-4050](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtobjratingdistb-4050.html#hrtobjratingdistb-4050)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_OBJ_RATING_DIST_B_PK | OBJ_RATING_DIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJ_RATING_DIST_ID | NUMBER |  | 18 | Yes | Unique identifier for object rating distribution |
| OBJECT_ID | NUMBER |  | 18 | Yes | Object for which rating distribution is being defined |
| OBJECT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Object type for which rating distribution is being defined |
| RATING_MODEL_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_RATING_MODELS_B |
| DATE_FROM | DATE |  |  | Yes | Start date where rating distribution is valid for the object |
| DATE_TO | DATE |  |  |  | End date where rating distribution is no longer valid for the object |
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
| HRT_OBJ_RATING_DIST_B_N1 | Non Unique | Default | OBJECT_ID | Obsolete |
| HRT_OBJ_RATING_DIST_B_PK | Unique | Default | OBJ_RATING_DIST_ID |  |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
