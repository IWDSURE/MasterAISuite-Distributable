# PAY_UPGRADE_LEGISLATIONS

This Table is used to enable/disable the Upgrade for particular legislation.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payupgradelegislations-22319.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payupgradelegislations-22319.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_UPGRADE_LEGISLATIONS_PK | UPGRADE_LEGISLATIONS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| UPGRADE_LEGISLATIONS_ID | NUMBER |  | 18 | Yes | UPGRADE_LEGISLATIONS_ID |  |
| UPGRADE_OBJECT_ID | NUMBER |  | 18 | Yes | UPGRADE_OBJECT_ID |  |
| ENABLED | VARCHAR2 | 3 |  | Yes | It will be marked as “N” , if any localization doesn’t want this upgrade. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 120 |  | Yes | Foreign key to FND_TERRITORIES. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |  |
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
| PAY_UPGRADE_LEGISLATIONS_N20 | Non Unique | Default | SGUID |
| PAY_UPGRADE_LEGISLATIONS_U1 | Unique | Default | UPGRADE_LEGISLATIONS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
