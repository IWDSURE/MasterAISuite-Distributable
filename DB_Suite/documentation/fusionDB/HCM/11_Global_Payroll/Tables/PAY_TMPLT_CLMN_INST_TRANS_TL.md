# PAY_TMPLT_CLMN_INST_TRANS_TL

This Table Holds the clmn instances for template data

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttranstl-9113.html#paytmpltclmninsttranstl-9113](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltclmninsttranstl-9113.html#paytmpltclmninsttranstl-9113)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_CLMN_INST_TR_TL_PK | CLMN_INST_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CLMN_INST_ID | NUMBER |  | 18 | Yes | CLMN_INST_ID |  |
| COL_VALUE | VARCHAR2 | 4000 |  |  | COL_VALUE |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_CLMN_INST_TR_TL_PK | Unique | Default | CLMN_INST_ID, LANGUAGE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
