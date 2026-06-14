# WLF_ACCESS_PERMISSIONS_F

Table to store user access permissions on Learning Items

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfaccesspermissionsf-31705.html#wlfaccesspermissionsf-31705](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfaccesspermissionsf-31705.html#wlfaccesspermissionsf-31705)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ACCESS_PERMISSIONS_PK | ACCESS_PERMISSION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCESS_PERMISSION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ACCESS_PERMISSION_NUMBER | VARCHAR2 | 30 |  |  | UserKey to uniquely identify Access Permission. |
| SS_VIEW_MODE | VARCHAR2 | 30 |  |  | Self-service view mode that is visible to the user |
| ASSIGN_FOR_SELF | VARCHAR2 | 30 |  |  | Self join assignment initial status |
| ASSIGN_AS_MANAGER | VARCHAR2 | 30 |  |  | Manager join assignment initial status |
| ADMIN_ACCESS_MODE | VARCHAR2 | 30 |  |  | Access mode in the admin work area catalog |
| MANAGE_LEARNER | VARCHAR2 | 30 |  |  | Admin access to manage learners |
| MANAGE_ADMIN | VARCHAR2 | 30 |  |  | Admin access to manage admins |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SS_ACTIVATE_ON_APPROVE | VARCHAR2 | 30 |  |  | When the SS request is approved the learning assignment is immediatly active |
| MNGR_ACTIVATE_ON_APPROVE | VARCHAR2 | 30 |  |  | When the manager request is approved the learning assignment is immediatly active |
| SS_SHOW_REQ_FORM | VARCHAR2 | 30 |  |  | Determines whether the self-service Request form should be displayed to the user. |
| MGR_SHOW_REQ_FORM | VARCHAR2 | 30 |  |  | Determines wheather the manager Request form should be displayed to the user |
| PREREQ_SELF_EVAL_TYPE | VARCHAR2 | 30 |  |  | Prereq eval type , either Deferred or Not Deferred |
| PREREQ_SELF_EVAL_DAYS | NUMBER |  |  |  | Number of days after assigned on date prereq has to be evaluated |
| PREREQ_MGR_EVAL_TYPE | VARCHAR2 | 30 |  |  | Prereq eval type , either Deferred or Not Defered |
| PREREQ_MGR_EVAL_DAYS | NUMBER |  |  |  | Number of days after assigned on date prereq has to be evaluated |
| ADMIN_VIEW_ACCESS_MODE | VARCHAR2 | 30 |  |  | This column stores various options for admin's view access mode for admin managed learning items |
| ADMIN_ADMINISTRATION_MODE | VARCHAR2 | 30 |  |  | This column stores various options for admin's administration access mode for admin managed learning items |
| INSTRUCTOR_ACCESS_MODE | VARCHAR2 | 30 |  |  | This column stores various options for Instructor's administration access mode for admin managed learning items |
| FOLLOW_COMMUNITY | VARCHAR2 | 1 |  |  | Column to hold Y or N to check if the community is followed |
| FOLLOW_SPEC | VARCHAR2 | 1 |  |  | Column to hold the values of Y or N to determine if the Specializaiton is followed |
| LRNR_ENROLL_QSTNR | VARCHAR2 | 30 |  |  | Column to enable enrollment questionnaire for learner |
| LRNR_QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Column to hold learner enrollment questionnaire id |
| MGR_ENROLL_QSTNR | VARCHAR2 | 30 |  |  | Column to enable enrollment questionnaire for manager |
| MGR_QUESTIONNAIRE_ID | NUMBER |  | 18 |  | Column to hold manager enrollment questionnaire id |
| MGR_ENROLL_COMPLETE | VARCHAR2 | 30 |  |  | Column to indicate if a learner manager can mark enrollment records complete |
| MGR_APPR_ENROLL_COMPLETE | VARCHAR2 | 30 |  |  | Column to indicate if manager needs approvals to make an enrollment complete |
| ENROLLMENT_CONDITION | VARCHAR2 | 30 |  |  | Indicates if a learner can enroll in this learning item |
| ENROLLMENT_START_DATE | TIMESTAMP |  |  |  | Column to indicate the enrollment start date |
| ENROLLMENT_END_DATE | TIMESTAMP |  |  |  | Column to indicate the enrollment end date |
| ENROLLMENT_VISIBILITY_MSS | VARCHAR2 | 30 |  |  | Column to indicate the enrollment visibility |
| WITHDRAW_RULE_ESS | VARCHAR2 | 30 |  |  | Column to indicate the withdrawal rule for learners |
| WITHDRAW_RULE_MSS | VARCHAR2 | 30 |  |  | Column to indicate the withdrawal rule for managers |
| WITHDRAW_PERIOD | VARCHAR2 | 30 |  |  | Column to indicate the period when learner can withdraw |
| WITHDRAW_PERIOD_UNITS | NUMBER |  | 18 |  | Number of units for the unit of measure of withdraw period |
| WITHDRAW_PERIOD_UOM | VARCHAR2 | 20 |  |  | Unit of Measure for withdraw period |
| WITHDRAW_PERIOD_BEFORE | VARCHAR2 | 30 |  |  | Column to indicate till when withdraw can happen |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ACCESS_PERMISSIONS_F_N1 | Non Unique | Default | ACCESS_PERMISSION_NUMBER |
| WLF_ACCESS_PERMISSIONS_F_U1 | Unique | Default | ACCESS_PERMISSION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
