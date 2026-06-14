# PER_GRADES_F

PER_GRADES_F stores the Grade definitions. Grades identify the level or rank of an employee in an organization and are also used to determine the compensation for the level or rank.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesf-23801.html#pergradesf-23801](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesf-23801.html#pergradesf-23801)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADES_F_PK | GRADE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| GRADE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| SET_ID | NUMBER |  | 18 | Yes | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| PAY_SCALE_ID | NUMBER |  | 18 |  | Foreign Key to PER_PAY_SCALES table. |  |
| STARTING_STEP | NUMBER |  | 18 |  | Indicates the starting step. |  |
| CEILING_STEP_ID | NUMBER |  | 18 |  | Identifier of the ceiling step. |  |
| GRADE_CODE | VARCHAR2 | 30 |  | Yes | Code of the grade. |  |
| GRADE_TYPE | VARCHAR2 | 30 |  | Yes | Type of the grade. |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a grade is active or inactive. |  |
| CATEGORY_CODE | VARCHAR2 | 80 |  | Yes | Extensible Flexfield Category Code |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Additional Details (PER_GRADES_DF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_GRADES_F_N11 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| PER_GRADES_F_N12 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| PER_GRADES_F_N13 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| PER_GRADES_F_N14 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| PER_GRADES_F_N15 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| PER_GRADES_F_N16 | Non Unique | Default | ATTRIBUTE6 |
| PER_GRADES_F_N17 | Non Unique | Default | ATTRIBUTE7 |
| PER_GRADES_F_N18 | Non Unique | Default | ATTRIBUTE8 |
| PER_GRADES_F_N19 | Non Unique | Default | ATTRIBUTE9 |
| PER_GRADES_F_N2 | Non Unique | FUSION_TS_TX_IDX | SET_ID |
| PER_GRADES_F_N20 | Non Unique | Default | ATTRIBUTE10 |
| PER_GRADES_F_N3 | Non Unique | FUSION_TS_TX_IDX | PAY_SCALE_ID |
| PER_GRADES_F_N31 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| PER_GRADES_F_N32 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| PER_GRADES_F_N33 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| PER_GRADES_F_N34 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| PER_GRADES_F_N35 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| PER_GRADES_F_N4 | Non Unique | Default | UPPER("GRADE_CODE") |
| PER_GRADES_F_N41 | Non Unique | Default | ATTRIBUTE_DATE1 |
| PER_GRADES_F_N42 | Non Unique | Default | ATTRIBUTE_DATE2 |
| PER_GRADES_F_N43 | Non Unique | Default | ATTRIBUTE_DATE3 |
| PER_GRADES_F_N44 | Non Unique | Default | ATTRIBUTE_DATE4 |
| PER_GRADES_F_N45 | Non Unique | Default | ATTRIBUTE_DATE5 |
| PER_GRADES_F_N5 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_GRADES_F_PK | Unique | FUSION_TS_TX_IDX | GRADE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_GRADES_F_U1 | Unique | Default | BUSINESS_GROUP_ID, SET_ID, GRADE_CODE, EFFECTIVE_START_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
