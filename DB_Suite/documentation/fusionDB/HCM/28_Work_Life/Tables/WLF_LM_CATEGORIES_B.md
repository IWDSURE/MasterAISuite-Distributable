# WLF_LM_CATEGORIES_B

Category table indicates the role in which an activity category is used.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcategoriesb-29988.html#wlflmcategoriesb-29988](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcategoriesb-29988.html#wlflmcategoriesb-29988)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_CATEGORIES_PK | CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_ID | NUMBER |  | 18 | Yes | CATEGORY_ID |
| PARENT_CATEGORY_ID | NUMBER |  | 18 |  | PARENT_CATEGORY_ID |
| TYPE | VARCHAR2 | 30 |  | Yes | TYPE |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| SYNCHRONOUS_FLAG | VARCHAR2 | 30 |  |  | SYNCHRONOUS_FLAG |
| ONLINE_FLAG | VARCHAR2 | 30 |  |  | ONLINE_FLAG |
| DATA_SOURCE | VARCHAR2 | 30 |  |  | DATA_SOURCE |
| USER_GROUP_ID | NUMBER |  | 18 |  | USER_GROUP_ID |
| START_DATE_ACTIVE | DATE |  |  |  | START_DATE_ACTIVE |
| END_DATE_ACTIVE | DATE |  |  |  | END_DATE_ACTIVE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CAT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CAT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CAT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER1 |
| CAT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER2 |
| CAT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER3 |
| CAT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER4 |
| CAT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER5 |
| CAT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER6 |
| CAT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER7 |
| CAT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER8 |
| CAT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER9 |
| CAT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER10 |
| CAT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER11 |
| CAT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER12 |
| CAT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER13 |
| CAT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER14 |
| CAT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER15 |
| CAT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER16 |
| CAT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER17 |
| CAT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER18 |
| CAT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER19 |
| CAT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CAT_ATTRIBUTE_NUMBER20 |
| CAT_ATTRIBUTE_DATE1 | DATE |  |  |  | CAT_ATTRIBUTE_DATE1 |
| CAT_ATTRIBUTE_DATE2 | DATE |  |  |  | CAT_ATTRIBUTE_DATE2 |
| CAT_ATTRIBUTE_DATE3 | DATE |  |  |  | CAT_ATTRIBUTE_DATE3 |
| CAT_ATTRIBUTE_DATE4 | DATE |  |  |  | CAT_ATTRIBUTE_DATE4 |
| CAT_ATTRIBUTE_DATE5 | DATE |  |  |  | CAT_ATTRIBUTE_DATE5 |
| CAT_ATTRIBUTE_DATE6 | DATE |  |  |  | CAT_ATTRIBUTE_DATE6 |
| CAT_ATTRIBUTE_DATE7 | DATE |  |  |  | CAT_ATTRIBUTE_DATE7 |
| CAT_ATTRIBUTE_DATE8 | DATE |  |  |  | CAT_ATTRIBUTE_DATE8 |
| CAT_ATTRIBUTE_DATE9 | DATE |  |  |  | CAT_ATTRIBUTE_DATE9 |
| CAT_ATTRIBUTE_DATE10 | DATE |  |  |  | CAT_ATTRIBUTE_DATE10 |
| CAT_ATTRIBUTE_DATE11 | DATE |  |  |  | CAT_ATTRIBUTE_DATE11 |
| CAT_ATTRIBUTE_DATE12 | DATE |  |  |  | CAT_ATTRIBUTE_DATE12 |
| CAT_ATTRIBUTE_DATE13 | DATE |  |  |  | CAT_ATTRIBUTE_DATE13 |
| CAT_ATTRIBUTE_DATE14 | DATE |  |  |  | CAT_ATTRIBUTE_DATE14 |
| CAT_ATTRIBUTE_DATE15 | DATE |  |  |  | CAT_ATTRIBUTE_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_CATEGORIES_N1 | Non Unique | Default | ENTERPRISE_ID, TYPE |
| WLF_LM_CATEGORIES_N2 | Non Unique | Default | SYNCHRONOUS_FLAG, ONLINE_FLAG |
| WLF_LM_CATEGORIES_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| WLF_LM_CATEGORIES_U1 | Unique | Default | CATEGORY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
