# PER_GRADE_LADDERS_F

PER_GRADE_LADDERS_F stores the grade ladder details. A Grade Ladder is a hierarchy of Grades and is used to provide the ability to define rates for the Grades or the Steps.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradeladdersf-23346.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradeladdersf-23346.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADE_LADDERS_F_PK | GRADE_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| GRADE_LADDER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| GRADE_SET_ID | NUMBER |  | 18 | Yes | Identifier of the grade set. |  |
| GRADE_TYPE | VARCHAR2 | 30 |  | Yes | Type of the grade, for example with steps. |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Indicates if a grade ladder is active or inactive. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Grade Ladder Additional Details (PER_GRADE_LADDERS_DF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| AUTO_PROGRESSION_CODE | VARCHAR2 | 30 |  |  | Indicates if workers on this ladder will be automatically progressed or if progression needs manual approval. |  |
| PROGRESSION_STYLE_CODE | VARCHAR2 | 30 |  |  | Indicates if this ladder allows 'Grade' or 'Grade and Step'. |  |
| STEP_DETERMINATION_CODE | VARCHAR2 | 30 |  |  | If Progression Style is Grade and Step, on reaching the highest step in grade or ceiling step, this column determines how the starting step in new grade needs to be determined. |  |
| PROGRESSION_DATE_CODE | VARCHAR2 | 30 |  |  | Create new lookup_type CMP_GSP_PROG_DT. |  |
| PROG_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Progression Action Occurrence. |  |
| PROG_ACTION_ID | NUMBER |  | 18 |  | Progression Action. |  |
| PROG_ACTION_REASON_ID | NUMBER |  | 18 |  | Progression Action Reason. |  |
| UPDATE_SALARY_FLAG | VARCHAR2 | 1 |  |  | Indicates if salary is updated along with grade or step change. |  |
| AUTO_SAL_CHANGE_CODE | VARCHAR2 | 30 |  |  | Indicates if salary change as a result of grade/step change is updated automatically or needs manual approval. |  |
| SALARY_CHANGE_DATE_CODE | VARCHAR2 | 30 |  |  | Date on which the new salary amount takes effect. |  |
| SALARY_CALC_METHOD_CODE | VARCHAR2 | 30 |  |  | Used to determine the new salary rate. |  |
| SALARY_CALC_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate salary rate. |  |
| SALARY_UPD_METHOD_CODE | VARCHAR2 | 30 |  |  | Indicates if the salary change will be written on the salary record or using a different payroll element. |  |
| SALARY_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Payroll element in which the workers new grade or step rate is written. |  |
| SALARY_INPUT_VALUE_ID | NUMBER |  | 18 |  | Payroll element in which the workers new grade or step rate is written. |  |
| SALARY_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Salary Action Occurrence. |  |
| SALARY_ACTION_ID | NUMBER |  | 18 |  | Salary Action. |  |
| SALARY_ACTION_REASON_ID | NUMBER |  | 18 |  | Salary Action Reason. |  |
| RATE_CHANGE_DATE_CODE | VARCHAR2 | 30 |  |  | Used by Rate Sync process to determine as of which date the new rate is applied. |  |
| ALLOW_PROG_OVERRIDE_FLAG | VARCHAR2 | 1 |  |  | don |  |
| ALLOW_SALARY_OVERRIDE_FLAG | VARCHAR2 | 1 |  |  | Indicates if the salary amount written by progression process can be overidden by Admin on the salary UI. |  |
| PROGRESSION_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate progression date. Value in this column makes sense only if progression_date_code = ' ORA_CMP_GSP_DATE_RULE' |  |
| SALARY_CHANGE_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate salary change date. Value in this column makes sense only if salary_change_date_code = ' ORA_CMP_GSP_DATE_RULE' |  |
| RATE_CHANGE_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate rate change date. Value in this column makes sense only if rate_change_date_code = ' ORA_CMP_GSP_DATE_RULE' |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group |  |
| GRADE_LADDER_GRP_CODE | VARCHAR2 | 30 |  |  | To combine grade ladders into groups for processing. |  |
| SALARY_ADJUSTMENT_TYPE_CODE | VARCHAR2 | 30 |  |  | Determines how  the salary from the ladder is adjusted. |  |
| RATE_SYNC_ACTION_ID | NUMBER |  | 18 |  | The ID of the action used for the salary record indicating why the salary was updated by the rate synchronization process. |  |
| RATE_SYNC_ACTION_REASON_ID | NUMBER |  | 18 |  | The code of the optional reason used for the salary record indicating why the record was updated by the rate synchronization process. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_GRADE_LADDERS_F_N1 | Non Unique | APPS_TS_TX_DATA | GRADE_SET_ID |
| PER_GRADE_LADDERS_F_N11 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| PER_GRADE_LADDERS_F_N12 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| PER_GRADE_LADDERS_F_N13 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| PER_GRADE_LADDERS_F_N14 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| PER_GRADE_LADDERS_F_N15 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| PER_GRADE_LADDERS_F_N16 | Non Unique | Default | ATTRIBUTE6 |
| PER_GRADE_LADDERS_F_N17 | Non Unique | Default | ATTRIBUTE7 |
| PER_GRADE_LADDERS_F_N18 | Non Unique | Default | ATTRIBUTE8 |
| PER_GRADE_LADDERS_F_N19 | Non Unique | Default | ATTRIBUTE9 |
| PER_GRADE_LADDERS_F_N2 | Non Unique | Default | GRADE_LADDER_GRP_CODE |
| PER_GRADE_LADDERS_F_N20 | Non Unique | Default | ATTRIBUTE10 |
| PER_GRADE_LADDERS_F_N31 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| PER_GRADE_LADDERS_F_N32 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| PER_GRADE_LADDERS_F_N33 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| PER_GRADE_LADDERS_F_N34 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| PER_GRADE_LADDERS_F_N35 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| PER_GRADE_LADDERS_F_N41 | Non Unique | Default | ATTRIBUTE_DATE1 |
| PER_GRADE_LADDERS_F_N42 | Non Unique | Default | ATTRIBUTE_DATE2 |
| PER_GRADE_LADDERS_F_N43 | Non Unique | Default | ATTRIBUTE_DATE3 |
| PER_GRADE_LADDERS_F_N44 | Non Unique | Default | ATTRIBUTE_DATE4 |
| PER_GRADE_LADDERS_F_N45 | Non Unique | Default | ATTRIBUTE_DATE5 |
| PER_GRADE_LADDERS_F_PK | Unique | Default | GRADE_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
