# HWM_TM_AUDITS

The Time change audit (TA) table stores one row for each time entry.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmaudits-7503.html#hwmtmaudits-7503](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmaudits-7503.html#hwmtmaudits-7503)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_AUDITS_PK | TM_AUDIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_AUDIT_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TM_RECORD_GRP_ID | NUMBER |  | 18 | Yes | reference to the time record group (time card) |
| USAGES_TYPE | NUMBER |  | 9 | Yes | 1 = RECORD, can take other value in the future |
| ACTION_TYPE | VARCHAR2 | 1 |  | Yes | Action performed on the referenced item |
| REF_DATE | DATE |  |  | Yes | The date to which this Time Record is assigned |
| TM_BLK_ID | NUMBER |  | 18 | Yes | Id of the time record (created, deleted or before) |
| TM_BLK_VERSION | NUMBER |  | 9 | Yes | Version of the time record  (created, deleted or before) |
| TM_NEW_BLK_ID | NUMBER |  | 18 |  | in case of update action, Id of the time record after update |
| TM_NEW_BLK_VERSION | NUMBER |  | 9 |  | Version of the time record after update or create |
| REASON_CODE | VARCHAR2 | 30 |  |  | Code referencing a Lookup value. |
| ORIG_AUDIT_ID | NUMBER |  | 18 |  | Reference the initial audit rows when updating the reason attribute |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| PART_DATE | TIMESTAMP |  |  |  | partition key |
| PART_GRP_TYPE_ID | NUMBER |  | 18 |  | partition key |
| CHANGE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of the corresponding change made on the time entry. |
| CHANGED_BY | VARCHAR2 | 64 |  |  | Indicates the user who made the corresponding change on the time entry. |
| REASON_CHANGE_DATE | TIMESTAMP |  |  |  | Indicates the date and time of when the Change Reason of this audit row is updated. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_AUDITS_N1 | Non Unique | FUSION_TS_TX_DATA | TM_RECORD_GRP_ID |
| HWM_TM_AUDITS_N2 | Non Unique | Default | TM_BLK_ID |
| HWM_TM_AUDITS_N3 | Non Unique | Default | TM_NEW_BLK_ID |
| HWM_TM_AUDITS_U1 | Unique | FUSION_TS_TX_DATA | TM_AUDIT_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
