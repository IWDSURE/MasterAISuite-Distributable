# IRC_IM_QSTNR_INFO

IRC_IM_QSTNR_INFO table stores the questionnaire related information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimqstnrinfo-13104.html#ircimqstnrinfo-13104](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimqstnrinfo-13104.html#ircimqstnrinfo-13104)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_QSTNR_INFO_PK | QSTNR_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QSTNR_INFO_ID | NUMBER |  | 18 | Yes | Primary key for this table.  System generated |
| QSTNR_INFO_CODE | VARCHAR2 | 36 |  | Yes | Qstnr Info Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments |
| OBJECT_ID | NUMBER |  | 18 | Yes | Business Object ID - It can be FEEDBK_INFO_ID.. etc |
| OBJECT_TYPE | VARCHAR2 | 20 |  | Yes | Business Object Type - It can be INTR_SCH_FEEDBK_INFO .. etc |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | Foreign key to HRQ_QUESTIONNAIRES_B table. |
| QSTNR_TYPE_CODE | VARCHAR2 | 64 |  |  | Code for questionnaire type |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | Version number of the questionnaire. It identifies the specific version of the questionnaire if it is modified. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_QSTNR_INFO_FK1 | Non Unique | Default | QUESTIONNAIRE_ID, QSTNR_VERSION_NUM |
| IRC_IM_QSTNR_INFO_N1 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE |
| IRC_IM_QSTNR_INFO_PK | Unique | Default | QSTNR_INFO_ID |
| IRC_IM_QSTNR_INFO_U1 | Unique | Default | QSTNR_INFO_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
