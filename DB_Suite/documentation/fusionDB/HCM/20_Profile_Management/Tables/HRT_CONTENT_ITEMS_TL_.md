# HRT_CONTENT_ITEMS_TL_

Content Item translation table.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemstl-23860.html#hrtcontentitemstl-23860](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemstl-23860.html#hrtcontentitemstl-23860)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_ITEMS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Unique identifier of Content Item |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| NAME | VARCHAR2 | 700 |  |  | The name of Content Item |  |
| ITEM_DESCRIPTION | VARCHAR2 | 2000 |  |  | The description of Content Item |  |
| ITEM_TEXT_TL_1 | VARCHAR2 | 240 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_2 | VARCHAR2 | 240 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_3 | VARCHAR2 | 240 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_4 | VARCHAR2 | 240 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_5 | VARCHAR2 | 240 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_6 | VARCHAR2 | 2000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_7 | VARCHAR2 | 2000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_8 | VARCHAR2 | 2000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_9 | VARCHAR2 | 2000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_10 | VARCHAR2 | 2000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_11 | VARCHAR2 | 4000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_12 | VARCHAR2 | 4000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_13 | VARCHAR2 | 4000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_14 | VARCHAR2 | 4000 |  |  | Text column in defining Content Type properties |  |
| ITEM_TEXT_TL_15 | VARCHAR2 | 4000 |  |  | Text column in defining Content Type properties |  |
| ITEM_DESCRLONG | VARCHAR2 | 4000 |  |  | Long description of Content Item |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEMS_TLN1_ | Non Unique | Default | CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE |
| HRT_CONTENT_ITEMS_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONTENT_ITEM_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
