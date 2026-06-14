# HWM_TM_AUDIT_ATRBS

The Time change audit attributes(TAA) table stores one row for each change of an attribute for a time entry.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmauditatrbs-17390.html#hwmtmauditatrbs-17390](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmauditatrbs-17390.html#hwmtmauditatrbs-17390)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_AUDIT_ATRBS_PK | TM_AUDIT_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_AUDIT_ATRB_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_AUDIT_ID | NUMBER |  | 18 | Yes | Reference to a row of the Time audit table |
| ACTION_TYPE | VARCHAR2 | 1 |  | Yes | Action performed on the attribute |
| REASON_CODE | VARCHAR2 | 30 |  |  | Code referencing a Lookup value |
| TM_ATRB_FLD_ID | NUMBER |  | 18 |  | Id of the Time attribute updated if ACTION_TYPE = Update |
| TM_ATTRIBUTE_TYPE | VARCHAR2 | 20 |  |  | Type of the attribute : Number, Varchar, Timestamp, Date |
| OLD_TIMESTAMP | TIMESTAMP |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp,Timestamp value of the attribute before change |
| OLD_ZONE_TYPE | VARCHAR2 | 30 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the type of time zone for the value of the attribute before change. Possible values : OFFSET, ZONE, NULL |
| OLD_GMT_OFFSET | NUMBER |  | 22 |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the time zone offset in milliseconds for the value of the attribute before change |
| OLD_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the time zone code for the value of the attribute before change |
| NEW_TIMESTAMP | TIMESTAMP |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp,Timestamp value of the attribute after change |
| NEW_ZONE_TYPE | VARCHAR2 | 30 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the type of time zone for the value of the attribute after change. Possible values : OFFSET, ZONE, NULL |
| NEW_GMT_OFFSET | NUMBER |  | 22 |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the time zone offset in milliseconds for the value of the attribute after change. |
| NEW_TIMEZONE_CODE | VARCHAR2 | 50 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Timestamp, contain the time zone code for the value of the attribute after change. |
| OLD_VARCHAR | VARCHAR2 | 2000 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Varchar, value of the attribute before change |
| NEW_VARCHAR | VARCHAR2 | 2000 |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Varchar, value of the attribute after change |
| OLD_DATE | DATE |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Date, value of the attribute before change |
| NEW_DATE | DATE |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Date, value of the attribute after change |
| OLD_NUMBER | NUMBER |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Number, value of the attribute before change |
| NEW_NUMBER | NUMBER |  |  |  | if ACTION_TYPE = Update and ATTRIBUTE_TYPE = Number, value of the attribute after change |
| ORIG_AUDIT_ATRB_ID | NUMBER |  | 18 |  | Reference the initial audit rows when updating the reason attribute |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |
| REASON_CHANGE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of when the Change Reason of this audit row is updated. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_AUDIT_ATRBS_N1 | Non Unique | FUSION_TS_TX_DATA | TM_AUDIT_ID |
| HWM_TM_AUDIT_ATRBS_U1 | Unique | FUSION_TS_TX_DATA | TM_AUDIT_ATRB_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
