# WLF_GRW_ROLE_GUIDES_F

Table to store details of role guides.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwroleguidesf-30468.html#wlfgrwroleguidesf-30468](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwroleguidesf-30468.html#wlfgrwroleguidesf-30468)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_ROLE_GUIDES_F_PK | ROLE_GUIDE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ROLE_GUIDE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| GUIDE_ID | NUMBER |  | 18 | Yes | Id of guide associated with the role guide. |
| VISIBILITY | VARCHAR2 | 30 |  | Yes | Visibility of Role Guide (e.g. Private, Public etc.) |
| PUBLISHED_DATE | TIMESTAMP |  |  |  | Date role guide was published, i.e. changed from Draft to Active. |
| PUBLISHED_BY_ID | NUMBER |  | 18 |  | Person Id of user publishing the role guide. |
| EVALUATION_START_DATE | TIMESTAMP |  |  |  | Date on which role guide should start the evaluation. |
| PROCESSING_PRIORITY | VARCHAR2 | 30 |  |  | Priority to process the role guides. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SPLIT_CREATION_DATE | TIMESTAMP |  |  | Yes | Split Creation Date to track when the split was created. This column will be populated only on insert and defauled to System datetime. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_ROLE_GUIDES_F_N1 | Non Unique | Default | GUIDE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| WLF_GRW_ROLE_GUIDES_F_N2 | Non Unique | Default | VISIBILITY |
| WLF_GRW_ROLE_GUIDES_F_N3 | Non Unique | Default | PROCESSING_PRIORITY |
| WLF_GRW_ROLE_GUIDES_F_U1 | Unique | Default | ROLE_GUIDE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
