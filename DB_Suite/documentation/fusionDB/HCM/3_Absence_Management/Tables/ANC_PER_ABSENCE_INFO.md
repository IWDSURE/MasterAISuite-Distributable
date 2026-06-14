# ANC_PER_ABSENCE_INFO

Records in this table store clob data information  for absence records which require approvals. This is to be used in BIP notifications to extract the values.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsenceinfo-12509.html#ancperabsenceinfo-12509](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsenceinfo-12509.html#ancperabsenceinfo-12509)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABSENCE_INFO_PK | PER_ABSENCE_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABSENCE_INFO_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_INFO_ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABSENCE_ENTRY_ID |
| PER_ABSENCE_INFO | CLOB |  |  |  | PER_ABSENCE_INFO |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABSENCE_INFO_U1 | Unique | Default | PER_ABSENCE_INFO_ID |
| anc_per_absence_info_INDEX_N1 | Non Unique | Default | PER_ABSENCE_ENTRY_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
