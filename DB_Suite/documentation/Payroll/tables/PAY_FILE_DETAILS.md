# PAY_FILE_DETAILS

Report file details that have been saved in the system

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payfiledetails-20406.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payfiledetails-20406.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FILE_DETAILS_PK | FILE_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILE_DETAIL_ID | NUMBER |  | 18 | Yes | System generated  Primary Key |
| SOURCE_ID | NUMBER |  | 18 | Yes | Foreign Key to an entity described by the SOURCE_TYPE column |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Denotes the source of the SOURCE_ID attribute |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| FILE_TYPE | VARCHAR2 | 30 |  | Yes | Denotes the type of file. |
| FILE_LOCATION | VARCHAR2 | 255 |  |  | The Operating System location of the file. |
| BLOB_FILE_FRAGMENT | BLOB |  |  |  | BLOB_FILE_FRAGMENT |
| FILE_FRAGMENT | CLOB |  |  |  | Whole or Partial file content |
| INTERNAL_FILE_NAME | VARCHAR2 | 240 |  |  | INTERNAL_FILE_NAME |
| SEQUENCE | NUMBER |  | 18 |  | SEQUENCE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| ORA_PART_KEY | DATE |  |  | Yes | The partition key used to determine the range interval. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_FILE_DETAILS_N1 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_FILE_DETAILS_PK | Unique | Default | FILE_DETAIL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
