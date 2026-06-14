# HNS_SUBJECT_B

HNS SUBJECT. This is the base table for Analysis Subject.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjectb-13410.html#hnssubjectb-13410](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjectb-13410.html#hnssubjectb-13410)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_SUBJECT_B_PK | SUBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUBJECT_ID | NUMBER |  | 18 | Yes | Analysis Subject Identifier. Primary key for the table HNS_SUBJECT_B. | Active |
| SUBJECT_AREA_ID | NUMBER |  | 18 | Yes | Analysis Subject Area identifier. Foreign key for HNS_SUBJECT_AREA_B table. |  |
| SUBJECT_CODE | VARCHAR2 | 18 |  | Yes | Analysis subject code. This unique code is used for seach in UI. |  |
| DISPLAY_SEQUENCE | NUMBER |  | 18 | Yes | Display sequence for Analysis subject table. This field is editable from UI. |  |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Enabled flag.This column signifies whether the subject is enabled. |  |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag. The column signifies whether the subject is marked for deletion. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_SUBJECT_B_N1 | Non Unique | FUSION_TS_TX_DATA | SUBJECT_AREA_ID |
| HNS_SUBJECT_B_U1 | Unique | Default | SUBJECT_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
