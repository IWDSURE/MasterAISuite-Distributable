# HWM_TCAT_USAGES

Time categories for a time record or time record group within the workforce management repository.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatusages-25669.html#hwmtcatusages-25669](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcatusages-25669.html#hwmtcatusages-25669)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCAT_USAGES_PK | TCAT_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCAT_USAGE_ID | NUMBER |  | 18 | Yes | TCAT_USAGE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| TCAT_ID | NUMBER |  | 18 |  | The time category for which the time building block is related |
| TM_BLDG_BLK_ID | NUMBER |  | 18 |  | TM_BLDG_BLK_ID |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 |  | TM_BLDG_BLK_VERSION |
| BLDG_BLK_TYPE | VARCHAR2 | 32 |  |  | BLDG_BLK_TYPE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| RESOURCE_ID | NUMBER |  | 18 |  | RESOURCE_ID |
| START_TIME | TIMESTAMP |  |  |  | START_TIME |
| STOP_TIME | TIMESTAMP |  |  |  | STOP_TIME |
| SUBRESOURCE_ID | NUMBER |  | 18 |  | SUBRESOURCE_ID |
| AREA1 | NUMBER |  | 18 |  | AREA1 |
| AREA2 | NUMBER |  | 18 |  | AREA2 |
| AREA3 | NUMBER |  | 18 |  | AREA3 |
| AREA4 | NUMBER |  | 18 |  | AREA4 |
| REF_DATE | DATE |  |  |  | Reference Date of the Time Record |
| ACTUAL_DATE | DATE |  |  |  | Actual Date of the Time Record |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCAT_USAGES_N1 | Non Unique | Default | TM_BLDG_BLK_ID, TM_BLDG_BLK_VERSION |
| HWM_TCAT_USAGES_N2 | Non Unique | Default | RESOURCE_ID, REF_DATE, TCAT_ID, SUBRESOURCE_ID |
| HWM_TCAT_USAGES_N3 | Non Unique | Default | RESOURCE_ID, ACTUAL_DATE, TCAT_ID, SUBRESOURCE_ID |
| HWM_TCAT_USAGES_U1 | Unique | FUSION_TS_TX_IDX | TCAT_USAGE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
