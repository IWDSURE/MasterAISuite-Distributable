# PER_RATE_VALUES_F

PER_RATE_VALUES_F stores the Grade, Scale or Step Rate values for a specific Grade, Pay Scale Point or Grade Step respectively. Depending on the type of rate, the Rate_Object_Id identifies the Grade, Pay Scale Point or Grade Step for which the value is defined.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perratevaluesf-9617.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perratevaluesf-9617.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_RATE_VALUES_F_PK | RATE_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| RATE_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| RATE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_RATES_F table. |  |
| RATE_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Stores GRADE/STEP, tells whether it's Grade Rate Value or Step Rate Value |  |
| RATE_OBJECT_ID | NUMBER |  | 18 | Yes | Stores grade_id for grade rate value,  grade_step_id for step rate value |  |
| SEQUENCE | NUMBER |  | 18 |  | Included for storing sequence for grade rate values to display them in an order in UI. But the attribute is no longer used now. |  |
| MINIMUM | VARCHAR2 | 20 |  |  | Stores minimum value for a grade rate while defining grade rate range |  |
| MAXIMUM | VARCHAR2 | 20 |  |  | Stores maximum value for a grade rate while defining grade rate range |  |
| MID_VALUE | VARCHAR2 | 20 |  |  | Stores mid value(a value between minimum and maximum) for a grade rate while defining grade rate range |  |
| VALUE | VARCHAR2 | 20 |  |  | Stores the value for a grade rate/step rate |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Rate Value Additional Details (PER_RATE_VALUES_DF) |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Rate Value More Additional Details (PER_RATE_VALUES_DDF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_RATE_VALUES_F_N1 | Non Unique | APPS_TS_TX_DATA | RATE_ID |
| PER_RATE_VALUES_F_N11 | Non Unique | Default | UPPER("INFORMATION1") |
| PER_RATE_VALUES_F_N12 | Non Unique | Default | UPPER("INFORMATION2") |
| PER_RATE_VALUES_F_N13 | Non Unique | Default | UPPER("INFORMATION3") |
| PER_RATE_VALUES_F_N14 | Non Unique | Default | UPPER("INFORMATION4") |
| PER_RATE_VALUES_F_N15 | Non Unique | Default | UPPER("INFORMATION5") |
| PER_RATE_VALUES_F_N16 | Non Unique | Default | INFORMATION6 |
| PER_RATE_VALUES_F_N17 | Non Unique | Default | INFORMATION7 |
| PER_RATE_VALUES_F_N18 | Non Unique | Default | INFORMATION8 |
| PER_RATE_VALUES_F_N19 | Non Unique | Default | INFORMATION9 |
| PER_RATE_VALUES_F_N2 | Non Unique | APPS_TS_TX_DATA | RATE_OBJECT_ID |
| PER_RATE_VALUES_F_N20 | Non Unique | Default | INFORMATION10 |
| PER_RATE_VALUES_F_N31 | Non Unique | Default | INFORMATION_NUMBER1 |
| PER_RATE_VALUES_F_N32 | Non Unique | Default | INFORMATION_NUMBER2 |
| PER_RATE_VALUES_F_N33 | Non Unique | Default | INFORMATION_NUMBER3 |
| PER_RATE_VALUES_F_N34 | Non Unique | Default | INFORMATION_NUMBER4 |
| PER_RATE_VALUES_F_N35 | Non Unique | Default | INFORMATION_NUMBER5 |
| PER_RATE_VALUES_F_N4 | Non Unique | Default | RATE_OBJECT_TYPE |
| PER_RATE_VALUES_F_N41 | Non Unique | Default | INFORMATION_DATE1 |
| PER_RATE_VALUES_F_N42 | Non Unique | Default | INFORMATION_DATE2 |
| PER_RATE_VALUES_F_N43 | Non Unique | Default | INFORMATION_DATE3 |
| PER_RATE_VALUES_F_N44 | Non Unique | Default | INFORMATION_DATE4 |
| PER_RATE_VALUES_F_N45 | Non Unique | Default | INFORMATION_DATE5 |
| PER_RATE_VALUES_F_PK | Unique | Default | RATE_VALUE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
