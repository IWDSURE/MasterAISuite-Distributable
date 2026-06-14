# PAY_MARKED_OBJECTS

This Table is used to capture the unprocessed business objects.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymarkedobjects-28692.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paymarkedobjects-28692.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_MARKED_OBJECTS_PK | PAY_MARKED_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_MARKED_OBJECT_ID | NUMBER |  | 18 | Yes | PAY_MARKED_OBJECT_ID |
| OBJECT_TYPE | VARCHAR2 | 50 |  |  | OBJECT_TYPE |
| OBJECT_ID | NUMBER |  | 18 |  | OBJECT_ID |
| PARAM1 | VARCHAR2 | 128 |  |  | PARAM1 |
| PARAM2 | VARCHAR2 | 128 |  |  | PARAM2 |
| PARAM3 | VARCHAR2 | 128 |  |  | PARAM3 |
| PARAM4 | VARCHAR2 | 128 |  |  | PARAM4 |
| PARAM5 | VARCHAR2 | 128 |  |  | PARAM5 |
| PARAM6 | VARCHAR2 | 128 |  |  | PARAM6 |
| PARAM7 | VARCHAR2 | 128 |  |  | PARAM7 |
| PARAM8 | VARCHAR2 | 128 |  |  | PARAM8 |
| PARAM9 | VARCHAR2 | 128 |  |  | PARAM9 |
| PARAM10 | VARCHAR2 | 128 |  |  | PARAM10 |
| ACTION | VARCHAR2 | 20 |  |  | ACTION |
| EDITION_NAME | VARCHAR2 | 128 |  |  | Identifier of the currently active marked objects. |
| STATUS | VARCHAR2 | 20 |  |  | STATUS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_MARKED_OBJECTS_N1 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE |
| PAY_MARKED_OBJECTS_N2 | Non Unique | Default | OBJECT_TYPE, ACTION |
| PAY_MARKED_OBJECTS_PK | Unique | Default | PAY_MARKED_OBJECT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
