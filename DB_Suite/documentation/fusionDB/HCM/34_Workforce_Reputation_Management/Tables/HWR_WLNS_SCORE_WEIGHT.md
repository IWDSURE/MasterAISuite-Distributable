# HWR_WLNS_SCORE_WEIGHT

This table stores wellness score weight per category.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsscoreweight-5724.html#hwrwlnsscoreweight-5724](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsscoreweight-5724.html#hwrwlnsscoreweight-5724)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_SCORE_WEIGHT_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| CATEGORY | VARCHAR2 | 64 |  | Yes | This is the key of the base category. |
| CAT_WEIGHT | NUMBER |  |  | Yes | This is the weight value of the base category. |
| QUALIFIER_1 | VARCHAR2 | 64 |  |  | This is the key of the sub category. |
| QUA_WEIGHT_1 | NUMBER |  |  |  | This is the weight value of the sub category. |
| QUA_PATTERN_1 | VARCHAR2 | 64 |  |  | This is the weight pattern of the sub category. |
| QUALIFIER_2 | VARCHAR2 | 64 |  |  | This is the key of the sub category. |
| QUA_WEIGHT_2 | NUMBER |  |  |  | This is the weight value of the sub category. |
| QUA_PATTERN_2 | VARCHAR2 | 64 |  |  | This is the weight pattern of the sub category. |
| QUALIFIER_3 | VARCHAR2 | 64 |  |  | This is the key of the sub category. |
| QUA_WEIGHT_3 | NUMBER |  |  |  | This is the weight value of the sub category. |
| QUA_PATTERN_3 | VARCHAR2 | 64 |  |  | This is the weight pattern of the sub category. |
| FORMULA | VARCHAR2 | 1000 |  |  | This is the formula to compute the score. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_SCORE_WEIGHT_U1 | Unique | Default | ID, ORA_SEED_SET1 |
| HWR_WLNS_SCORE_WEIGHT_U11 | Unique | Default | ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
