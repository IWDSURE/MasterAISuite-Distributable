# HRC_DL_INTEGRATION_UK_DATA

HRC_DL_INTEGRATION_UK_DATA table holds the values of the user key attributes for each surrogate id of an integration enabled entity instance, that has an entry in HRC_INTEGRATION_KEY_MAP

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlintegrationukdata-8350.html#hrcdlintegrationukdata-8350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlintegrationukdata-8350.html#hrcdlintegrationukdata-8350)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_INTEGRATION_UK_DAT_PK | USER_KEY_DATA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| USER_KEY_DATA_ID | NUMBER |  | 18 | Yes | USER_KEY_DATA_ID |
| SURROGATE_ID | NUMBER |  | 18 | Yes | SURROGATE_ID |
| OBJECT_NAME | VARCHAR2 | 256 |  | Yes | OBJECT_NAME |
| USER_KEY_NAME | VARCHAR2 | 256 |  | Yes | USER_KEY_NAME |
| USER_KEY_VALUE | VARCHAR2 | 500 |  |  | USER_KEY_VALUE |
| USER_KEY_VALUE_SECURE | VARCHAR2 | 500 |  |  | USER_KEY_VALUE_SECURE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_INTEGRATION_UK_DATA_PK | Unique | Default | USER_KEY_DATA_ID |
| HRC_DL_INTEGRATION_UK_DAT_U1 | Unique | Default | OBJECT_NAME, SURROGATE_ID, USER_KEY_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
