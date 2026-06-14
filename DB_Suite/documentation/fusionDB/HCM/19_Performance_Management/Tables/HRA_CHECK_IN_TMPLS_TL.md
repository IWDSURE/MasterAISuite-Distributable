# HRA_CHECK_IN_TMPLS_TL

This table will store translatable Ui field values for creating Check-In Template like name and comments

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplstl-19864.html#hracheckintmplstl-19864](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hracheckintmplstl-19864.html#hracheckintmplstl-19864)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_CHECK_IN_TMPLS_TL_PK | CHECK_IN_TEMPLATE_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECK_IN_TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign Key of Check-In Template and part of the Composite Primary Key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ALL_ORGANIZATION_UNITS |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 400 |  | Yes | Translated name of the Check-In Template |
| COMMENTS | VARCHAR2 | 4000 |  |  | Translated comments of the Check-In Template |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_CHECK_IN_TMPLS_TL_N1 | Non Unique | Default | NAME |
| HRA_CHECK_IN_TMPLS_TL_U1 | Unique | Default | CHECK_IN_TEMPLATE_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
