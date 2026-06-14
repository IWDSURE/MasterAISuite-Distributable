# HRC_DL_VO_TABLES

HRC_DL_VO_TABLES is used to record the Table Name mapped to the Business Object VO and the annotations defined in the VO. These tables will be used later to perform the gather statistics during HDL Load process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvotables-29681.html#hrcdlvotables-29681](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvotables-29681.html#hrcdlvotables-29681)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_VO_TABLES_PK | VO_TABLE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_TABLE_ID | NUMBER |  | 18 | Yes | Surroage ID for the current table |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO Mapping ID from HRC_DL_VO_MAPS |
| TABLE_NAME | VARCHAR2 | 30 |  | Yes | Table Name for which gather statistics is required. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise ID for applying the VPD policy |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_TABLES_PK | Unique | Default | VO_TABLE_ID |
| HRC_DL_VO_TABLES_U1 | Unique | Default | VO_MAPPING_ID, TABLE_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
