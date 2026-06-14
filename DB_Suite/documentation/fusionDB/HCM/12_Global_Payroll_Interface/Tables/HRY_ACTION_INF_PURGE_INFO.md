# HRY_ACTION_INF_PURGE_INFO

For Storing information about extract pay action information for purge process.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryactioninfpurgeinfo-18507.html#hryactioninfpurgeinfo-18507](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryactioninfpurgeinfo-18507.html#hryactioninfpurgeinfo-18507)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRY_ACTION_INF_PURGE_INFO_ID | NUMBER |  | 18 |  | ID value for table hry_action_inf_purge_info |
| ACTION_INFORMATION_ID | NUMBER |  | 18 |  | Foreign Key to table PAY_ACTION_INFORMATION |
| STATUS | VARCHAR2 | 4 |  |  | Status of purge record.values are P or U |
| PAI_ROW_ID | VARCHAR2 | 80 |  |  | Row id of table PAY_ACTION_INFORMATION Purge Record |
| ACTION_ID | NUMBER |  | 18 |  | Foreign key to PAY_OBJECT_ACTIONS or PAY_PAYROLL_REL_ACTIONS or PAY_TEMP_OBJECT_ACTIONS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_ACTION_INF_PURGE_INFO_U1 | Unique | Default | HRY_ACTION_INF_PURGE_INFO_ID |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
