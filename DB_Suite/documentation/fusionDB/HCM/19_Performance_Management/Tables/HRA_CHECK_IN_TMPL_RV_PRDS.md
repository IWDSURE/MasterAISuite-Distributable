# HRA_CHECK_IN_TMPL_RV_PRDS

This table will store the Review Periods eligible for a Check-in template.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplrvprds-27055.html#hracheckintmplrvprds-27055](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplrvprds-27055.html#hracheckintmplrvprds-27055)

## Primary Key

| Name | Columns |
|------|----------|
| hra_check_in_tmpl_rv_prds_PK | CHECK_IN_TMPL_RV_PRD_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECK_IN_TMPL_RV_PRD_ID | NUMBER |  | 18 | Yes | System generated unique key |
| BUSINESS_GROUP_ID | VARCHAR2 | 18 |  | Yes | Foreign key to PER_BUSINESS_GROUPS |
| CHECK_IN_TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign key of Check-In Template |
| REVIEW_PERIOD_ID | NUMBER |  | 18 | Yes | Foreign key of Review Period |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_CHECK_IN_TMPL_RV_PRDS_U1 | Unique | Default | CHECK_IN_TMPL_RV_PRD_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
