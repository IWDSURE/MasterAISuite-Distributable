# IRC_IM_REQ_QSTNRS

This table stores all the Questionnaires used in a Requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimreqqstnrs-24848.html#ircimreqqstnrs-24848](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimreqqstnrs-24848.html#ircimreqqstnrs-24848)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_REQ_QSTNRS_PK | REQ_QSTNR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_QSTNR_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITION_B table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Foreign key to HRQ_QUESTIONNAIRES_B table. |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | Version number of the questionnaire. It identifies the specific version of the questionnaire if it is modified. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| QSTNR_TYPE_CODE | VARCHAR2 | 64 |  | Yes | This column is used to differentiate Interview Questionnaire and DQ Questionnaire. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_REQ_QSTNRS_FK1 | Non Unique | Default | REQUISITION_ID, QUESTIONNAIRE_ID |
| IRC_IM_REQ_QSTNRS_FK2 | Non Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM |
| IRC_IM_REQ_QSTNRS_PK | Unique | Default | REQ_QSTNR_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
