# HRT_FEEDBACK_SUGGESTIONS_B

Feedback Suggestions table. Provides suggestions for text that can be included in documents based on user-provided context.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfeedbacksuggestionsb-12807.html#hrtfeedbacksuggestionsb-12807](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtfeedbacksuggestionsb-12807.html#hrtfeedbacksuggestionsb-12807)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_FEEDBACK_SUGGESTIONS_B_PK | SUGGESTION_ID, ENTERPRISE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUGGESTION_ID | NUMBER |  | 18 | Yes | Unique ID for the item |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| SUGGESTION_SUPPLIER_CODE | VARCHAR2 | 120 |  |  | Identifier for the item usually provided by an external source |
| SUGGESTION_TYPE | VARCHAR2 | 30 |  |  | The type of item, e.g., Development Tip or Feedback item. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | The status of the item, Active or Inactive |
| SUGGESTION_ASSOC | VARCHAR2 | 30 |  | Yes | Represents the object type that the item is associated with. |
| SUGGESTION_ASSOC_KEY1 | NUMBER |  | 18 | Yes | First key of the object that the item is associated with. |
| SUGGESTION_ASSOC_KEY2 | NUMBER |  | 18 |  | Second key of the object type that the item is associated with. |
| SUGGESTION_SUPPLIER_ID | VARCHAR2 | 30 |  |  | Item origin |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_FEEDBACK_SUGGESTIONS_B_N1 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, SUGGESTION_ASSOC, SUGGESTION_ASSOC_KEY1, SUGGESTION_ASSOC_KEY2 |
| HRT_FEEDBACK_SUGGESTIONS_B_N2 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID, SUGGESTION_ASSOC_KEY1, SUGGESTION_ASSOC_KEY2 |
| HRT_FEEDBACK_SUGGESTIONS_B_U1 | Unique | FUSION_TS_TX_DATA | SUGGESTION_ID, ENTERPRISE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
