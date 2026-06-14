# HNS_SUBJECT_TL

HNS SUBJECT. This multi lingual table stores analysis subject related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjecttl-23911.html#hnssubjecttl-23911](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjecttl-23911.html#hnssubjecttl-23911)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_SUBJECT_TL_PK | SUBJECT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUBJECT_ID | NUMBER |  | 18 | Yes | SUBJECT_ID column : Analysis subject primary key. | Active |
| SUBJECT_NAME | VARCHAR2 | 200 |  | Yes | SUBJECT_NAME column : Analysis subject Name. This is a multi lingual column. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |  |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag. The column signifies whether the subject is marked for deletion. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_SUBJECT_TL_UK1 | Unique | FUSION_TS_TX_DATA | SUBJECT_ID, LANGUAGE |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
