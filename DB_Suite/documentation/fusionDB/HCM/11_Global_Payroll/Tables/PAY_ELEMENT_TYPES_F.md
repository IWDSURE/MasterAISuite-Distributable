# PAY_ELEMENT_TYPES_F

This table contains the definitions of elements, which are the units used to build all earnings and benefits. NOTE: Users must not enter information into the Developer Descriptive Flexfield columns of this table. These are reserved for the use of localization and verticalization teams, for entry and maintenance of legislative or industry-specific data.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementtypesf-5736.html#payelementtypesf-5736](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payelementtypesf-5736.html#payelementtypesf-5736)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ELEMENT_TYPES_F_PK | ELEMENT_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ELEMENT_TYPE_ID | NUMBER |  | 18 | Yes | ELEMENT_TYPE_ID |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| ADDITIONAL_ENTRY_ALLOWED_FLAG | VARCHAR2 | 30 |  | Yes | ADDITIONAL_ENTRY_ALLOWED_FLAG |  |
| ADJUSTMENT_ONLY_FLAG | VARCHAR2 | 30 |  | Yes | ADJUSTMENT_ONLY_FLAG |  |
| CLASSIFICATION_ID | NUMBER |  | 18 | Yes | CLASSIFICATION_ID |  |
| CLOSED_FOR_ENTRY_FLAG | VARCHAR2 | 30 |  | Yes | CLOSED_FOR_ENTRY_FLAG |  |
| INDIRECT_ONLY_FLAG | VARCHAR2 | 30 |  | Yes | INDIRECT_ONLY_FLAG |  |
| MULTIPLE_ENTRIES_ALLOWED_FLAG | VARCHAR2 | 30 |  | Yes | MULTIPLE_ENTRIES_ALLOWED_FLAG |  |
| PROCESS_IN_RUN_FLAG | VARCHAR2 | 30 |  | Yes | PROCESS_IN_RUN_FLAG |  |
| PROCESSING_PRIORITY | NUMBER |  | 9 | Yes | PROCESSING_PRIORITY |  |
| PROCESSING_TYPE | VARCHAR2 | 30 |  | Yes | PROCESSING_TYPE |  |
| STANDARD_LINK_FLAG | VARCHAR2 | 30 |  | Yes | STANDARD_LINK_FLAG |  |
| USE_AT_REL_LEVEL | VARCHAR2 | 30 |  | Yes | USE_AT_REL_LEVEL |  |
| USE_AT_TERM_LEVEL | VARCHAR2 | 30 |  | Yes | USE_AT_TERM_LEVEL |  |
| USE_AT_ASG_LEVEL | VARCHAR2 | 30 |  | Yes | USE_AT_ASG_LEVEL |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| BASE_ELEMENT_NAME | VARCHAR2 | 80 |  | Yes | BASE_ELEMENT_NAME |  |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| INPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | INPUT_CURRENCY_CODE |  |
| OUTPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | OUTPUT_CURRENCY_CODE |  |
| STARTING_TIME_DEF_ID | NUMBER |  | 18 |  | STARTING_TIME_DEF_ID |  |
| ENDING_TIME_DEF_ID | NUMBER |  | 18 |  | ENDING_TIME_DEF_ID |  |
| TIME_DEFINITION_TYPE | VARCHAR2 | 1 |  |  | TIME_DEFINITION_TYPE |  |
| TIME_DEFINITION_ID | NUMBER |  | 18 |  | TIME_DEFINITION_ID |  |
| SECONDARY_CLASSIFICATION_ID | NUMBER |  | 18 |  | SECONDARY_CLASSIFICATION_ID |  |
| CATEGORY | VARCHAR2 | 30 |  |  | CATEGORY |  |
| CREATOR_TYPE | VARCHAR2 | 30 |  |  | CREATOR_TYPE |  |
| FORMULA_ID | NUMBER |  | 18 |  | FORMULA_ID |  |
| DEFAULTING_FORMULA_ID | NUMBER |  | 18 |  | DEFAULTING_FORMULA_ID |  |
| CALCULATION_FORMULA_ID | NUMBER |  | 18 |  | CALCULATION_FORMULA_ID |  |
| VALIDATION_FORMULA_ID | NUMBER |  | 18 |  | VALIDATION_FORMULA_ID |  |
| VALIDATION_OVERRIDE_MESSAGE | VARCHAR2 | 30 |  |  | VALIDATION_OVERRIDE_MESSAGE |  |
| GROSSUP_FLAG | VARCHAR2 | 30 |  |  | GROSSUP_FLAG |  |
| ITERATIVE_FLAG | VARCHAR2 | 30 |  |  | ITERATIVE_FLAG |  |
| ITERATIVE_FORMULA_ID | NUMBER |  | 18 |  | ITERATIVE_FORMULA_ID |  |
| ITERATIVE_PRIORITY | NUMBER |  | 9 |  | ITERATIVE_PRIORITY |  |
| ONCE_EACH_PERIOD_FLAG | VARCHAR2 | 1 |  |  | ONCE_EACH_PERIOD_FLAG |  |
| PROCESS_MODE | VARCHAR2 | 30 |  |  | PROCESS_MODE |  |
| PRORATION_FORMULA_ID | NUMBER |  | 18 |  | PRORATION_FORMULA_ID |  |
| PRORATION_GROUP_ID | NUMBER |  | 18 |  | PRORATION_GROUP_ID |  |
| RECALC_EVENT_GROUP_ID | NUMBER |  | 18 |  | RECALC_EVENT_GROUP_ID |  |
| DEDUCTION_TYPE_ID | NUMBER |  | 18 |  | DEDUCTION_TYPE_ID |  |
| DEDUCTION_OR_EXEMPTION | VARCHAR2 | 30 |  |  | DEDUCTION_OR_EXEMPTION |  |
| EXPEDITED_MODE | VARCHAR2 | 30 |  |  | Forms the definition of whether the Element is part of and Expedited or Non expedited Payroll Run. |  |
| PARENT_BASE_ELEMENT_NAME | VARCHAR2 | 80 |  |  | Base Name of Parent Element. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Element Type Attributes (PAY_ELEMENT_TYPES_DFF) |
| ELEMENT_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | ELEMENT_INFORMATION_CATEGORY | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| ELEMENT_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Element Type Information (PAY_ELEMENT_TYPES_DDF) |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ELEMENT_TYPES_F_N1 | Non Unique | Default | CLASSIFICATION_ID |
| PAY_ELEMENT_TYPES_F_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_ELEMENT_TYPES_F_N24 | Non Unique | Default | DEFAULTING_FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N25 | Non Unique | Default | CALCULATION_FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N26 | Non Unique | Default | VALIDATION_FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N27 | Non Unique | Default | ITERATIVE_FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N28 | Non Unique | Default | PRORATION_FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N3 | Non Unique | Default | FORMULA_ID |
| PAY_ELEMENT_TYPES_F_N4 | Non Unique | Default | UPPER("BASE_ELEMENT_NAME") |
| PAY_ELEMENT_TYPES_F_N5 | Non Unique | Default | RECALC_EVENT_GROUP_ID, ELEMENT_TYPE_ID |
| PAY_ELEMENT_TYPES_F_N6 | Non Unique | Default | PARENT_BASE_ELEMENT_NAME |
| PAY_ELEMENT_TYPES_F_PK | Unique | Default | ELEMENT_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_ELEMENT_TYPES_F_PK1 | Unique | Default | ELEMENT_TYPE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_ELEMENT_TYPES_F_UK2 | Unique | Default | BASE_ELEMENT_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_ELEMENT_TYPES_F_UK21 | Unique | Default | BASE_ELEMENT_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
