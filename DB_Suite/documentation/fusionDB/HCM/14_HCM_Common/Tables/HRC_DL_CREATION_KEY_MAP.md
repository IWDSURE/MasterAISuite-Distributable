# HRC_DL_CREATION_KEY_MAP

HRC_DL_CREATION_KEY_MAP table stores the Source Key to Fusion ID mapping for every new record created in Fusion VO tables, and helps keep track of all new records created in Fusion through Data Loader.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcreationkeymap-31003.html#hrcdlcreationkeymap-31003](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcreationkeymap-31003.html#hrcdlcreationkeymap-31003)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_CREATION_KEY_MAP_PK | DL_KEY_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DL_KEY_MAP_ID | NUMBER |  | 18 | Yes | DL_KEY_MAP_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 |  | DATA_SET_BUS_OBJ_ID |
| SOURCE_ID | VARCHAR2 | 2000 |  | Yes | SOURCE_ID |
| TARGET_ID | NUMBER |  | 18 | Yes | TARGET_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_NAME |
| SOURCE_OWNER | VARCHAR2 | 256 |  |  | SOURCE_OWNER |
| ACTION | VARCHAR2 | 20 |  |  | ACTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_CREATION_KEY_MAP_N1 | Non Unique | Default | BUSINESS_OBJECT_ID, TARGET_ID, ACTION |
| HRC_DL_CREATION_KEY_MAP_N2 | Non Unique | Default | BUSINESS_OBJECT_ID, SOURCE_OWNER, SOURCE_ID, ACTION |
| HRC_DL_CREATION_KEY_MAP_N3 | Non Unique | Default | DATA_SET_BUS_OBJ_ID, TARGET_ID |
| HRC_DL_CREATION_KEY_MAP_PK | Unique | Default | DL_KEY_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
