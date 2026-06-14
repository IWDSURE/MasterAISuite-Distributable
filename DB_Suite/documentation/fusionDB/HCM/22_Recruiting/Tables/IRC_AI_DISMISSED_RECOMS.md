# IRC_AI_DISMISSED_RECOMS

Table used for tracking dismissed candidates from AI recommendations. The dismissed candidates will not be recommended for that requisition

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaidismissedrecoms-21641.html#ircaidismissedrecoms-21641](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaidismissedrecoms-21641.html#ircaidismissedrecoms-21641)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AI_DISMISSED_RECOMS_PK | AI_DISMISSED_RECOMS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AI_DISMISSED_RECOMS_ID | NUMBER |  | 18 | Yes | Identifier for the dismissed Recommendation, System generated value |
| AI_RECOMS_CONTEXT_CODE | VARCHAR2 | 60 |  | Yes | Context from where the recommendation is dismissed |
| DISMISSED_ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Represents dismissed entity type Ex:Person |
| DISMISSED_ENTITY_ID | NUMBER |  | 18 | Yes | Reference Id for the dismissed entity Ex: Candidate Person Id |
| SOURCE_ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Represents Source Entity type from where the recommendation is dismissed Ex: Requisition |
| SOURCE_ENTITY_ID | NUMBER |  | 18 | Yes | Reference Id for the source entity. Ex: Requisition id |
| REQUESTOR_ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Requestor entity type , who is dismissing the recommendation. Possible values are PERSON , REQUISITION |
| REQUESTOR_ENTITY_ID | NUMBER |  | 18 | Yes | Person Id of the logged in user who has dismissed the candidate |
| REASON_CODE | VARCHAR2 | 30 |  |  | Dismissed reason. References to lookup code ORA_AI_DISMISS_RECOMS_REASON for dismissed reason |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AI_DISMISSED_RECOMS_N1 | Non Unique | Default | DISMISSED_ENTITY_TYPE, DISMISSED_ENTITY_ID |
| IRC_AI_DISMISSED_RECOMS_N2 | Non Unique | Default | SOURCE_ENTITY_TYPE, SOURCE_ENTITY_ID |
| IRC_AI_DISMISSED_RECOMS_N3 | Non Unique | Default | AI_RECOMS_CONTEXT_CODE |
| IRC_AI_DISMISSED_RECOMS_N4 | Non Unique | Default | REQUESTOR_ENTITY_TYPE, REQUESTOR_ENTITY_ID |
| IRC_AI_DISMISSED_RECOMS_PK | Unique | Default | AI_DISMISSED_RECOMS_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
