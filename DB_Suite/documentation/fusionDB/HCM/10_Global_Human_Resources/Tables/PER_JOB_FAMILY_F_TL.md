# PER_JOB_FAMILY_F_TL

Contains translated attributes of PER_JOB_FAMILY_F base table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilyftl-19501.html#perjobfamilyftl-19501](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilyftl-19501.html#perjobfamilyftl-19501)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_FAMILY_F_TL_PK | JOB_FAMILY_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| JOB_FAMILY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| JOB_FAMILY_NAME | VARCHAR2 | 240 |  | Yes | Denoted the name for the Job Family. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| PER_JOB_FAMILY_F_TL_N1 | Non Unique | FUSION_TS_TX_DATA | LANGUAGE, JOB_FAMILY_NAME | Active |
| PER_JOB_FAMILY_F_TL_N2 | Non Unique | Default | UPPER("JOB_FAMILY_NAME") |  |
| PER_JOB_FAMILY_F_TL_PK | Unique | Default | JOB_FAMILY_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |  |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
