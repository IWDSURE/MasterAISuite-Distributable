# IRC_IM_AUTO_FDBK_QSTNRS

This table stores the questionnaries selected during the automatic Collect Feedback action in CSP Configuration.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimautofdbkqstnrs-7868.html#ircimautofdbkqstnrs-7868](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimautofdbkqstnrs-7868.html#ircimautofdbkqstnrs-7868)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_AUTO_FDBK_QSTNRS_PK | AUTO_FDBK_QSTNRS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_FDBK_QSTNRS_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| AUTO_FDBK_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_IM_AUTO_FDBK_CONFIG table. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Foreign key to HRQ_QUESTIONNAIRES_B table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CODE | VARCHAR2 | 240 |  | Yes | Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_AUTO_FDBK_QSTNRS_FK1 | Non Unique | Default | AUTO_FDBK_CONFIG_ID |
| IRC_IM_AUTO_FDBK_QSTNRS_FK2 | Non Unique | Default | QUESTIONNAIRE_ID |
| IRC_IM_AUTO_FDBK_QSTNRS_PK | Unique | Default | AUTO_FDBK_QSTNRS_ID |
| IRC_IM_AUTO_FDBK_QSTNRS_U1 | Unique | Default | CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
