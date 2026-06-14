# HWM_TM_REC_CHANGE_ATRBS

Table to store changed attributes for change requests.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchangeatrbs-24210.html#hwmtmrecchangeatrbs-24210](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrecchangeatrbs-24210.html#hwmtmrecchangeatrbs-24210)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_rec_change_attribu_PK | TM_REC_CHANGE_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_CHANGE_ATRB_ID | NUMBER |  |  | Yes | TM_REC_CHANGE_ATRB_ID |
| VALUE_VARCHAR_OLD | VARCHAR2 | 2000 |  |  | Old value of the attribute (varchar) |
| VALUE_NUMBER_OLD | NUMBER |  |  |  | Old value of the attribute (number) |
| VALUE_DATE_OLD | DATE |  |  |  | Old value of the attribute (date) |
| VALUE_TIMESTAMP_OLD | TIMESTAMP |  |  |  | Old value of the attribute (timestamp) |
| TM_REC_CHANGE_ID | NUMBER |  |  | Yes | Foreign key for the table HWM_TM_REC_CHANGES |
| TM_ATRB_FLD_ID | NUMBER |  |  | Yes | Attribute id (needs to be resolved by creating a transient attribute and LOV with all attribute names) |
| ATTRIBUTE_TYPE | VARCHAR2 | 64 |  | Yes | ATTRIBUTE_TYPE |
| VALUE_VARCHAR | VARCHAR2 | 2000 |  |  | VALUE_VARCHAR |
| VALUE_NUMBER | NUMBER |  |  |  | VALUE_NUMBER |
| VALUE_DATE | DATE |  |  |  | VALUE_DATE |
| VALUE_TIMESTAMP | TIMESTAMP |  |  |  | VALUE_TIMESTAMP |
| VALUE_GMT_OFFSET | NUMBER |  |  |  | Value of GMT offset in case of timestamp |
| VALUE_TIMEZONE_CODE | VARCHAR2 | 150 |  |  | Value of Timezone code in case of timestamp |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| hwm_tm_rec_change_atrbs_N1 | Non Unique | Default | TM_ATRB_FLD_ID | Obsolete |
| hwm_tm_rec_change_atrbs_N2 | Non Unique | Default | TM_REC_CHANGE_ID |  |
| hwm_tm_rec_change_atrbs_U1 | Unique | Default | TM_REC_CHANGE_ATRB_ID |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
