# HWM_TM_REP_ALLOW_EXPS

an allow exception record is to capture if an exception is  allowed for an time entry .

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepallowexps-20918.html#hwmtmrepallowexps-20918](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepallowexps-20918.html#hwmtmrepallowexps-20918)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REP_ALLOW_EXPS_PK | TM_REP_ALLOW_EXPS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REP_ALLOW_EXPS_ID | NUMBER |  | 18 | Yes | TM_REP_ALLOW_EXPS_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| REPOSITORY_TYPE | VARCHAR2 | 32 |  |  | REPOSITORY_TYPE |
| TM_BLDG_BLK_ID | NUMBER |  | 18 | Yes | TM_BLDG_BLK_ID |
| TM_BLDG_BLK_VERSION | NUMBER |  | 9 | Yes | TM_BLDG_BLK_VERSION |
| TM_REP_MSGS_ID | NUMBER |  | 18 |  | TM_REP_MSGS_ID |
| TM_REP_MSGS_NAME | VARCHAR2 | 256 |  | Yes | TM_REP_MSGS_NAME |
| ATTRIBUTE_TYPE | VARCHAR2 | 20 |  |  | ATTRIBUTE_TYPE |
| MESSAGE_FIELD | VARCHAR2 | 256 |  |  | MESSAGE_FIELD |
| MESSAGE_FIELD_NUMBER_VALUE | NUMBER |  | 18 |  | MESSAGE_FIELD_NUMBER_VALUE |
| MESSAGE_FIELD_VARCHAR_VALUE | VARCHAR2 | 150 |  |  | MESSAGE_FIELD_VARCHAR_VALUE |
| MESSAGE_FIELD_DATE_VALUE | DATE |  |  |  | MESSAGE_FIELD_DATE_VALUE |
| MESSAGE_FIELD_TIMESTAMP_VALUE | TIMESTAMP |  |  |  | MESSAGE_FIELD_TIMESTAMP_VALUE |
| ALLOW_EXCEPTION | VARCHAR2 | 1 |  |  | ALLOW_EXCEPTION |
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
| HWM_TM_REP_ALLOW_EXPS_N1 | Non Unique | Default | TM_BLDG_BLK_ID, TM_BLDG_BLK_VERSION |
| HWM_TM_REP_ALLOW_EXPS_N2 | Non Unique | Default | TM_REP_MSGS_ID |
| HWM_TM_REP_ALLOW_EXPS_U1 | Unique | Default | TM_REP_ALLOW_EXPS_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
