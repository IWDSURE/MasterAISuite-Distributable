# ANC_PER_ACRL_ENTRY_DTLS_MAP

mapping table for person accural entry details for comp type record

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlentrydtlsmap-20963.html#ancperacrlentrydtlsmap-20963](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperacrlentrydtlsmap-20963.html#ancperacrlentrydtlsmap-20963)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACRL_ENTRY_DTLS_MAP_PK | PER_ACRL_ENTRY_DTLS_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ACRL_ENTRY_DTLS_MAP_ID | NUMBER |  | 18 | Yes | ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 |  | Accrual Entry DTL ID of consuming record |
| REF_PER_ACRL_ENTRY_DTL_ID | NUMBER |  | 18 |  | Reference to original Accrual Entry Dtl ID |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 |  | Absence entry ID |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 |  | PER_ABS_TYPE_ENTRY_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ACRL_ENTRY_DTLS_MAP_N1 | Non Unique | Default | PER_ACRL_ENTRY_DTL_ID |
| ANC_PER_ACRL_ENTRY_DTLS_MAP_N2 | Non Unique | FUSION_TS_TX_DATA | PER_ABS_TYPE_ENTRY_ID |
| ANC_PER_ACRL_ENTRY_DTLS_MAP_N3 | Non Unique | FUSION_TS_TX_DATA | PER_ABSENCE_ENTRY_ID, PER_ABS_TYPE_ENTRY_ID |
| ANC_PER_ACRL_ENTRY_DTLS_MAP_N4 | Non Unique | Default | REF_PER_ACRL_ENTRY_DTL_ID |
| ANC_PER_ACRL_ENTRY_DTLS_MAP_U1 | Unique | FUSION_TS_TX_DATA | PER_ACRL_ENTRY_DTLS_MAP_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
