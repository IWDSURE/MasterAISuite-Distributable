# HWM_TM_REC_GRP_USAGES

A time record associated with a particular time record group.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpusages-14294.html#hwmtmrecgrpusages-14294](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecgrpusages-14294.html#hwmtmrecgrpusages-14294)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_GRP_USAGES_PK | TM_REC_GRP_USAGES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_GRP_USAGES_ID | NUMBER |  | 18 | Yes | Primary key of the Time Attribute Usages |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TM_REC_VERSION | NUMBER |  | 9 | Yes | Foreign key to HWM_TM_BLDG_BLKS |
| TM_REC_ID | NUMBER |  | 18 | Yes | Foreign Key to HWM_TM_ATRBS |
| TM_REC_GRP_ID | NUMBER |  | 18 | Yes | Foreign key to HWM_TM_BLDG_BLKS |
| TM_REC_GRP_VERSION | NUMBER |  | 9 | Yes | TM_RECORD_GRP_VERSION |
| DATA_SET_ID | NUMBER |  | 18 |  | Data set id |
| LAYER_CODE | VARCHAR2 | 20 |  |  | LAYER_CODE |
| LATEST_VERSION | VARCHAR2 | 1 |  |  | Indicates if this is the most recent version of the time building block. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_GRP_USAGES_N1 | Non Unique | Default | TM_REC_ID, TM_REC_VERSION |
| HWM_TM_REC_GRP_USAGES_N2 | Non Unique | Default | TM_REC_GRP_ID, TM_REC_GRP_VERSION, TM_REC_ID, TM_REC_VERSION, LATEST_VERSION, ENTERPRISE_ID |
| HWM_TM_REC_GRP_USAGES_U1 | Unique | FUSION_TS_TX_DATA | TM_REC_GRP_USAGES_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
