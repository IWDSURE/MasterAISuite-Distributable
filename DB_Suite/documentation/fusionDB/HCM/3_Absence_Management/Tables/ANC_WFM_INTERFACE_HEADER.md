# ANC_WFM_INTERFACE_HEADER

All ANC_PER_ABS_TYPE_ENTRIES rows created, changed, and deleted in a single transaction should be ‘grouped’ together under a single transaction ID in this staging table.  The staging acts as a processing queue for Absences not yet in the time repository.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancwfminterfaceheader-27490.html#ancwfminterfaceheader-27490](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancwfminterfaceheader-27490.html#ancwfminterfaceheader-27490)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_WFM_INTERFACE_HEADER_PK | WFM_IFACE_HDR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WFM_IFACE_HDR_ID | NUMBER |  | 18 | Yes | WFM_IFACE_HDR_ID |
| HEADER_ID | NUMBER |  | 18 | Yes | HEADER_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| PER_ABS_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_ENTRY_ID |
| PER_ABS_TYPE_ENTRY_ID | NUMBER |  | 18 | Yes | PER_ABS_TYPE_ENTRY_ID |
| START_DATETIME | TIMESTAMP |  |  | Yes | Absence type entry start date and time |
| END_DATETIME | TIMESTAMP |  |  |  | Absence type entry end date time |
| ABSENCE_TYPE_ID | NUMBER |  | 18 | Yes | Absence type id |
| TRANSACTION_ID | NUMBER |  | 18 |  | TRANSACTION_ID |
| USER_OPERATION | VARCHAR2 | 20 |  | Yes | USER_OPERATION |
| DML_OPERATION | VARCHAR2 | 20 |  | Yes | DML_OPERATION |
| STATUS_TIME | TIMESTAMP |  |  | Yes | STATUS_TIME |
| PROCESS_STATUS | NUMBER |  | 3 |  | PROCESS_STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_WFM_INTERFACE_HEADER_N1 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, TRANSACTION_ID, PROCESS_STATUS |
| ANC_WFM_INTERFACE_HEADER_N2 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, PROCESS_STATUS, STATUS_TIME |
| ANC_WFM_INTERFACE_HEADER_PK | Unique | FUSION_TS_TX_DATA | WFM_IFACE_HDR_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
