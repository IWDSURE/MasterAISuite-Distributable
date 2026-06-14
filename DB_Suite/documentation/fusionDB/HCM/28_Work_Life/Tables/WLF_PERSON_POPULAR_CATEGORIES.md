# WLF_PERSON_POPULAR_CATEGORIES

This table is used to store recipients group by popular recommenders categories like group by job or groupy by manager etc

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpersonpopularcategories-31484.html#wlfpersonpopularcategories-31484](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpersonpopularcategories-31484.html#wlfpersonpopularcategories-31484)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PERS_POPULAR_CATEGORY_PK | PERSON_POPULAR_CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_POPULAR_CATEGORY_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| POPULARITY_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the popularity category. |
| POPULARITY_CATEGORY_ID | NUMBER |  | 18 | Yes | Specifies the identifier for the popularity category. |
| PERSON_ID | NUMBER |  | 18 | Yes | Specifies the person identifier. |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS Job processing the popular categories. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PERS_POPULAR_CATEGORY_N1 | Non Unique | Default | POPULARITY_CATEGORY, POPULARITY_CATEGORY_ID |
| WLF_PERS_POPULAR_CATEGORY_N2 | Non Unique | Default | ESS_JOB_ID |
| WLF_PERS_POPULAR_CATEGORY_U1 | Unique | Default | PERSON_POPULAR_CATEGORY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
