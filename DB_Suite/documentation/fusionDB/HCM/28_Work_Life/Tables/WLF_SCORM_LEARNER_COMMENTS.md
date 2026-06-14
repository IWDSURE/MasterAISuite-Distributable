# WLF_SCORM_LEARNER_COMMENTS

Comments a user made on a content object during an attempt.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormlearnercomments-30424.html#wlfscormlearnercomments-30424](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormlearnercomments-30424.html#wlfscormlearnercomments-30424)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_LEARNER_COMMENTS_PK | LEARNER_COMMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARNER_COMMENT_ID | NUMBER |  | 18 | Yes | LEARNER_COMMENT_ID |
| ATTEMPT_INTERACTION_ID | NUMBER |  | 18 | Yes | ATTEMPT_INTERACTION_ID |
| COMMENT_SEQUENCE | NUMBER |  |  | Yes | COMMENT_SEQUENCE |
| COMMENT_LANGUAGE | VARCHAR2 | 250 |  |  | Indicates the code of the language into which the contents of the translatable columns are translated. |
| COMMENTS | VARCHAR2 | 4000 |  |  | COMMENTS |
| LOCATION | VARCHAR2 | 250 |  |  | LOCATION |
| COMMENTED_ON | VARCHAR2 | 120 |  |  | COMMENTED_ON |
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
| WLF_SCORM_LEARNER_COMMENTS_N1 | Non Unique | Default | ATTEMPT_INTERACTION_ID, COMMENT_SEQUENCE |
| WLF_SCORM_LEARNER_COMMENTS_PK | Unique | FUSION_TS_TX_DATA | LEARNER_COMMENT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
