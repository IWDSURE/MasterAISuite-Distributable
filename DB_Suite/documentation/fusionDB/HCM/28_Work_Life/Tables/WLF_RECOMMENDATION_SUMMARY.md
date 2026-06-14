# WLF_RECOMMENDATION_SUMMARY

This table stores the summary of the recommendations.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationsummary-14497.html#wlfrecommendationsummary-14497](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecommendationsummary-14497.html#wlfrecommendationsummary-14497)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOMMENDATION_SUMMARY_PK | RECOMMENDATION_SUMMARY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECOMMENDATION_SUMMARY_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| RECIPIENT_ID | NUMBER |  | 18 | Yes | Specifies the recipient of the recommendation |
| OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of the object (e.g., Learning Item, Journey, Gig, etc.,) is being recommended |
| OBJECT_CATEGORY | VARCHAR2 | 30 |  | Yes | Specifies the object category. Corresponds to the lookup code from lookup type WLF_OBJECT_CATEGORY |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | Specifies the type of the object within the category (e.g., Course, Offering, Specialization, etc., within the category "Learning Item") |
| OBJECT_SUB_TYPE | VARCHAR2 | 30 |  |  | Specifies the object sub type (e.g., Video, Book, etc., are the sub types corresponding to the object type eLearning) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOMMENDATION_SUMMARY_N1 | Non Unique | Default | OBJECT_CATEGORY, OBJECT_ID, RECIPIENT_ID |
| WLF_RECOMMENDATION_SUMMARY_N2 | Non Unique | Default | RECIPIENT_ID |
| WLF_RECOMMENDATION_SUMMARY_N3 | Non Unique | Default | OBJECT_ID |
| WLF_RECOMMENDATION_SUMMARY_N4 | Non Unique | Default | OBJECT_TYPE, OBJECT_SUB_TYPE |
| WLF_RECOMMENDATION_SUMMARY_U1 | Unique | Default | RECOMMENDATION_SUMMARY_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
