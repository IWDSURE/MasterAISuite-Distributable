# HWR_SRVY_ACTIVE_QSTNR

This will store the information regarding which questionnaire is currently active for a particular line manager. Table specific for meeting survey. This will also store the questionaires and ownwership mapping.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyactiveqstnr-11401.html#hwrsrvyactiveqstnr-11401](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrsrvyactiveqstnr-11401.html#hwrsrvyactiveqstnr-11401)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_SRVY_ACTIVE_QSTNR_PK | SUBSCRIBER_ID, LINE_MANAGER_PRFL_ID, QUESTIONNAIRE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This is the Subscriber ID associated with the Survey. Used to differentiate between different survey projects. |
| LINE_MANAGER_PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the FUSION id of the owner of the Questionnaire. |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | This is the Questionnaire ID of the Questionnaire being identified in this record. |
| QUESTIONNAIRE_VERSION | NUMBER |  | 18 |  | This is the Questionnaire Version associated with the Questionnaire ID of this Survey |
| IS_ACTIVE | VARCHAR2 | 100 |  |  | This determines if this Questionnaire is the Active Questionnaire for the corresponding Line Manager. |
| ACTIVE_QSTNR_ATTR_1 | VARCHAR2 | 100 |  |  | ACTIVE_QSTNR_ATTR_1. This is the extra attribute in case if needed. |
| ACTIVE_QSTNR_ATTR_2 | VARCHAR2 | 100 |  |  | ACTIVE_QSTNR_ATTR_2. This is the extra attribute in case if needed. |
| ACTIVE_QSTNR_ATTR_3 | VARCHAR2 | 100 |  |  | ACTIVE_QSTNR_ATTR_3. This is the extra attribute in case if needed. |
| ACTIVE_QSTNR_ATTR_4 | VARCHAR2 | 100 |  |  | ACTIVE_QSTNR_ATTR_4. This is the extra attribute in case if needed. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_SRVY_ACTIVE_QSTNR_N1 | Non Unique | Default | IS_ACTIVE |
| HWR_SRVY_ACTIVE_QSTNR_U1 | Unique | Default | SUBSCRIBER_ID, LINE_MANAGER_PRFL_ID, QUESTIONNAIRE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
