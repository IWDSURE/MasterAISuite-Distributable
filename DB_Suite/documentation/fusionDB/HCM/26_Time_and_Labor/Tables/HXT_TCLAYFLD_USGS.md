# HXT_TCLAYFLD_USGS

The table HXT_TCLAYFLD_USGS contains the usage mapping of layout fields in layout sets.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayfldusgs-28407.html#hxttclayfldusgs-28407](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxttclayfldusgs-28407.html#hxttclayfldusgs-28407)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_TCLAYFLD_USGS_PK | TCLAYFLD_USGS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TCLAYFLD_USGS_ID | NUMBER |  | 18 | Yes | COLUMN1 |
| DESCRIPTION | VARCHAR2 | 3200 |  |  | DESCRIPTION |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| TCLAY_ID | NUMBER |  | 18 |  | TCLAY_ID |
| TCLAYFLD_DEFNS_ID | NUMBER |  | 18 |  | TCLAYFLD_DEFNS_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_TCLAYFLD_USGS_PK | Unique | Default | TCLAYFLD_USGS_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
