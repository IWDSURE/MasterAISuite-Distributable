# HWR_CAT_TOPIC_B

The topic table is used to store tags/topics for a user and category.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcattopicb-4999.html#hwrcattopicb-4999](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcattopicb-4999.html#hwrcattopicb-4999)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CAT_TOPIC_B_PK | TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | This column holds the primary key for this table |  |
| CATEGORY_ID | NUMBER |  | 18 | Yes | The category id. This is a foreign key from the category tables. |  |
| CATEGORY_KEY | VARCHAR2 | 200 |  | Yes | This column holds the category_key from the category table |  |
| TOPIC_KEY | VARCHAR2 | 200 |  | Yes | This column holds the topic key for this table |  |
| AVERAGE_SCORE | NUMBER |  |  |  | This column stores average calculated score for the skill specified |  |
| URL_LINK | VARCHAR2 | 1000 |  |  | This column stores the url lik to the website that best teaches the skill set specified |  |
| IS_SEEDED_DATA | VARCHAR2 | 4 |  | Yes | A flag indicating seeded data. Use Y for seeded data or N for customer data | Active |
| ACCURACY_VALUE | NUMBER |  |  |  | This is the ACCURACY score for this topic. |  |
| IMPORTANCE_VALUE | NUMBER |  |  |  | This is the IMPORTANCE score for this topic. |  |
| PRECISION_VALUE | NUMBER |  |  |  | This is the PRECISION score for this topic. |  |
| RELEVANCE_VALUE | NUMBER |  |  |  | This is the RELEVANCE score for this topic. |  |
| IS_ACTIVE | VARCHAR2 | 4 |  | Yes | A flag indicating active topics to be used. Use Y for true (active) or N for false (not active) |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CAT_TOPIC_B_N1 | Non Unique | FUSION_TS_SEED | CATEGORY_ID |
| HWR_CAT_TOPIC_B_U1 | Unique | FUSION_TS_SEED | TOPIC_ID, ORA_SEED_SET1 |
| HWR_CAT_TOPIC_B_U11 | Unique | FUSION_TS_SEED | TOPIC_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
