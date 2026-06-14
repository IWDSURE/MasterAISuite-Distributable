# HWR_WLNS_QSTN_TOPIC_XREF

This table stores the wellness question and topics mapping.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstntopicxref-4459.html#hwrwlnsqstntopicxref-4459](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrwlnsqstntopicxref-4459.html#hwrwlnsqstntopicxref-4459)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_WLNS_QSTN_TOPIC_XREF_PK | QUESTION_ID, TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTION_ID | NUMBER |  | 18 | Yes | This is the id of the question. |
| TOPIC_ID | NUMBER |  | 18 | Yes | This is the wellness topic related with the question. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_WLNS_QSTN_TOPIC_XREF_U1 | Unique | Default | QUESTION_ID, TOPIC_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
