# PER_JOB_FAMILY_F

PER_JOB_FAMILY_F holds Job Families. Job Families enable identification of related jobs that may not reflect the same attributes as other jobs in the same grouping.   The groupings are also beneficial for reporting.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilyf-21470.html#perjobfamilyf-21470](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perjobfamilyf-21470.html#perjobfamilyf-21470)

## Primary Key

| Name | Columns |
|------|----------|
| PER_JOB_FAMILY_F_PK | JOB_FAMILY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| JOB_FAMILY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| JOB_FAMILY_CODE | VARCHAR2 | 240 |  | Yes | JobFamilyCode attribute |  |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a job family is active or inactive. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Job Family Attributes (PER_JOB_FAMILY_DFF) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_JOB_FAMILY_F_N1 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| PER_JOB_FAMILY_F_N10 | Non Unique | Default | ATTRIBUTE10 |
| PER_JOB_FAMILY_F_N2 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| PER_JOB_FAMILY_F_N21 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| PER_JOB_FAMILY_F_N22 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| PER_JOB_FAMILY_F_N23 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| PER_JOB_FAMILY_F_N24 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| PER_JOB_FAMILY_F_N25 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| PER_JOB_FAMILY_F_N3 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| PER_JOB_FAMILY_F_N31 | Non Unique | Default | ATTRIBUTE_DATE1 |
| PER_JOB_FAMILY_F_N32 | Non Unique | Default | ATTRIBUTE_DATE2 |
| PER_JOB_FAMILY_F_N33 | Non Unique | Default | ATTRIBUTE_DATE3 |
| PER_JOB_FAMILY_F_N34 | Non Unique | Default | ATTRIBUTE_DATE4 |
| PER_JOB_FAMILY_F_N35 | Non Unique | Default | ATTRIBUTE_DATE5 |
| PER_JOB_FAMILY_F_N36 | Non Unique | Default | UPPER("JOB_FAMILY_CODE") |
| PER_JOB_FAMILY_F_N4 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| PER_JOB_FAMILY_F_N5 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| PER_JOB_FAMILY_F_N6 | Non Unique | Default | ATTRIBUTE6 |
| PER_JOB_FAMILY_F_N7 | Non Unique | Default | ATTRIBUTE7 |
| PER_JOB_FAMILY_F_N8 | Non Unique | Default | ATTRIBUTE8 |
| PER_JOB_FAMILY_F_N9 | Non Unique | Default | ATTRIBUTE9 |
| PER_JOB_FAMILY_F_PK | Unique | Default | JOB_FAMILY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_JOB_FAMILY_F_U1 | Unique | Default | LAST_UPDATE_DATE, JOB_FAMILY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
