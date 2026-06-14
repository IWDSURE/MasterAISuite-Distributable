# PAY_EVENT_GROUPS

This table contains payroll event groups, such as retro events.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroups-20136.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventgroups-20136.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_GROUPS_PK | EVENT_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_GROUP_ID | NUMBER |  | 18 | Yes | System-generated primary key column |
| BASE_EVENT_GROUP_NAME | VARCHAR2 | 80 |  | Yes | BASE_EVENT_GROUP_NAME |
| EVENT_GROUP_TYPE | VARCHAR2 | 80 |  | Yes | Type of group |
| PRORATION_TYPE | VARCHAR2 | 30 |  |  | If used for Proration, identifies the type |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign Key to FND_TERRITORIES |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENT_SUBSCRIPTION_SET_ID | NUMBER |  | 18 |  | Enterprise Level Subscription Set Id |
| LDG_SUBSCRIPTION_SET_ID | NUMBER |  | 18 |  | Legislative Data Group Subscription Set Id |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |
| FORMULA_ID | NUMBER |  | 18 |  | Formula used to validate the overall Event. |
| SOURCE_ID | NUMBER |  | 18 |  | Foreign Key to the Source of the Event Group |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Determines the Source of the Event Group |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_EVENT_GROUPS_FK1 | Non Unique | Default | TIME_DEFINITION_ID |
| PAY_EVENT_GROUPS_PK | Unique | Default | EVENT_GROUP_ID, ORA_SEED_SET1 |
| PAY_EVENT_GROUPS_PK1 | Unique | Default | EVENT_GROUP_ID, ORA_SEED_SET2 |
| PAY_EVENT_GROUPS_UK1 | Unique | Default | BASE_EVENT_GROUP_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET1 |
| PAY_EVENT_GROUPS_UK11 | Unique | Default | BASE_EVENT_GROUP_NAME, LEGISLATION_CODE, LEGISLATIVE_DATA_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
