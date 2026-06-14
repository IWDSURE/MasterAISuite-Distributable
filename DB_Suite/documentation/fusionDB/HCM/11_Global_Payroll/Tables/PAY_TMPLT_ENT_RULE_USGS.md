# PAY_TMPLT_ENT_RULE_USGS

This entity indicated how a rule (i.e. a question) can be used to exclude a record or another rule.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltentruleusgs-28741.html#paytmpltentruleusgs-28741](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltentruleusgs-28741.html#paytmpltentruleusgs-28741)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_ENT_RULE_USGS_PK | ENT_RULE_USG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ENT_RULE_USG_ID | NUMBER |  | 18 | Yes | ENT_RULE_USG_ID |  |
| RULE_VALUE | VARCHAR2 | 200 |  |  | RULE_VALUE |  |
| BASE_ENT_RULE_USG_ID | NUMBER |  | 18 |  | BASE_ENT_RULE_USG_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |  |
| ENTITY_ID | NUMBER |  | 18 | Yes | ENTITY_ID |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| LEGISLATION_CODE | VARCHAR2 | 32 |  |  | Foreign key to FND_TERRITORIES. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| ENTITY_TYPE | VARCHAR2 | 30 |  |  | ENTITY_TYPE |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PAY_TMPLT_ENT_RULE_USGS_N1 | Non Unique | Default | BASE_ENT_RULE_USG_ID, LEGISLATION_CODE | Obsolete |
| PAY_TMPLT_ENT_RULE_USGS_N20 | Non Unique | Default | SGUID |  |
| PAY_TMPLT_ENT_RULE_USGS_PK | Unique | Default | ENT_RULE_USG_ID |  |
| PAY_TMPLT_ENT_RULE_USGS_U1 | Unique | Default | LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, RULE_ID, ENTITY_ID, RULE_VALUE |  |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
