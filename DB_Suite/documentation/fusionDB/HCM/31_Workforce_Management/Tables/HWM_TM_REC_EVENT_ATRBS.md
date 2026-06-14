# HWM_TM_REC_EVENT_ATRBS

Time event attributes table for rest service devices.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreceventatrbs-17134.html#hwmtmreceventatrbs-17134](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmreceventatrbs-17134.html#hwmtmreceventatrbs-17134)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_REC_EVENT_ATRBS_PK | TM_REC_EVENT_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_REC_EVENT_ATRB_ID | NUMBER |  | 18 | Yes | TM_REC_EVENT_ATRB_ID |
| CHANGE_REASON | VARCHAR2 | 64 |  |  | Change reason for attribute change. |
| TM_REC_EVENT_ID | NUMBER |  |  | Yes | TM_REC_EVENT_ID |
| TM_ATRB_FLD_ID | NUMBER |  | 18 | Yes | TM_ATRB_FLD_ID |
| ATTRIBUTE_NAME | VARCHAR2 | 240 |  |  | ATTRIBUTE_NAME |
| VALUE | VARCHAR2 | 150 |  |  | Attribute Value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_REC_EVENT_ATRBS_N1 | Non Unique | Default | TM_REC_EVENT_ID |
| HWM_TM_REC_EVENT_ATRBS_U1 | Unique | Default | TM_REC_EVENT_ATRB_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
