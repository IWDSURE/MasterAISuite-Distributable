# BEN_ENTITLEMENT

BEN_ENTITLEMENT defines main absence entitlements.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benentitlement-23444.html#benentitlement-23444](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benentitlement-23444.html#benentitlement-23444)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ENTITLEMENT_PK | ENTITLEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ENTITLEMENT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | LEGISLATIVE_DATA_GROUP_ID |  |
| ENTITLEMENT_NAME | VARCHAR2 | 30 |  | Yes | Identifies the entitlement name. |  |
| DEFAULT_ENTITLEMENT | VARCHAR2 | 1 |  |  | Defines whether it is a default entitlement. |  |
| PL_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_F.PL_ID. |  |
| BAND_ENTITLEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BAND_ABS_ENTITLEMENT.BAND_ENTITLEMENT_ID. |  |
| SCHEME_TYP_CODE | VARCHAR2 | 30 |  | Yes | Defines scheme type as sicknes, maternity etc. |  |
| SCHEME_START_DATE | DATE |  |  | Yes | Start Date. |  |
| SCHEME_END_DATE | DATE |  |  |  | End Date. |  |
| SCHEME_DEFINITION_TYP_CODE | VARCHAR2 | 30 |  |  | SCHEME_DEFINITION_TYP_CODE |  |
| SCHEME_PERIOD_TYP_CODE | VARCHAR2 | 30 |  |  | Identifies the scheme period such as Calendar year, Anniversary year, Rolling etc. |  |
| EMPLOYMENT_EVENT_TYPE | VARCHAR2 | 30 |  |  | EMPLOYMENT_EVENT_TYPE |  |
| PERIOD_QUALIFYING_DATE_TYPE | VARCHAR2 | 30 |  |  | Is applicable the maternity. Defines the statutory date or leave begin date or calculated from EWC. |  |
| SCHEME_PERIOD_UOM | VARCHAR2 | 30 |  |  | Defines scheme or plan period unit of measure. |  |
| SCHEME_PERIOD_DURATION | NUMBER |  | 18 |  | Defines the scheme or plan period duration. |  |
| OVERLAP_RULE | VARCHAR2 | 30 |  |  | Defines the overlap rule for rolloing period types. |  |
| SECONDARY_PERIOD_DURATION | NUMBER |  | 18 |  | Secondary assessment period duration applicable for dual rolling period type. |  |
| SECONDARY_PERIOD_UOM | VARCHAR2 | 30 |  |  | Secondary assessment period uom applicable for dual rolling period type. |  |
| FIXED_YEAR_START_DATE | DATE |  |  |  | Calendar year start date for Fixed year period type. |  |
| ENABLE_ENTITLEMENT_PRORATION | VARCHAR2 | 1 |  |  | Represents entitlemnt proration flag. |  |
| FT_ROUNDING_CODE | VARCHAR2 | 10 |  |  | Defines the full time employee rounding code. |  |
| PT_ROUNDING_CODE | VARCHAR2 | 10 |  |  | Defines the part time employee rounding code. |  |
| DAILY_RATE_CALC_UOM | VARCHAR2 | 10 |  | Yes | Defines the unit of measure to calculate daily rate. |  |
| DAILY_RATE_CALC_PERIOD | VARCHAR2 | 10 |  | Yes | Represents the earnings period such as annual or pay period to calculate daily rate. |  |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | SCHEDULE_ID |  |
| EARNING_PERIOD_PRORATION | VARCHAR2 | 1 |  |  | Represents earning period proration flag. |  |
| WORK_PATTERN_ID | NUMBER |  | 18 |  | Represents the default work pattern. Foreign key to BEN_WORK_PATTERN.WORK_PATTERN_ID. |  |
| ABS_SCHED_WORK_PATTERN_ID | NUMBER |  | 18 |  | Represents the default absence work pattern, such as saturday and sunday. Foreign key to BEN_WORK_PATTERN.WORK_PATTERN_ID. |  |
| CALENDAR_ID | NUMBER |  | 18 |  | Represents the holidays to exclude from entitlements. Foreign key to BEN_HOLIDAY_CALENDAR. |  |
| PAY_COMPONENT_RATE_TYPE | VARCHAR2 | 30 |  |  | Represents rate type. |  |
| AVG_EARNINGS_DURATION | NUMBER |  |  |  | Average earnings duration for omp. |  |
| AVG_EARNINGS_UOM | VARCHAR2 | 10 |  |  | Average earnings uom for omp. |  |
| AVG_EARNINGS_BALANCE | VARCHAR2 | 30 |  |  | Average earnings balance for omp. |  |
| PROCESS_TYP_CODE | VARCHAR2 | 30 |  |  | Process type code. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Represents the business group id. |  |
| ENT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield structure defining column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield segment column. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| ENT_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Entitlement Attributes (BEN_ENTITLEMENT_DFF) |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| INTENDS_TO_RETURN | VARCHAR2 | 1 |  |  | Intends to return from maternity leave.
Values are 'Y' or 'N' |  |
| ITR_BAND_ENTITLEMENT_ID | NUMBER |  | 18 |  | Associated Band entitlement if employee  intends to return after maternity leave.
Foreign key to BEN_BAND_ABS_ENTITLEMENT.BAND_ENTITLEMENT_ID. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ENTITLEMENT_PK | Unique | FUSION_TS_TX_DATA | ENTITLEMENT_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
