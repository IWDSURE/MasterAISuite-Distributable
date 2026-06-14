# HRT_CONTENT_ITEM_EXT_RELATIONS

Define the relationship between each content item and an external object, such as a questionnaire.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** hrt_content_item_ext_relations

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemextrelations-24252.html#hrtcontentitemextrelations-24252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemextrelations-24252.html#hrtcontentitemextrelations-24252)

## Primary Key

| Name | Columns |
|------|----------|
| hrt_content_item_ext_relat_PK | CONTENT_ITEM_EXT_RELATION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_ITEM_EXT_RELATION_ID | NUMBER |  | 18 | Yes | System generated primary key |
| PK1_VALUE | VARCHAR2 | 150 |  |  | To identify the primary keys in external table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_CONTENT_ITEMS_B table |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to HRT_CONTENT_TYPES_B table |
| OBJECT_ID | NUMBER |  | 18 | Yes | Foreign key to external table like HRQ_QUESTIONNAIRES_B |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of the external object like QUESTIONNAIRE |
| RELATION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Identify a relation type within a questionnaire, like skill |
| DATE_FROM | DATE |  |  | Yes | Start date of Content Item	 relation |
| DATE_TO | DATE |  |  |  | End date of Content Item relation |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEM_EXT_REL_PK | Unique | Default | CONTENT_ITEM_EXT_RELATION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
