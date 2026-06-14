# WLF_LEARN_RELATION_RECORDS

Table to store learn organization relation access information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelationrecords-16385.html#wlflearnrelationrecords-16385](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelationrecords-16385.html#wlflearnrelationrecords-16385)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_RELATION_RECORDS_PK | LEARN_RELATION_RECORD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEARN_RELATION_RECORD_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARN_RELATION_RECORD_NUMBER | VARCHAR2 | 30 |  |  | Learn Relation Record Number |
| RELATION_ID | NUMBER |  | 18 | Yes | Learn organization relation id |
| LEARN_OBJECT_ID | NUMBER |  | 18 | Yes | Learn organization object id |
| LEARN_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Learn organization object type. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person id |
| STATUS | VARCHAR2 | 64 |  | Yes | This column represents status of the learn relation record {ACTIVE, DELETED}. |
| IN_ELASTIC | VARCHAR2 | 1 |  |  | Indicates if access is processed to security index or not |
| LATEST_PROCESS_ID | NUMBER |  | 18 |  | Learning Organization expansion job latest process id |
| LATEST_PROCESS_DATE | TIMESTAMP |  |  |  | Learning Organization expansion job latet process date |
| FIRST_ACTIVATION_DATE | TIMESTAMP |  |  |  | Date when this participant became Active the first time |
| STATUS_CHANGE_DATE | TIMESTAMP |  |  |  | Date of last status transition |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the learn relation record active date |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the learn relation record removed date |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
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
| WLF_LEARN_RELATION_RECORDS_N1 | Non Unique | Default | LEARN_OBJECT_ID, LEARN_OBJECT_TYPE |
| WLF_LEARN_RELATION_RECORDS_N2 | Non Unique | Default | RELATION_ID |
| WLF_LEARN_RELATION_RECORDS_U1 | Unique | Default | LEARN_RELATION_RECORD_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
