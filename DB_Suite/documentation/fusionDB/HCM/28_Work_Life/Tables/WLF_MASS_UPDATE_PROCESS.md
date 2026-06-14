# WLF_MASS_UPDATE_PROCESS

Table to store language-independent information of learning item objects.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmassupdateprocess-21335.html#wlfmassupdateprocess-21335](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmassupdateprocess-21335.html#wlfmassupdateprocess-21335)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_MASS_UPDATE_PROCESS_PK | PROCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| OBJECT_TYPE | VARCHAR2 | 64 |  | Yes | Mass action object type |
| AM_DEF | VARCHAR2 | 4000 |  |  | AM Definition |
| AM_CONFIG | VARCHAR2 | 128 |  |  | AM Config |
| PROCESS_IDENTIFIER_TYPE | VARCHAR2 | 64 |  |  | mass update process identifier |
| PROCESS_IDENTIFIER_ID | NUMBER |  | 18 |  | process identifier to fetch records |
| ACTION | VARCHAR2 | 250 |  | Yes | Mass update action |
| PARAMETERS | CLOB |  |  |  | name,value pairs for mass update |
| SUBMISSION_NOTES | VARCHAR2 | 4000 |  |  | Submission notes |
| STATUS | VARCHAR2 | 64 |  |  | Status of Mass action |
| ESS_JOB_ID | NUMBER |  | 18 |  | ESS_JOB_ID |
| ESS_COMPLETION_DATE | TIMESTAMP |  |  |  | Time when ESS job is completed |
| ATTRIBUTE_NAME | VARCHAR2 | 64 |  |  | Name of the attribute |
| START_DATE | DATE |  |  |  | Date when mass update needs to run |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_MASS_UPDATE_PROCESS_U1 | Unique | Default | PROCESS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
