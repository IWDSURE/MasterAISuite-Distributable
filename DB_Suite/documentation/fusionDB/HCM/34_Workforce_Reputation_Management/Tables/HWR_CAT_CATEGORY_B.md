# HWR_CAT_CATEGORY_B

The category table stores information about groups of topics.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatcategoryb-14580.html#hwrcatcategoryb-14580](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcatcategoryb-14580.html#hwrcatcategoryb-14580)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CAT_CATEGORY_B_PK | CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | This column holds the primary key |  |
| CATEGORY_KEY | VARCHAR2 | 200 |  | Yes | This is a string key identifying a common category. | Active |
| CATEGORY_TYPE | NUMBER |  | 1 | Yes | This column holds the category type information.  As of now SOFT_SKILL(1), HARD_SKILL(2) |  |
| IS_SEEDED_DATA | VARCHAR2 | 4 |  | Yes | A flag indicating seeded data. Use Y for seeded data or N for customer data | Active |
| IS_ACTIVE | VARCHAR2 | 4 |  | Yes | A flag indicating active categories to be used. Use Y for true (active) or N for false (not active) |  |
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
| HWR_CAT_CATEGORY_B_U1 | Unique | FUSION_TS_SEED | CATEGORY_KEY, ORA_SEED_SET1 |
| HWR_CAT_CATEGORY_B_U11 | Unique | FUSION_TS_SEED | CATEGORY_KEY, ORA_SEED_SET2 |
| HWR_CAT_CATEGORY_B_U2 | Unique | FUSION_TS_SEED | CATEGORY_ID, ORA_SEED_SET1 |
| HWR_CAT_CATEGORY_B_U21 | Unique | FUSION_TS_SEED | CATEGORY_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
