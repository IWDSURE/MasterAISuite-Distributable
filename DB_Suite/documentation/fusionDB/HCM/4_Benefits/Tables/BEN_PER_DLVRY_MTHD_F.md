# BEN_PER_DLVRY_MTHD_F

BEN_PER_DLVRY_MTHD_F  identifies the communication delivery method preferred by a person.  For example, George Green prefers to have communications delivered via email.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperdlvrymthdf-22721.html#benperdlvrymthdf-22721](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperdlvrymthdf-22721.html#benperdlvrymthdf-22721)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_DLVRY_MTHD_F_PK | PER_DLVRY_MTHD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_DLVRY_MTHD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PEOPLE_F. |
| PFD_FLAG | VARCHAR2 | 30 |  | Yes | Preferred Y or N. |
| CM_DLVRY_MTHD_CD | VARCHAR2 | 30 |  | Yes | Communication delivery method. |
| PDM_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. |
| PDM_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| PDM_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_DLVRY_MTHD_F_N1 | Non Unique | Default | PERSON_ID |
| BEN_PER_DLVRY_MTHD_F_PK | Unique | Default | PER_DLVRY_MTHD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
