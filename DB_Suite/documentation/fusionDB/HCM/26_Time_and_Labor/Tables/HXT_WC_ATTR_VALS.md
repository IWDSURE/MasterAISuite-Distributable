# HXT_WC_ATTR_VALS

This table is for storing the timecard attribute and its value assosicated with the punches of webclock

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtwcattrvals-21224.html#hxtwcattrvals-21224](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtwcattrvals-21224.html#hxtwcattrvals-21224)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_WC_ATTR_VALS_PK | WC_ATTR_VAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WC_ATTR_VAL_ID | NUMBER |  | 18 | Yes | Reference to a row of the webclock Timecard Fields table |
| WC_TCF_VALUE_CD | VARCHAR2 | 150 |  |  | Required to identify the value selected by the user for the timecardfield in discussion |
| TM_CARD_FLD_ID | NUMBER |  | 18 | Yes | Reference to a Timecard Attribute Fields |
| WC_TCF_VALUE_ID | NUMBER |  | 18 |  | Required to identify the value selected by the user for the timecardfield in discussion |
| WC_CLICKTIME_ID | NUMBER |  | 18 | Yes | Required to identify the event triggered |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | stores the enterprise id of the user |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_WC_TCFIELDS_U1 | Unique | Default | WC_ATTR_VAL_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
