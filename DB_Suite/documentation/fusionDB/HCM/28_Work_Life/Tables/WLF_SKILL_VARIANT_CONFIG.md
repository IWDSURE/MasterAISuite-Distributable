# WLF_SKILL_VARIANT_CONFIG

This table stores the recommender configuration details.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfskillvariantconfig-21353.html#wlfskillvariantconfig-21353](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfskillvariantconfig-21353.html#wlfskillvariantconfig-21353)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SKILL_VARIANT_CONFIG_PK | SKILL_VARIANT_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SKILL_VARIANT_CONFIG_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| USE_SKILL_VARIANTS | VARCHAR2 | 30 |  |  | Specifies whether to consider skill variants or not. |
| USE_SEMANTIC_VARIANTS | VARCHAR2 | 30 |  |  | Specifies whether to consider semantic skill variants or not. |
| SEMANTIC_VARIANT_MIN_SCORE | NUMBER |  |  |  | Specifies minimum score for semantic skill variant to be considered |
| USE_RAW_SYNTACTIC_VARIANTS | VARCHAR2 | 30 |  |  | Specifies whether to consider 'raw syntactic variants' or not. |
| USE_CONTAIN_SYNTACTIC_VARIANTS | VARCHAR2 | 30 |  |  | Specifies whether to consider 'contains syntactic variants' or not. |
| SKILL_VARIANT_COUNT | NUMBER |  |  |  | Specifies how many number of skill variants to consider in each catetory. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SKILL_VARIANT_CONFIG_U1 | Unique | Default | SKILL_VARIANT_CONFIG_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
