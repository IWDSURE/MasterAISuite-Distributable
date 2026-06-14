# HRC_DL_FILE_KEYS_INFO

This table holds data for Each KEY present in a given METADATA line. Holds key information for LOCAL/PARENT/FK attributes

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfilekeysinfo-31163.html#hrcdlfilekeysinfo-31163](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfilekeysinfo-31163.html#hrcdlfilekeysinfo-31163)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_FILE_KEYS_INFO_PK | KEY_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEY_INFO_ID | NUMBER |  | 18 | Yes | KEY_INFO_ID |
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| KEY_RESOLUTION_HINT | VARCHAR2 | 50 |  | Yes | KEY_RESOLUTION_HINT |
| VO_ATTRIBUTE_MAPPING_ID | NUMBER |  | 18 | Yes | VO_ATTRIBUTE_MAPPING_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_FILE_KEYS_INFO_F1 | Non Unique | Default | HEADER_ID |
| HRC_DL_FILE_KEYS_INFO_F2 | Non Unique | Default | VO_ATTRIBUTE_MAPPING_ID |
| HRC_DL_FILE_KEYS_INFO_U1 | Unique | Default | KEY_INFO_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
