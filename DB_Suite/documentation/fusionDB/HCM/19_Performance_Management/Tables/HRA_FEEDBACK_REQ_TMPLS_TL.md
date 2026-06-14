# HRA_FEEDBACK_REQ_TMPLS_TL

Translation table for template name of Feedback Requests

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackreqtmplstl-9797.html#hrafeedbackreqtmplstl-9797](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackreqtmplstl-9797.html#hrafeedbackreqtmplstl-9797)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_FEEDBACK_REQ_TMPLS_TL_PK | FEEDBACK_REQ_TMPL_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_REQ_TMPL_ID | NUMBER |  | 18 | Yes | Foreign key to Feedback requests base table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 400 |  | Yes | Translated Name |
| COMMENTS | VARCHAR2 | 4000 |  |  | Translated Comments |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_FEEDBACK_REQ_TMPLS_TL_U1 | Unique | Default | FEEDBACK_REQ_TMPL_ID, BUSINESS_GROUP_ID, LANGUAGE |
| HRA_FEEDBACK_REQ_TMPLS_TL_N1 | Non Unique | Default | NAME |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
