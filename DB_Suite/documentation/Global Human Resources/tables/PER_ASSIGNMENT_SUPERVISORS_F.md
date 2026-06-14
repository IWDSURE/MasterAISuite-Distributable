# PER_ASSIGNMENT_SUPERVISORS_F

This stores the supervisors associated to a particular assignment. This supports different relationships established between a person and a particular supervisor. One person could have one functional manager (line manager who has absolute control over the person) and a ???project manager??? (project leader who controls a project and organizes resources/people).

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentsupervisorsf-21655.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentsupervisorsf-21655.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ASSIGNMENT_SUP_F_PK | ASSIGNMENT_SUPERVISOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| ASSIGNMENT_SUPERVISOR_ID | NUMBER |  | 18 | Yes | System-generated primary key column. Surrogate Key. |  | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  | Active |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Uniquely identifies an assignment. Foreign key to PER_ALL_ASSIGNMENTS_M. |  | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies the worker that has supervisors registered in this table. This is derived from the ASSIGNMEMT_ID record. |  | Active |
| PRIMARY_FLAG | VARCHAR2 | 30 |  | Yes | Accepts Yes or No values. If yes, then row represent main supervisor. |  | Active |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Identifies the supervisor?s assignment. Foreign Key to PER_ALL_ASSIGNMENTS_M. |  | Active |
| MANAGER_ID | NUMBER |  | 18 | Yes | Identifies supervisor. Foreign key to PER_PERSONS. This should be derived from the Manager?s assignment record. |  | Active |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Identifies the role this supervisor has with regards to the overall organization structure: functional, project leader, etc. |  | Active |
| SUP_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) | Active |
| SUP_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| SUP_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Assignment Supervisors Attributes (PER_ASG_SUPERVISOR_DF) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES |  |  |
| WORKING_PERCENTAGE | NUMBER |  | 3 |  | Percentage that person is working for supervisor |  |  |
| FREEZE_START_DATE | DATE |  |  | Yes | Represents the Deferred data freeze start date (defaulted to End of Time). |  |  |
| FREEZE_UNTIL_DATE | DATE |  |  | Yes | Represents the Deferred data freeze until date (defaulted to Start of time). |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ASSIGNMENT_SUP_F_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_ASSIGNMENT_SUP_F_N1 | Non Unique | Default | ASSIGNMENT_ID |
| PER_ASSIGNMENT_SUP_F_N2 | Non Unique | Default | MANAGER_ID |
| PER_ASSIGNMENT_SUP_F_N3 | Non Unique | Default | MANAGER_ASSIGNMENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_ASSIGNMENT_SUP_F_N4 | Non Unique | Default | PERSON_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_ASSIGNMENT_SUP_F_N5 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ASSIGNMENT_SUP_F_PK | Unique | Default | ASSIGNMENT_SUPERVISOR_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
