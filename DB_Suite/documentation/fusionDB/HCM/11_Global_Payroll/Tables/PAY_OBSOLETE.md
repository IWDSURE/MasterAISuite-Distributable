# PAY_OBSOLETE

Table to hold index of obsoleted seed data.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobsolete-5536.html#payobsolete-5536](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payobsolete-5536.html#payobsolete-5536)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_OBSOLETE_PK | OBSOLETE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| OBSOLETE_ID | NUMBER |  | 18 | Yes | OBSOLETE_ID |  |
| INSTANCE | VARCHAR2 | 30 |  | Yes | INSTANCE |  |
| AMVO | VARCHAR2 | 300 |  | Yes | AMVO |  |
| KEY | VARCHAR2 | 512 |  |  | KEY |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| ACTION | VARCHAR2 | 1 |  |  | ACTION |  |
| ROWFOUND | VARCHAR2 | 1 |  |  | ROWFOUND |  |
| RESULT | VARCHAR2 | 100 |  |  | RESULT |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_OBSOLETE_U1 | Unique | Default | OBSOLETE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
