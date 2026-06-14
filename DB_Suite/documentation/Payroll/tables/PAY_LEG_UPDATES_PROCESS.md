# PAY_LEG_UPDATES_PROCESS

PAY_LEG_UPDATES_PROCESS - stores transaction of legislative data update process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatesprocess-28399.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatesprocess-28399.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LEG_UPDATES_PROCESS_PK | PAY_LEG_UPDATE_PRC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_LEG_UPDATE_PRC_ID | NUMBER |  | 18 | Yes | Unique ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | CA, US.... |
| UPDATE_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Update Type Base Code. Example - TAX DATA, GEOGRAPHY.... |
| UPDATE_FOR_YEAR | NUMBER |  | 4 | Yes | 2023, 2024.... |
| UPDATE_FOR_MONTH | VARCHAR2 | 30 |  | Yes | 1-12 |
| SEQ_FOR_YEAR_MON | NUMBER |  | 4 | Yes | 1,2,3,4..... (Sequence number within Year and Month) |
| INTERNAL_SEQUENCE | NUMBER |  | 4 |  | 1,2,3,4..... (Sequence number for internal purpose) |
| PROCESS_STATUS | VARCHAR2 | 1 |  |  | I - In process, E - Error, C - Complete |
| PAY_REQUEST_ID | NUMBER |  | 18 |  | Request ID of the Flow Request |
| PROCESS_START_DATE_TIME | TIMESTAMP |  |  |  | ESS job upload start date/time |
| PROCESS_END_DATE_TIME | TIMESTAMP |  |  |  | ESS job upload end date/time |
| ENTERPRISE_ID | NUMBER |  | 18 |  | NVL(SYS_CONTEXT('FND_VPD_CTX', 'FND_ENTERPRISE_ID'), 0) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_LEG_UPDATES_PROCESS_PK | Unique | Default | PAY_LEG_UPDATE_PRC_ID |
| PAY_LEG_UPDATES_PROCESS_UK1 | Unique | Default | LEGISLATION_CODE, UPDATE_TYPE_CODE, UPDATE_FOR_YEAR, UPDATE_FOR_MONTH, SEQ_FOR_YEAR_MON |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
