# HWM_TM_REP_ATRB_USAGES

An attribute usage defines which attributes are used by which time records and time record groups in the repository.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepatrbusages-13835.html#hwmtmrepatrbusages-13835](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepatrbusages-13835.html#hwmtmrepatrbusages-13835)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REP_ATRB_USAGES_PK | TM_REP_ATRB_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REP_ATRB_USAGE_ID | NUMBER |  | 18 | Yes | Primary key of the Time Attribute Usages |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_REP_ATRB_ID | NUMBER |  | 18 | Yes | The primary key of the Time Attributes. |
| USAGES_TYPE | VARCHAR2 | 30 |  |  | USAGES_TYPE |
| USAGES_SOURCE_ID | NUMBER |  | 18 |  | TM_REC_GRP_ID |
| USAGES_SOURCE_VERSION | NUMBER |  | 9 |  | TM_REC_GRP_VERSION |
| USAGES_SOURCE_GRP_LEVEL | NUMBER |  |  |  | Source level -  from HWM_GRP_TYPE . GRP_LEVEL |
| DATA_SET_ID | NUMBER |  | 18 |  | Data set id |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | Indicates if this is the most recent version of the time building block. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_TM_REP_ATRB_USAGES_N1 | Non Unique | Default | USAGES_SOURCE_ID |  |
| HWM_TM_REP_ATRB_USAGES_N2 | Non Unique | Default | TM_REP_ATRB_ID, USAGES_SOURCE_ID, LATEST_VERSION, ENTERPRISE_ID |  |
| HWM_TM_REP_ATRB_USAGES_N3 | Non Unique | Default | ENTERPRISE_ID, LATEST_VERSION, TM_REP_ATRB_ID, USAGES_SOURCE_ID | Obsolete |
| HWM_TM_REP_ATRB_USAGES_N2 | Non Unique | Default | TM_REP_ATRB_ID | Obsolete |
| HWM_TM_REP_ATRB_USAGES_PK | Unique | FUSION_TS_TX_DATA | TM_REP_ATRB_USAGE_ID |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
