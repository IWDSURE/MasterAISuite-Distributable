# WLF_EVENT_SOCIAL

Table to store social events on learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsocial-13006.html#wlfeventsocial-13006](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsocial-13006.html#wlfeventsocial-13006)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_EVENT_SOCIAL_PK | EVENT_SOCIAL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_SOCIAL_ID | NUMBER |  | 18 | Yes | EVENT_ATTEMPT_ID |
| RATING_DATE | TIMESTAMP |  |  |  | The most recent date the row was updated by the user. |
| COMMENTS | VARCHAR2 | 4000 |  |  | Learning Item Rating comments |
| RATING | NUMBER |  |  |  | Learning Item Rating |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| LATEST_SOCIAL_INTERACTION_ID | NUMBER |  | 18 |  | LATEST_SOCIAL_INTERACTION_ID |
| LATEST_INTERACTION_STATUS | VARCHAR2 | 30 |  |  | Latest Interaction Status |
| OBJECT_TYPE | VARCHAR2 | 30 |  |  | OBJECT_TYPE |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| DATA | VARCHAR2 | 1024 |  |  | DATA |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| EVENT_SOCIAL_NUMBER | VARCHAR2 | 30 |  |  | EVENT_SOCIAL_NUMBER |
| EVENT_SUB_TYPE | VARCHAR2 | 30 |  |  | EVENT SUB TYPE |
| SOURCE_ID | NUMBER |  | 18 |  | Catalog Learning Item ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Event sub type |
| SOURCE_SOCIAL_ID | NUMBER |  | 18 |  | SOCIAL ID for reply |
| SOURCE_SOCIAL_NUMBER | VARCHAR2 | 30 |  |  | SOURCE_SOCIAL_NUMBER |
| LIKE_COUNT | NUMBER |  | 9 |  | LIKE COUNT |
| REPLY_COUNT | NUMBER |  | 9 |  | REPLY COUNT |
| LAST_ACTED_ON_DATE | TIMESTAMP |  |  |  | The most recent date the social event has occurred. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_EVENT_SOCIAL_N1 | Non Unique | Default | EVENT_ID |
| WLF_EVENT_SOCIAL_N2 | Non Unique | Default | LATEST_SOCIAL_INTERACTION_ID |
| WLF_EVENT_SOCIAL_N3 | Non Unique | Default | EVENT_SOCIAL_NUMBER |
| WLF_EVENT_SOCIAL_N5 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| WLF_EVENT_SOCIAL_N6 | Non Unique | Default | SOURCE_SOCIAL_ID, EVENT_SUB_TYPE |
| WLF_EVENT_SOCIAL_N7 | Non Unique | Default | LAST_UPDATE_DATE |
| WLF_EVENT_SOCIAL_N8 | Non Unique | Default | OBJECT_ID |
| WLF_EVENT_SOCIAL_PK | Unique | Default | EVENT_SOCIAL_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
