# WLF_GRW_GUIDE_RELATIONS

Table to store relations between guides and related child objects like sq guides, tasks, resources, skills etc.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguiderelations-21620.html#wlfgrwguiderelations-21620](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguiderelations-21620.html#wlfgrwguiderelations-21620)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDE_RELATIONS_PK | GUIDE_RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_RELATION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| GUIDE_RELATION_NUMBER | VARCHAR2 | 30 |  | Yes | UserKey for uniquely identifying guide relation. |
| GUIDE_ID | NUMBER |  | 18 | Yes | ID of guide associated with the relation |
| GUIDE_TYPE | VARCHAR2 | 30 |  | Yes | Type of Object Related (E.g. Task, Resources etc) |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the guide relation (e.g Active, InActive etc.) |
| RELATION_TYPE | VARCHAR2 | 30 |  | Yes | Type of Object Related (E.g. Task, Resources etc) |
| RELATED_OBJECT_CATEGORY | VARCHAR2 | 30 |  | Yes | Type of Object Related (E.g. Learning, Journey etc) |
| RELATED_OBJECT_ID | NUMBER |  | 18 | Yes | ID of the object related to guide. |
| RELATED_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Type of Object Related (E.g. Course, Journey Task etc) |
| RELATED_OBJECT_SUBTYPE | VARCHAR2 | 30 |  |  | Sub Type of Object Related (E.g. Book, Online Course, Article etc) |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Date when the relation was added to guide. |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Date when the relation was removed from guide. |
| PREV_RELATION_ID | NUMBER |  | 18 |  | ID of the predecessor relation to maintain order of position. |
| NEXT_RELATION_ID | NUMBER |  | 18 |  | ID of the successor relation to maintain order of position. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDE_RELATIONS_N1 | Non Unique | Default | GUIDE_ID, GUIDE_TYPE |
| WLF_GRW_GUIDE_RELATIONS_N2 | Non Unique | Default | RELATED_OBJECT_CATEGORY, RELATED_OBJECT_ID, RELATED_OBJECT_TYPE |
| WLF_GRW_GUIDE_RELATIONS_N3 | Non Unique | Default | RELATION_TYPE |
| WLF_GRW_GUIDE_RELATIONS_N4 | Non Unique | Default | GUIDE_RELATION_NUMBER, GUIDE_TYPE |
| WLF_GRW_GUIDE_RELATIONS_N5 | Non Unique | Default | STATUS |
| WLF_GRW_GUIDE_RELATIONS_U1 | Unique | Default | GUIDE_RELATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
