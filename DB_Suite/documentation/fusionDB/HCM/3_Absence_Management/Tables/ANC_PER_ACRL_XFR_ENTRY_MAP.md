# ANC_PER_ACRL_XFR_ENTRY_MAP

New Table to store transfer mapping

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlxfrentrymap-11248.html#ancperacrlxfrentrymap-11248](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlxfrentrymap-11248.html#ancperacrlxfrentrymap-11248)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ACRL_XFR_ENTRY_MA_PK | PER_ACRL_XFR_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ACRL_XFR_ENTRY_ID | NUMBER |  | 18 | Yes | ID |
| SRC_PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 |  | Accrual Entry DTL ID of source plan id of the transfer type record |
| TGT_PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 |  | Accural entry dtl_id of the targe plan id of the transfer type record |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SRC_PLAN_ID | NUMBER |  | 18 |  | Source plan Id of the transfer type record |
| TGT_PLAN_ID | NUMBER |  | 18 |  | Target plan Id of the transfer type record |
| CONVERSION_RATE | NUMBER |  | 18 |  | Conversion rate to transfer balance from one plan to another. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ACRL_XFR_ENTRY_MAP_U1 | Unique | Default | PER_ACRL_XFR_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
