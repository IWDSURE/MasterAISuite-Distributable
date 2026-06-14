# HRA_FEEDBACK_REQUEST_OBJECTS

Feedback objects linked to requests

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackrequestobjects-9253.html#hrafeedbackrequestobjects-9253](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrafeedbackrequestobjects-9253.html#hrafeedbackrequestobjects-9253)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_FEEDBACK_REQUEST_OBJE_PK | FEEDBACK_REQ_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FEEDBACK_REQ_OBJ_ID | NUMBER |  | 18 | Yes | Primary key for the table |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| FEEDBACK_REQ_ID | NUMBER |  | 18 | Yes | Primary key of HRA_FEEDBACK_REQUEST table |
| OBJECT_ID | NUMBER |  | 18 | Yes | Business object identifier for feedback |
| OBJECT_REFERENCE_NAME | VARCHAR2 | 400 |  |  | OBJECT_REFERENCE_NAME |
| OBJECT_REFERENCE_DESCRIPTION | VARCHAR2 | 4000 |  |  | OBJECT_REFERENCE_DESCRIPTION |
| OBJECT_TYPE | VARCHAR2 | 60 |  | Yes | Business object type identifier for feedback |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_FEEDBACK_REQUEST_OBJE_N1 | Non Unique | Default | FEEDBACK_REQ_ID |
| HRA_FEEDBACK_REQUEST_OBJE_N2 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE |
| HRA_FEEDBACK_REQUEST_OBJE_PK | Unique | Default | FEEDBACK_REQ_OBJ_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
