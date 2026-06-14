# HRY_OBJECT_ACT_PURGE_INFO

For Storing information about extract payroll object action for purge process.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryobjectactpurgeinfo-29890.html#hryobjectactpurgeinfo-29890](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryobjectactpurgeinfo-29890.html#hryobjectactpurgeinfo-29890)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_OBJECT_ACT_PURGE_INFO_ID | NUMBER |  | 18 |  | ID value for table hry_object_act_purge_info |
| ACTION_ID | NUMBER |  | 18 |  | Foreign key to tables PAY_OBJECT_ACTIONS or PAY_PAYROLL_REL_ACTIONS or PAY_TEMP_OBJECT_ACTIONS. |
| ACTION_TYPE | VARCHAR2 | 8 |  |  | Action Type values are POA or PTOA or PRA |
| EXT_ACTION_ID | NUMBER |  | 18 |  | Foreign Key to pay_payroll_actions record. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_OBJECT_ACT_PURGE_INFO_U1 | Unique | Default | HRY_OBJECT_ACT_PURGE_INFO_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
