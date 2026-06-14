# PAY_TMPLT_RULE_GR_USAGES

This Table will hold the relatoinship between the rules and the template

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulegrusages-29853.html#paytmpltrulegrusages-29853](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulegrusages-29853.html#paytmpltrulegrusages-29853)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_RULE_GR_USAGES_PK | RULE_GROUP_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RULE_GROUP_USAGE_ID | NUMBER |  | 18 | Yes | RULE_GROUP_USAGE_ID |  |
| GROUP_SEQUENCE | NUMBER |  | 2 |  | GROUP_SEQUENCE |  |
| BASE_RULE_GROUP_USAGE_ID | NUMBER |  | 18 |  | BASE_RULE_GROUP_USAGE_ID |  |
| ENABLE_FLAG | VARCHAR2 | 1 |  |  | ENABLE_FLAG |  |
| DISPLAY_FLAG | VARCHAR2 | 1 |  |  | DISPLAY_FLAG |  |
| RULE_GROUP_ID | NUMBER |  | 18 | Yes | RULE_GROUP_ID |  |
| RULE_ID | NUMBER |  | 18 | Yes | RULE_ID |  |
| TEMPLATE_ID | NUMBER |  | 18 |  | TEMPLATE_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| RULE_SEQUENCE | NUMBER |  | 18 |  | RULE_SEQUENCE |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TMPLT_RULE_GR_USAGES_N20 | Non Unique | Default | SGUID |
| PAY_TMPLT_RULE_GR_USAGES_PK | Unique | Default | RULE_GROUP_USAGE_ID |
| PAY_TMPLT_RULE_GR_USAGES_U1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, TEMPLATE_ID, RULE_GROUP_ID, RULE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
