# WLF_EVENT_SOCIAL_INTERACTIONS

Table to store details of social interactions on learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsocialinteractions-9685.html#wlfeventsocialinteractions-9685](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfeventsocialinteractions-9685.html#wlfeventsocialinteractions-9685)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SOCIAL_INTERACTION_PK | EVENT_SOCIAL_INTERACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_SOCIAL_INTERACTION_ID | NUMBER |  | 18 | Yes | EVENT_ATTEMPT_ID |
| RATING_DATE | TIMESTAMP |  |  |  | The most recent date the row was updated by the user |
| COMMENTS | VARCHAR2 | 4000 |  |  | Learning Item Rating comments |
| RATING | NUMBER |  |  |  | Rating of the learning Item |
| EVENT_ID | NUMBER |  | 18 |  | EVENT_ID |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| DATA | VARCHAR2 | 1024 |  |  | DATA |
| ES_INTERACTION_CREATION_DATE | TIMESTAMP |  |  |  | ES_INTERACTION_CREATION_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SOCIAL_INTERACTION_N1 | Non Unique | Default | EVENT_ID |
| WLF_SOCIAL_INTERACTION_N2 | Non Unique | Default | ES_INTERACTION_CREATION_DATE |
| WLF_SOCIAL_INTERACTION_PK | Unique | Default | EVENT_SOCIAL_INTERACTION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
