# WLF_LM_CLASSES_B

Table to store details of classes.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassesb-4980.html#wlflmclassesb-4980](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassesb-4980.html#wlflmclassesb-4980)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_CLASSES_B_PK | CLASS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASS_ID | NUMBER |  | 18 | Yes | CLASS_ID |
| CLASS_NUMBER | VARCHAR2 | 30 |  |  | CLASS_NUMBER |
| VENDOR_ID | NUMBER |  | 18 |  | VENDOR_ID |
| COURSE_ID | NUMBER |  | 18 | Yes | COURSE_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| PARENT_CLASS_ID | NUMBER |  | 18 |  | PARENT_CLASS_ID |
| CLASS_TYPE | VARCHAR2 | 30 |  | Yes | CLASS_TYPE |
| ACTUAL_COST | NUMBER |  |  |  | ACTUAL_COST |
| BUDGET_COST | NUMBER |  |  |  | BUDGET_COST |
| BUDGET_CURRENCY_CODE | VARCHAR2 | 30 |  |  | BUDGET_CURRENCY_CODE |
| CENTRE | VARCHAR2 | 30 |  |  | CENTRE |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| END_DATE | DATE |  |  |  | END_DATE |
| END_TIME | VARCHAR2 | 5 |  |  | END_TIME |
| START_DATE | DATE |  |  |  | START_DATE |
| START_TIME | VARCHAR2 | 5 |  |  | START_TIME |
| DURATION | NUMBER |  |  |  | DURATION |
| DURATION_UNITS | VARCHAR2 | 30 |  |  | DURATION_UNITS |
| ENROLMENT_END_DATE | DATE |  |  |  | ENROLMENT_END_DATE |
| ENROLMENT_START_DATE | DATE |  |  |  | ENROLMENT_START_DATE |
| LANGUAGE_ID | NUMBER |  | 18 |  | LANGUAGE_ID |
| PUBLIC_FLAG | VARCHAR2 | 30 |  |  | PUBLIC_FLAG |
| USER_STATUS | VARCHAR2 | 80 |  |  | USER_STATUS |
| DEVELOPMENT_TYPE | VARCHAR2 | 30 |  |  | DEVELOPMENT_TYPE |
| CLASS_STATUS | VARCHAR2 | 30 |  |  | CLASS_STATUS |
| PRICE_BASIS | VARCHAR2 | 30 |  |  | PRICE_BASIS |
| SECURE_FLAG | VARCHAR2 | 30 |  |  | SECURE_FLAG |
| BOOK_INDEPENDENT_FLAG | VARCHAR2 | 30 |  |  | BOOK_INDEPENDENT_FLAG |
| CURRENCY_CODE | VARCHAR2 | 30 |  |  | CURRENCY_CODE |
| MAXIMUM_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_ATTENDEES |
| MAXIMUM_INTERNAL_ATTENDEES | NUMBER |  | 9 |  | MAXIMUM_INTERNAL_ATTENDEES |
| MINIMUM_ATTENDEES | NUMBER |  | 9 |  | MINIMUM_ATTENDEES |
| STANDARD_PRICE | NUMBER |  |  |  | STANDARD_PRICE |
| CATEGORY_CODE | VARCHAR2 | 30 |  |  | CATEGORY_CODE |
| PROJECT_ID | NUMBER |  | 18 |  | PROJECT_ID |
| OWNER_ID | NUMBER |  | 18 |  | OWNER_ID |
| LINE_ID | NUMBER |  | 18 |  | LINE_ID |
| ORG_ID | NUMBER |  | 18 |  | Indicates the identifier of the business unit associated to the row. |
| TRAINING_CENTER_ID | NUMBER |  | 18 |  | TRAINING_CENTER_ID |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| TIMEZONE | VARCHAR2 | 30 |  |  | TIMEZONE |
| DATA_SOURCE | VARCHAR2 | 30 |  |  | DATA_SOURCE |
| AVAILABILITY | VARCHAR2 | 30 |  |  | AVAILABILITY |
| DELIVERY_MODE | VARCHAR2 | 30 |  |  | DELIVERY_MODE |
| CONTENT_ID | NUMBER |  | 18 |  | CONTENT_ID |
| RELATED_CONTENT_ID | NUMBER |  | 18 |  | RELATED_CONTENT_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLS_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| CLS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| CLS_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER1 |
| CLS_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER2 |
| CLS_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER3 |
| CLS_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER4 |
| CLS_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER5 |
| CLS_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER6 |
| CLS_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER7 |
| CLS_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER8 |
| CLS_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER9 |
| CLS_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER10 |
| CLS_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER11 |
| CLS_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER12 |
| CLS_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER13 |
| CLS_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER14 |
| CLS_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER15 |
| CLS_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER16 |
| CLS_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER17 |
| CLS_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER18 |
| CLS_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER19 |
| CLS_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | CLS_ATTRIBUTE_NUMBER20 |
| CLS_ATTRIBUTE_DATE1 | DATE |  |  |  | CLS_ATTRIBUTE_DATE1 |
| CLS_ATTRIBUTE_DATE2 | DATE |  |  |  | CLS_ATTRIBUTE_DATE2 |
| CLS_ATTRIBUTE_DATE3 | DATE |  |  |  | CLS_ATTRIBUTE_DATE3 |
| CLS_ATTRIBUTE_DATE4 | DATE |  |  |  | CLS_ATTRIBUTE_DATE4 |
| CLS_ATTRIBUTE_DATE5 | DATE |  |  |  | CLS_ATTRIBUTE_DATE5 |
| CLS_ATTRIBUTE_DATE6 | DATE |  |  |  | CLS_ATTRIBUTE_DATE6 |
| CLS_ATTRIBUTE_DATE7 | DATE |  |  |  | CLS_ATTRIBUTE_DATE7 |
| CLS_ATTRIBUTE_DATE8 | DATE |  |  |  | CLS_ATTRIBUTE_DATE8 |
| CLS_ATTRIBUTE_DATE9 | DATE |  |  |  | CLS_ATTRIBUTE_DATE9 |
| CLS_ATTRIBUTE_DATE10 | DATE |  |  |  | CLS_ATTRIBUTE_DATE10 |
| CLS_ATTRIBUTE_DATE11 | DATE |  |  |  | CLS_ATTRIBUTE_DATE11 |
| CLS_ATTRIBUTE_DATE12 | DATE |  |  |  | CLS_ATTRIBUTE_DATE12 |
| CLS_ATTRIBUTE_DATE13 | DATE |  |  |  | CLS_ATTRIBUTE_DATE13 |
| CLS_ATTRIBUTE_DATE14 | DATE |  |  |  | CLS_ATTRIBUTE_DATE14 |
| CLS_ATTRIBUTE_DATE15 | DATE |  |  |  | CLS_ATTRIBUTE_DATE15 |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LM_CLASSES_B_N50 | Non Unique | Default | VENDOR_ID |
| WLF_LM_CLASSES_B_N51 | Non Unique | Default | LANGUAGE_ID |
| WLF_LM_CLASSES_B_N52 | Non Unique | Default | OWNER_ID |
| WLF_LM_CLASSES_B_N53 | Non Unique | Default | LAST_UPDATE_DATE |
| WLF_LM_CLASSES_B_U1 | Unique | Default | CLASS_ID |
| WLF_LM_CLASSES_B_U2 | Unique | Default | LINE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
