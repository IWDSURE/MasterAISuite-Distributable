# WLF_RECOM_STATUS_SCOPE

This table stores the details of the recommendation status scopes.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomstatusscope-5825.html#wlfrecomstatusscope-5825](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfrecomstatusscope-5825.html#wlfrecomstatusscope-5825)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECOM_STATUS_SCOPE_PK | STATUS_SCOPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STATUS_SCOPE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RECOMMENDATION_SUMMARY_ID | NUMBER |  |  | Yes | Reference to the recommendation summary row. |
| STATUS | VARCHAR2 | 30 |  | Yes | Specifies the status for defining the scope. |
| STATUS_EXPIRY_DATE | DATE |  |  |  | Specifies the date after which the scope for the status will be expired. |
| SCOPE | VARCHAR2 | 30 |  | Yes | Specifies if the status scope is for a specific category or across all categories (e.g., ALL or CATEGORY) |
| SCOPE_VALUE | VARCHAR2 | 30 |  |  | Specifies the value for the scope i.e., for which specific category the scope is applicable. |
| SCOPE_START_DATE | TIMESTAMP |  |  | Yes | Specifies the date from which the scope for the status is effective. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECOM_STATUS_SCOPE_N1 | Non Unique | Default | RECOMMENDATION_SUMMARY_ID, SCOPE_START_DATE, STATUS_EXPIRY_DATE |
| WLF_RECOM_STATUS_SCOPE_N2 | Non Unique | Default | SCOPE_START_DATE |
| WLF_RECOM_STATUS_SCOPE_N3 | Non Unique | Default | STATUS_EXPIRY_DATE |
| WLF_RECOM_STATUS_SCOPE_U1 | Unique | Default | STATUS_SCOPE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
