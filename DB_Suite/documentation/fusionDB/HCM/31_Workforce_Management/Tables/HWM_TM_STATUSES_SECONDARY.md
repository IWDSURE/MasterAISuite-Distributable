# HWM_TM_STATUSES_SECONDARY

Secondary Statuses of a time record or time record group within the workforce management repository.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusessecondary-23866.html#hwmtmstatusessecondary-23866](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmstatusessecondary-23866.html#hwmtmstatusessecondary-23866)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_STATUSES_SECONDARY_PK | STATUS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATUS_ID | NUMBER |  | 18 | Yes | STATUS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE_ID |
| TM_BLDG_BLK_ID | NUMBER |  | 18 |  | TM_BLDG_BLK_ID |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 |  | TM_BLDG_BLK_VERSION |
| DATE_FROM | TIMESTAMP |  |  |  | DATE_FROM |
| DATE_TO | TIMESTAMP |  |  |  | DATE_TO |
| TM_STATUS_DEF_ID | NUMBER |  | 18 |  | TM_STATUS_DEF_ID |
| STATUS_VALUE | VARCHAR2 | 30 |  |  | STATUS_VALUE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LDG_OR_BUI_ID | NUMBER |  | 18 |  | LDG_OR_BUI_ID |
| PART_DATE | TIMESTAMP |  |  |  | PART_DATE |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | PART_GRP_TYPE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_STATUSES_SECONDARY_N1 | Non Unique | Default | TM_BLDG_BLK_ID, TM_BLDG_BLK_VERSION, TM_STATUS_DEF_ID, STATUS_VALUE, DATE_FROM, DATE_TO, ENTERPRISE_ID |
| HWM_TM_STATUSES_SECONDARY_N2 | Non Unique | Default | STATUS_VALUE, TM_STATUS_DEF_ID, LDG_OR_BUI_ID, ENTERPRISE_ID, DATE_TO, DATE_FROM, TM_BLDG_BLK_ID, TM_BLDG_BLK_VERSION |
| HWM_TM_STATUSES_SECONDARY_U1 | Unique | Default | STATUS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
