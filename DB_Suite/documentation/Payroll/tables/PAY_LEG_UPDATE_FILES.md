# PAY_LEG_UPDATE_FILES

PAY_LEG_UPDATE_FILES - contains delivered monthly updates.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatefiles-9535.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paylegupdatefiles-9535.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_LEG_UPDATE_FILES_PK | DATA_FILE_NAME, PROGRAM_UNIT |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DATA_FILE_NAME | VARCHAR2 | 30 |  | Yes | Name of data file used for legislative update. |
| PROGRAM_UNIT | VARCHAR2 | 240 |  | Yes | Program unit used to perform legislative update. |
| START_DATE_TIME | TIMESTAMP |  |  |  | Shell script data upload start date/time |
| END_DATE_TIME | TIMESTAMP |  |  |  | Shell script data upload end date/time |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_LEG_UPDATE_FILES_PK | Unique | Default | DATA_FILE_NAME, PROGRAM_UNIT |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
