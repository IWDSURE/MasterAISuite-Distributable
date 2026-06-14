# HNS_QUESTIONNAIRE_RECORDS

HNS QUESTIONNAIRE RECORDS : This table stores questionnaire ids for HNS Entity types

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsquestionnairerecords-28445.html#hnsquestionnairerecords-28445](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsquestionnairerecords-28445.html#hnsquestionnairerecords-28445)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_QUESTIONNAIRE_RECORDS_PK | QUESTIONNAIRE_RECORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| QUESTIONNAIRE_RECORD_ID | NUMBER |  | 18 | Yes | Unique system generated identifier for Questionnaire Records |
| ENTITY_TYPE | VARCHAR2 | 32 |  | Yes | Entity type for questionnaire |
| ENTITY_ID | NUMBER |  | 18 | Yes | Entity Id for which the questionnaire is associated |
| QUESTIONNAIRE_ID | NUMBER |  | 18 | Yes | The questionnaire Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_QUESTIONNAIRE_RECORDS_U1 | Unique | FUSION_TS_TX_DATA | QUESTIONNAIRE_RECORD_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
