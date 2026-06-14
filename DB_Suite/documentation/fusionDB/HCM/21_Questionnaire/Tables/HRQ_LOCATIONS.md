# HRQ_LOCATIONS

Table contaning  QUESTION_ID/ QSTNR_TEMPLATE_IDor QUESTIONNAIRE_ID as REFERENCE_ID and is used to classify each of them based on the geography location.

## Details

**Schema:** FUSION

**Object owner:** HRQ

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqlocations-31202.html#hrqlocations-31202](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrqlocations-31202.html#hrqlocations-31202)

## Primary Key

| Name | Columns |
|------|----------|
| HRQ_LOCATIONS_PK | HRQ_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HRQ_LOCATION_ID | NUMBER |  | 18 | Yes | Unique identifier for a location. System generated id. This attribute combined with the version number and business group id forms the primary key. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| REFERENCE_TYPE | VARCHAR2 | 240 |  | Yes | Question or Questionnaire Template or Questionnaire based on the context. |
| REFERENCE_ID | NUMBER |  | 18 | Yes | Question ID or Questionnaire Template ID or Questionnaire, based on the context. |
| REFERENCE_VERSION_NUM | NUMBER |  | 18 | Yes | Version Number of the Question or Questionnaire Template or Questionnaire, based on the context. |
| LOCATION_ID | NUMBER |  | 18 | Yes | Identifies the location id. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRQ_LOCATIONS_U1 | Unique | Default | HRQ_LOCATION_ID |

---

[← Back to Index](../21_Questionnaire_Tables_Index.md)
