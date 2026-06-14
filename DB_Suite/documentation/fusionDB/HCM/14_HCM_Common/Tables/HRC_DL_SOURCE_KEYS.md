# HRC_DL_SOURCE_KEYS

HCM Data Loader Source References

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsourcekeys-20350.html#hrcdlsourcekeys-20350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlsourcekeys-20350.html#hrcdlsourcekeys-20350)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_SOURCE_KEYS_PK | SOURCE_KEY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_KEY_ID | NUMBER |  | 18 | Yes | SOURCE_KEY_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SOURCE_TABLE_NAME | VARCHAR2 | 200 |  |  | SOURCE_TABLE_NAME |
| SOURCE_REF_NAME001 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME001 |
| SOURCE_REF_NAME002 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME002 |
| SOURCE_REF_NAME003 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME003 |
| SOURCE_REF_NAME004 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME004 |
| SOURCE_REF_NAME005 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME005 |
| SOURCE_REF_NAME006 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME006 |
| SOURCE_REF_NAME007 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME007 |
| SOURCE_REF_NAME008 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME008 |
| SOURCE_REF_NAME009 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME009 |
| SOURCE_REF_NAME010 | VARCHAR2 | 200 |  |  | SOURCE_KEY_ATTRIBUTE_NAME010 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_SOURCE_KEYS_N1 | Non Unique | Default | BUSINESS_OBJECT_ID, DATA_SET_BUS_OBJ_ID |
| HRC_DL_SOURCE_KEYS_PK | Unique | Default | SOURCE_KEY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
