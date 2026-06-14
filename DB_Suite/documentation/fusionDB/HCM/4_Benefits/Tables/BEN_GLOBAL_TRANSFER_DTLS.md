# BEN_GLOBAL_TRANSFER_DTLS

Used in Global Transfer process for Benefits

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benglobaltransferdtls-26377.html#benglobaltransferdtls-26377](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benglobaltransferdtls-26377.html#benglobaltransferdtls-26377)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_GLOBAL_TRANSFER_DTLS_F_PK | GLOBAL_TRANSFER_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GLOBAL_TRANSFER_DTL_ID | NUMBER |  | 18 | Yes | GLOBAL_TRANSFER_DTL_ID |
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 | Yes | MASS_ACTION_HEADER_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Assignment ID of launch assignment |
| PER_PERIODS_OF_SERVICE_ID | NUMBER |  | 18 |  | New PPS, Mass action table does not store |
| GLOBAL_TRANSFER_DATE | DATE |  |  |  | GLOBAL_TRANSFER_DATE |
| LER_ID | NUMBER |  | 18 |  | New LE |
| BALANCE_COPY_FLAG | VARCHAR2 | 30 |  |  | BALANCE_COPY_FLAG |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| STATUS | VARCHAR2 | 30 |  |  | Values are Initiated, Complete, Error |
| LEGISLATION_CODE | VARCHAR2 | 80 |  |  | New Legislation Code |
| PVAL001 | VARCHAR2 | 240 |  |  | Future use |
| PVAL002 | VARCHAR2 | 240 |  |  | Future use |
| PVAL003 | VARCHAR2 | 240 |  |  | Future use |
| PVAL004 | VARCHAR2 | 240 |  |  | Future use |
| PVAL005 | VARCHAR2 | 240 |  |  | Future use |
| PVAL006 | VARCHAR2 | 240 |  |  | Future use |
| PVAL007 | VARCHAR2 | 240 |  |  | Future use |
| PVAL008 | VARCHAR2 | 240 |  |  | Future use |
| PVAL009 | VARCHAR2 | 240 |  |  | Future use |
| PVAL010 | VARCHAR2 | 240 |  |  | Future use |
| PDATE001 | DATE |  |  |  | Future use |
| PDATE002 | DATE |  |  |  | Future use |
| PDATE003 | DATE |  |  |  | Future use |
| PDATE004 | DATE |  |  |  | Future use |
| PDATE005 | DATE |  |  |  | Future use |
| PDATE006 | DATE |  |  |  | Future use |
| PDATE007 | DATE |  |  |  | Future use |
| PDATE008 | DATE |  |  |  | Future use |
| PDATE009 | DATE |  |  |  | Future use |
| PDATE010 | DATE |  |  |  | Future use |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_GLOBAL_TRANSFER_DTLS_PK | Unique | Default | GLOBAL_TRANSFER_DTL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
