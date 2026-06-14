# WLF_CATALOG_DEFAULT_RULES

Table to store learning catalog default rules.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcatalogdefaultrules-4705.html#wlfcatalogdefaultrules-4705](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcatalogdefaultrules-4705.html#wlfcatalogdefaultrules-4705)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CATALOG_DEFAULT_RULES_PK | CATALOG_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATALOG_RULE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Referece to a learning item. eg: Learning Catalog Profile. |
| RULE_NAME | VARCHAR2 | 250 |  |  | This column represents name of an attribute {Status,Attempt} |
| RULE_VALUE | VARCHAR2 | 4000 |  |  | This column represents value of an attribute {Active,Unlimited} |
| OVERRIDE_CHECKER | VARCHAR2 | 1 |  |  | This column represents if an attribute value can be overriden. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CATALOG_DEFAULT_RULES_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_CATALOG_DEFAULT_RULES_U1 | Unique | Default | CATALOG_RULE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
