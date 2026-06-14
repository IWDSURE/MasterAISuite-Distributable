# HRC_DL_FILE_CLOBS

This table holds information about the CLOB Objects referred in a given data set.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileclobs-5337.html#hrcdlfileclobs-5337](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlfileclobs-5337.html#hrcdlfileclobs-5337)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_FILE_CLOBS_PK | CLOB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLOB_ID | NUMBER |  | 18 | Yes | CLOB_ID, Primary Key for the table |
| DATA_SET_ID | NUMBER |  | 18 | Yes | DATA_SET_ID, FK referring HRC_DL_DATA_SETS |
| LOB_FILE_NAME | VARCHAR2 | 300 |  | Yes | File Name provided in CLOB Folder of the zip file. |
| PCLOB | CLOB |  |  |  | CLOB Content to be stored in the Data Base. |
| PCLOB_SECURE | CLOB |  |  |  | PCLOB_SECURE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_FILE_CLOBS_U1 | Unique | Default | CLOB_ID |
| HRC_DL_FILE_CLOBS_U2 | Unique | Default | DATA_SET_ID, LOB_FILE_NAME |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
