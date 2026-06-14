# HWM_ANC_INTERFACE_DIAG

This table is used for logging decoupling details , for exceptions or for debugging purposes

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmancinterfacediag-24298.html#hwmancinterfacediag-24298](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmancinterfacediag-24298.html#hwmancinterfacediag-24298)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_ANC_INTERFACE_DIAG_PK | IFACE_DIAGNOSTIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| IFACE_DIAGNOSTIC_ID | NUMBER |  | 18 | Yes | IFACE_DIAGNOSTIC_ID |
| WFM_IFACE_HDR_ID | NUMBER |  | 18 | Yes | WFM_IFACE_HDR_ID |
| PROCESS_TYPE | VARCHAR2 | 20 |  |  | PROCESS_TYPE |
| PROCESS_ID | VARCHAR2 | 80 |  |  | PROCESS_ID |
| ERROR_LOG | CLOB |  |  |  | ERROR_LOG |
| PAYLOAD | CLOB |  |  |  | PAYLOAD |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_ANC_INTERFACE_DIAG_U1 | Unique | Default | IFACE_DIAGNOSTIC_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
