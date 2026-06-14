# WLF_RECOMMENDATION_CONTEXT

Table to store recommendation context attributes.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationcontext-7570.html#wlfrecommendationcontext-7570](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationcontext-7570.html#wlfrecommendationcontext-7570)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOMMENDATION_CONTEXT_PK | RECOMMENDATION_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDATION_CONTEXT_ID | NUMBER |  |  | Yes | System generated unique identifier. |
| RECOMMENDATION_ID | NUMBER |  |  | Yes | Reference to the recommendation id |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | Context attribute name |
| ATTRIBUTE_VALUE | VARCHAR2 | 100 |  |  | ATTRIBUTE_VALUE |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOMMENDATION_CONTEXT_U1 | Unique | WLF_RECOMMENDATION_CONTEXT_U1 | RECOMMENDATION_CONTEXT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
