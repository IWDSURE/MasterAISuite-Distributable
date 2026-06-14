# HRA_EVAL_RATINGS

This table stores the evaluation items and sections ratings

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalratings-22173.html#hraevalratings-22173](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalratings-22173.html#hraevalratings-22173)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_RATINGS_PK | EVAL_RATING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| EVAL_RATING_ID | NUMBER |  | 18 | Yes | Primary key of the Performance Rating |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| EVALUATION_ID | NUMBER |  | 18 |  | Foriegn key reference to HRA_EVALUATIONS table. |  |
| REFERENCE_ID | NUMBER |  | 18 |  | Primary key to evaluation items (when REFERENCE_TYPE is ITEM) or to evaluation sections (when REFERENCE_TYPE is SECTION) |  |
| REFERENCE_TYPE | VARCHAR2 | 240 |  |  | Indiacates the type of entity being rated. Valid values are SECTION or ITEM |  |
| PERFORMANCE_RATING_ID | NUMBER |  | 18 |  | Indicates the rating level for the performance. Uses performance rating model |  |
| PROFICIENCY_RATING_ID | NUMBER |  | 18 |  | Indicates the rating level for the proficiency. Uses proficiency rating model |  |
| EVAL_PARTICIPANT_ID | NUMBER |  | 18 |  | Any person, other than the employee/worker or manager, who participates in the performance evaluation business process. |  |
| REVIEW_POINTS | NUMBER |  | 18 |  | Indicates the corresponding review points for the rating |  |
| CALCULATED_RATING | NUMBER |  | 18 |  | Indicates the value of the rating calculated from fast formulas |  |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comments provided by the participant for an item or a section |  |
| ROLE_TYPE_CODE | VARCHAR2 | 240 |  |  | Indicates which role type has given the rating |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Evaluation Ratings (HRA_EVAL_RATINGS) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| COMMENT_TEXT | CLOB |  |  |  | Comments provided by the participant for an item or a section |  |
| JUSTIFICATION_TEXT | CLOB |  |  |  | Comments provided by Manager when manual rating and calculated rating are different. |  |
| JUSTIFICATION | VARCHAR2 | 4000 |  |  | Comments provided by Manager when manual rating and calculated rating are different. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_RATINGS_N2 | Non Unique | Default | EVAL_PARTICIPANT_ID |
| HRA_EVAL_RATINGS_N3 | Non Unique | Default | REFERENCE_ID, REFERENCE_TYPE, ROLE_TYPE_CODE |
| HRA_EVAL_RATINGS_N4 | Non Unique | Default | EVALUATION_ID, REFERENCE_TYPE, REFERENCE_ID |
| HRA_EVAL_RATINGS_PK | Unique | Default | EVAL_RATING_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
