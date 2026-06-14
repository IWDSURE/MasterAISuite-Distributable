# HWM_INTERACT_SET_LNS

Stores list of questioner IDs and conditions for Attestation group set

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwminteractsetlns-30642.html#hwminteractsetlns-30642](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwminteractsetlns-30642.html#hwminteractsetlns-30642)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_INTERACT_SET_LNS_PK | ITR_SET_LN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ITR_SET_LN_ID | NUMBER |  | 18 | Yes | ITR_SET_LN_ID |
| ITR_SET_ID | NUMBER |  | 18 | Yes | ITR_SET_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PROCESSING_ORDER | NUMBER |  |  | Yes | PROCESSING_ORDER |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | QUESTIONNAIRE_ID |
| QSTNR_VERSION_NUM | NUMBER |  | 18 | Yes | QSTNR_VERSION_NUM |
| QUESTIONNAIRE_CODE | VARCHAR2 | 240 |  | Yes | QUESTIONNAIRE_CODE |
| TIME_CATEGORY_ID | NUMBER |  | 18 | Yes | TIME_CATEGORY_ID |
| TRIGGER_EVENT_CS | VARCHAR2 | 400 |  | Yes | TRIGGER_EVENT_CS |
| DISPLAY_LEVEL | VARCHAR2 | 30 |  | Yes | DISPLAY_LEVEL |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_INTERACT_SET_LNS_N1 | Non Unique | Default | ITR_SET_ID, PROCESSING_ORDER |
| HWM_INTERACT_SET_LNS_PK | Unique | FUSION_TS_TX_DATA | ITR_SET_LN_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
