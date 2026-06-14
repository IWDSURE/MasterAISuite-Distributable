# HRC_DL_VO_USER_KEY_ATTRS

HRC_DL_VO_USER_KEY_ATTRS is used to record information for the user keys that correspond to any surrogate keys that have been mapped for a View Object.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvouserkeyattrs-29683.html#hrcdlvouserkeyattrs-29683](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvouserkeyattrs-29683.html#hrcdlvouserkeyattrs-29683)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_VO_USER_KEY_ATTRS_PK | VO_USER_KEY_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_USER_KEY_ATTR_ID | NUMBER |  | 18 | Yes | VO_USER_KEY_ATTR_ID |
| VO_ATTRIBUTE_MAPPING_ID | NUMBER |  | 18 | Yes | VO_ATTRIBUTE_MAPPING_ID |
| VO_USER_KEY_MAPPING_HASH | VARCHAR2 | 100 |  | Yes | VO_USER_KEY_MAPPING_HASH |
| KEY_LIST_INDEX | NUMBER |  | 2 | Yes | The index of the User Key List for this UK_STAGE_COLUMN_NAME mapping |
| UK_STAGE_COLUMN_NAME | VARCHAR2 | 100 |  | Yes | The TRANSFER specific User Key stage column name mapping for the User Key List indicated by the KEY_LIST_INDEX |
| LOCAL_ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | LOCAL_ATTRIBUTE_NAME |
| REF_VO_ATTRIBUTE_NAME | VARCHAR2 | 100 |  |  | REF_VO_ATTRIBUTE_NAME |
| REF_COLUMN_NAME | VARCHAR2 | 100 |  |  | REF_COLUMN_NAME |
| REF_TABLE_NAME | VARCHAR2 | 100 |  |  | REF_TABLE_NAME |
| PARENT_REF_VO_ATTR_NAME | VARCHAR2 | 100 |  |  | PARENT_REF_VO_ATTR_NAME |
| UK_QUERY_TEXT | VARCHAR2 | 4000 |  |  | Stores the User Key Query for a given user key. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| KEY_LIST_INDEX_POSITION | NUMBER |  | 2 |  | The attribute's position within the user key. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_USER_KEY_ATTRS_U1 | Unique | Default | VO_USER_KEY_ATTR_ID |
| HRC_DL_VO_USER_KEY_ATTRS_U2 | Unique | Default | VO_ATTRIBUTE_MAPPING_ID, VO_USER_KEY_MAPPING_HASH |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
