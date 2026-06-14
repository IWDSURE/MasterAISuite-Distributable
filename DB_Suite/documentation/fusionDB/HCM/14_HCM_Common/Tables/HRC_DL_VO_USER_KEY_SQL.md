# HRC_DL_VO_USER_KEY_SQL

This table is used to store the additional import query for each and every object.

Data will not be available for following conditions :

1) transient objects
2) translation objects

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvouserkeysql-14389.html#hrcdlvouserkeysql-14389](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvouserkeysql-14389.html#hrcdlvouserkeysql-14389)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_VO_USER_KEY_SQL_PK | VO_USER_KEY_SQL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_USER_KEY_SQL_ID | NUMBER |  | 18 | Yes | Primary Key for the table. Unique reference for each KEY_LIST_INDEX |
| VO_ATTRIBUTE_MAPPING_ID | NUMBER |  | 18 | Yes | Immediate Parent reference from HRC_DL_VO_ATTR_MAPS |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | Additional VO_MAP table reference for import usage |
| IMPORT_QUERY_TEXT | VARCHAR2 | 4000 |  |  | Import Query text column will hold the complete Import Query. 

SurrogateId an be retrieved for given User Key values. |
| KEY_LIST_INDEX | NUMBER |  | 2 | Yes | KEY_LIST_INDEX- Values can be 0,1,2 etc depending on the number of User Key Sets supported for Current Object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID - Attirbute supported for Multi tenancy |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_USER_KEY_SQL_N1 | Non Unique | Default | VO_MAPPING_ID |
| HRC_DL_VO_USER_KEY_SQL_U1 | Unique | Default | VO_USER_KEY_SQL_ID |
| HRC_DL_VO_USER_KEY_SQL_U2 | Unique | Default | VO_ATTRIBUTE_MAPPING_ID, KEY_LIST_INDEX |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
