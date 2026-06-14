# HXT_TCLAY_B

The table HXT_TCLAY_B table contains the list of all possible timecard layouts to be displayed for workers.  Examples are Entry Layout, Review Layout, Calendar Dialog Layout, etc.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayb-30098.html#hxttclayb-30098](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayb-30098.html#hxttclayb-30098)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAY_B_PK | TCLAY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAY_ID | NUMBER |  | 18 | Yes | TCLAY_ID |
| TCLAY_CD | VARCHAR2 | 500 |  |  | TCLAY_CD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCLAYST_ID | NUMBER |  | 18 |  | TCLAYST_ID |
| TCLAY_TYPE | VARCHAR2 | 32 |  | Yes | TCLAY_TYPE |
| STATUS | VARCHAR2 | 10 |  |  | STATUS |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAY_B_N1 | Non Unique | Default | TCLAY_TYPE, TCLAYST_ID |
| HXT_TCLAY_B_N20 | Non Unique | Default | SGUID |
| HXT_TCLAY_B_PK | Unique | Default | TCLAY_ID, ORA_SEED_SET1 |
| HXT_TCLAY_B_PK1 | Unique | Default | TCLAY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
