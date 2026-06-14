# HRT_RATING_MODELS_TL_

Rating Model Translation Table.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingmodelstl-18428.html#hrtratingmodelstl-18428](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtratingmodelstl-18428.html#hrtratingmodelstl-18428)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_RATING_MODELS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, RATING_MODEL_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATING_MODEL_ID | NUMBER |  | 18 | Yes | Unique Identifier of Rating Model |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| RATING_NAME | VARCHAR2 | 240 |  |  | Name of Rating Model |
| RATING_DESCRIPTION | VARCHAR2 | 4000 |  |  | Rating Model description |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_RATING_MODELS_TLN1_ | Non Unique | Default | RATING_MODEL_ID, BUSINESS_GROUP_ID, LANGUAGE |
| HRT_RATING_MODELS_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, RATING_MODEL_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
