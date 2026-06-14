# WLF_RECOM_CONTEXT

This table stores the recommendation context information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomcontext-9830.html#wlfrecomcontext-9830](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomcontext-9830.html#wlfrecomcontext-9830)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOM_CONTEXT_PK | RECOM_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOM_CONTEXT_ID | NUMBER | 18 |  | Yes | System generated unique identifier. |
| RECOMMENDATION_ID | NUMBER | 18 |  | Yes | Foreign Key to WLF_RECOMMENDATIONS |
| CONTEXT_TYPE | VARCHAR2 | 30 |  | Yes | Specifies the context type |
| PROFILE_ID | NUMBER | 18 |  |  | Identifier for the talent profile |
| PROFILE_TYPE_CODE | VARCHAR2 | 30 |  |  | Specifies talent profile type |
| CONTENT_TYPE_ID | NUMBER | 18 |  |  | Foreign Key to HRT_CONTENT_TYPES_B |
| CONTENT_ITEM_ID | NUMBER | 18 |  |  | Foreign Key to HRT_CONTENT_ITEMS_B |
| CONTENT_ITEM_TEXT | VARCHAR2 | 250 |  |  | Specifies content item text value of type free-form text |
| MANAGER_ID | NUMBER | 18 |  |  | Identifier for the manager |
| WORK_ASSIGNMENT_ID | NUMBER | 18 |  |  | Identifier for the work assignment |
| DEST_CRITERIA_ID | NUMBER | 18 |  |  | Identifier for the destination criteria |
| DEST_CRITERIA_TYPE | VARCHAR2 | 30 |  |  | Specifies the destination criteria type |
| IS_CURATED_ROLE_SKILL | VARCHAR2 | 1 |  |  | Specifies if the role skill is curated or not |
| IS_CURATED_RESOURCE_SKILL | VARCHAR2 | 1 |  |  | Specifies if the resource skill is curated or not |
| RESOURCE_MATCHING_CRITERIA | VARCHAR2 | 30 |  |  | Specifies the criteria for recommending resources |
| IS_REQ_ROLE_CONTENT_ITEM | VARCHAR2 | 1 |  |  | Specifies if the content item is marked as required in the role profile |
| IS_RESOURCE_WITH_OUTCOME | VARCHAR2 | 1 |  |  | Specifies if the resource is defined with the content item as an outcome |
| ESS_JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS Job populating the recommendation context |
| SYNONYM_CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_TYPES_B |
| SYNONYM_CONTENT_ITEM_TEXT | VARCHAR2 | 250 |  |  | Specifies content item text value of type free-form text |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOM_CONTEXT_N1 | Non Unique | Default | RECOMMENDATION_ID, CONTEXT_TYPE |
| WLF_RECOM_CONTEXT_N2 | Non Unique | Default | ESS_JOB_ID |
| WLF_RECOM_CONTEXT_U1 | Unique | Default | RECOM_CONTEXT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
