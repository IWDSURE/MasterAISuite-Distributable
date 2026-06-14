# IRC_CAND_POOL_RULES

This table contains information on candidate pool rules.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolrules-30323.html#irccandpoolrules-30323](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpoolrules-30323.html#irccandpoolrules-30323)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_POOL_RULES_PK | RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RULE_ID | NUMBER |  | 18 | Yes | The primary key for this table. System-generated |
| POOL_ID | NUMBER |  | 18 | Yes | Foreign key to hrt_pools_b |
| CRITERIA | CLOB |  |  | Yes | Stores the rule value as JSON |
| RULE_MODIFIED_FLAG | VARCHAR2 | 1 |  |  | Store the Indicator if rule is modified by system due change impact |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_POOL_RULES_FK1 | Non Unique | Default | POOL_ID |
| IRC_CAND_POOL_RULES_N1 | Non Unique | Default | RULE_ID, JSON_QUERY("CRITERIA",'$.filters[*]?(@.name == "ORA_TAGS").terms') |
| IRC_CAND_POOL_RULES_PK | Unique | Default | RULE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
