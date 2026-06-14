# HRY_VALUE_MAP_RULESET_TL

Stores translation information related to value map rule set.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryvaluemaprulesettl-17826.html#hryvaluemaprulesettl-17826](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryvaluemaprulesettl-17826.html#hryvaluemaprulesettl-17826)

## Primary Key

| Name | Columns |
|------|----------|
| hry_value_map_ruleset_tl_PK | RULE_SET_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_SET_ID | NUMBER |  | 18 | Yes | Primary key for HRY_VALUE_MAP_RULESET. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| RULE_SET_NAME | VARCHAR2 | 255 |  | Yes | For storing translated rule set name. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | This column holds the description of the rule set. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hry_value_map_ruleset_tl_PK | Unique | Default | RULE_SET_ID, LANGUAGE, ORA_SEED_SET1 |
| hry_value_map_ruleset_tl_PK1 | Unique | hry_value_map_ruleset_tl_PK1 | RULE_SET_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
