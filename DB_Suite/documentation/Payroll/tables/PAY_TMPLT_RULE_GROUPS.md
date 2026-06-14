# PAY_TMPLT_RULE_GROUPS

Holds details of the grouping of the template rules which are used in the display of the template

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulegroups-18044.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltrulegroups-18044.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_RULE_GROUPS_PK | RULE_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RULE_GROUP_ID | NUMBER |  | 18 | Yes | RULE_GROUP_ID |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| BASE_RULE_GROUP_NAME | VARCHAR2 | 80 |  | Yes | BASE_RULE_GROUP_NAME |  |
| GROUP_LOCATION | VARCHAR2 | 30 |  |  | GROUP_LOCATION |  |
| TEMPLATE_ID | NUMBER |  | 18 |  | TEMPLATE_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_RULE_GROUPS_N20 | Non Unique | Default | SGUID |
| PAY_TMPLT_RULE_GROUPS_PK | Unique | Default | RULE_GROUP_ID |
| PAY_TMPLT_RULE_GROUPS_U1 | Unique | Default | LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, BASE_RULE_GROUP_NAME, TEMPLATE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
