# HWM_TCD_EXP_DATA_PER_BDG_TXN

This table contains details for Time Clock Device export data for Person Badge Transactions

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataperbdgtxn-20554.html#hwmtcdexpdataperbdgtxn-20554](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtcdexpdataperbdgtxn-20554.html#hwmtcdexpdataperbdgtxn-20554)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TCD_EXP_DATA_PER_BDG_TX_PK | PER_BADGE_TXN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_BADGE_TXN_ID | NUMBER |  | 18 | Yes | Person Badge Data Transaction Id |
| PER_BADGE_DATA_ID | NUMBER |  | 18 |  | Person Badge Data Id |
| PER_BADGE_DATA_VERSION | NUMBER |  | 9 |  | Person Badge Data Version |
| TCD_EXP_DATA_TXN_ID | NUMBER |  | 18 |  | The time device export data transaction id |
| TCD_EXP_DATA_TXN_BATCH_ID | NUMBER |  | 9 |  | The time device export data transaction batch id |
| DELETE_FLAG | VARCHAR2 | 1 |  |  | Indicates soft delete of the row |
| STATUS | VARCHAR2 | 20 |  |  | Export or Collection Data Status |
| TCD_EXP_DATA_TXN_TYPE | VARCHAR2 | 15 |  |  | The time device export data transaction type. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TCD_PER_BDG_TXN_U1 | Unique | Default | PER_BADGE_TXN_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
