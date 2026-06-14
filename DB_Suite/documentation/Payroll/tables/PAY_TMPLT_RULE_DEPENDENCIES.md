# PAY_TMPLT_RULE_DEPENDENCIES

This Table holds meta data for dependency storage

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltruledependencies-12481.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltruledependencies-12481.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_RULE_DEPENDENCIES_PK | RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RELATION_ID | NUMBER |  | 18 | Yes | RELATION_ID |  |
| SOURCE_RULE_ID | NUMBER |  | 18 | Yes | SOURCE_RULE_ID |  |
| DEPENDENT_RULE_ID | NUMBER |  | 18 | Yes | DEPENDENT_RULE_ID |  |
| VALUE | VARCHAR2 | 250 |  |  | VALUE |  |
| USAGE | VARCHAR2 | 20 |  | Yes | USAGE |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_RULE_DEPENDENCIES_PK | Unique | Default | RELATION_ID |
| PAY_TMPLT_RULE_DEPENDENCI_N20 | Non Unique | Default | SGUID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
