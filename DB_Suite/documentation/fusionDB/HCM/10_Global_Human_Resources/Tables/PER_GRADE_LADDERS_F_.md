# PER_GRADE_LADDERS_F_

PER_GRADE_LADDERS_F stores the grade ladder details. A Grade Ladder is a hierarchy of Grades and is used to provide the ability to define rates for the Grades or the Steps.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradeladdersf-29886.html#pergradeladdersf-29886](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradeladdersf-29886.html#pergradeladdersf-29886)

## Primary Key

| Name | Columns |
|------|----------|
| PER_GRADE_LADDERS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, GRADE_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRADE_LADDER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| GRADE_SET_ID | NUMBER |  | 18 |  | Identifier of the grade set. |
| GRADE_TYPE | VARCHAR2 | 30 |  |  | Type of the grade, for example with steps. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  |  | Indicates if a grade ladder is active or inactive. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUTO_PROGRESSION_CODE | VARCHAR2 | 30 |  |  | Indicates if workers on this ladder will be automatically progressed or if progression needs manual approval. |
| PROGRESSION_STYLE_CODE | VARCHAR2 | 30 |  |  | Indicates if this ladder allows 'Grade' or 'Grade and Step'. |
| STEP_DETERMINATION_CODE | VARCHAR2 | 30 |  |  | If Progression Style is Grade and Step, on reaching the highest step in grade or ceiling step, this column determines how the starting step in new grade needs to be determined. |
| PROGRESSION_DATE_CODE | VARCHAR2 | 30 |  |  | Create new lookup_type CMP_GSP_PROG_DT. |
| PROG_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Progression Action Occurrence. |
| PROG_ACTION_ID | NUMBER |  | 18 |  | Progression Action. |
| PROG_ACTION_REASON_ID | NUMBER |  | 18 |  | Progression Action Reason. |
| UPDATE_SALARY_FLAG | VARCHAR2 | 1 |  |  | Indicates if salary is updated along with grade or step change. |
| AUTO_SAL_CHANGE_CODE | VARCHAR2 | 30 |  |  | Indicates if salary change as a result of grade/step change is updated automatically or needs manual approval. |
| SALARY_CHANGE_DATE_CODE | VARCHAR2 | 30 |  |  | Date on which the new salary amount takes effect. |
| SALARY_CALC_METHOD_CODE | VARCHAR2 | 30 |  |  | Used to determine the new salary rate. |
| SALARY_CALC_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate salary rate. |
| SALARY_UPD_METHOD_CODE | VARCHAR2 | 30 |  |  | Indicates if the salary change will be written on the salary record or using a different payroll element. |
| SALARY_ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Payroll element in which the workers new grade or step rate is written. |
| SALARY_INPUT_VALUE_ID | NUMBER |  | 18 |  | Payroll element in which the workers new grade or step rate is written. |
| SALARY_ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Salary Action Occurrence. |
| SALARY_ACTION_ID | NUMBER |  | 18 |  | Salary Action. |
| SALARY_ACTION_REASON_ID | NUMBER |  | 18 |  | Salary Action Reason. |
| RATE_CHANGE_DATE_CODE | VARCHAR2 | 30 |  |  | Used by Rate Sync process to determine as of which date the new rate is applied. |
| ALLOW_PROG_OVERRIDE_FLAG | VARCHAR2 | 1 |  |  | don |
| ALLOW_SALARY_OVERRIDE_FLAG | VARCHAR2 | 1 |  |  | Indicates if the salary amount written by progression process can be overidden by Admin on the salary UI. |
| PROGRESSION_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate progression date. Value in this column makes sense only if progression_date_code = ' ORA_CMP_GSP_DATE_RULE' |
| SALARY_CHANGE_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate salary change date. Value in this column makes sense only if salary_change_date_code = ' ORA_CMP_GSP_DATE_RULE' |
| RATE_CHANGE_DATE_RULE_ID | NUMBER |  | 18 |  | Fast formula to calculate rate change date. Value in this column makes sense only if rate_change_date_code = ' ORA_CMP_GSP_DATE_RULE' |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group |
| GRADE_LADDER_GRP_CODE | VARCHAR2 | 30 |  |  | To combine grade ladders into groups for processing. |
| SALARY_ADJUSTMENT_TYPE_CODE | VARCHAR2 | 30 |  |  | Determines how  the salary from the ladder is adjusted. |
| RATE_SYNC_ACTION_ID | NUMBER |  | 18 |  | The ID of the action used for the salary record indicating why the salary was updated by the rate synchronization process. |
| RATE_SYNC_ACTION_REASON_ID | NUMBER |  | 18 |  | The code of the optional reason used for the salary record indicating why the record was updated by the rate synchronization process. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_GRADE_LADDERS_FN1_ | Non Unique | Default | GRADE_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE |
| PER_GRADE_LADDERS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, GRADE_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
