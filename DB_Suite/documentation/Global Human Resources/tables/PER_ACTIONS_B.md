# PER_ACTIONS_B

This table stores actions and has  a foreign key of Action Types. Customers can add Actions for the given Action Types.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionsb-26859.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionsb-26859.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTIONS_B_PK | ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |  |
| ACTION_CODE | VARCHAR2 | 30 |  | Yes | Uniquely identifies the action. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACT_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| ACT_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Attributes (PER_ACT_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| START_DATE | DATE |  |  | Yes | The date from which the Action is active. |  |
| END_DATE | DATE |  |  |  | The date till when the action is active. |  |
| ACTION_TYPE_ID | NUMBER |  | 18 | Yes | A grouping for the action, so that similar actions can be under one type. |  |
| ACT_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER1 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER2 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER3 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER4 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER5 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER6 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER7 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER8 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER9 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER10 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER11 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER12 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER13 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER14 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER15 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER16 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER17 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER18 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER19 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMBER20 | NUMBER |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_NUMER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE1 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE2 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE3 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE4 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE5 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE6 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE7 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE8 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE9 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE10 | DATE |  |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| ACT_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Legislative Action Attributes (PER_ACT_LEG_DDF) |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| ACTION_TYPE_CODE | VARCHAR2 | 30 |  |  | Action Type Code for Seed Data |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ALL_ROLES | VARCHAR2 | 3 |  |  | Possible Values YES/NO/NULL

YES and NULL value means this Action is available for all Roles, NO means need to filter based on the ACTION_ROLE_MAPPING table |  |
| COUNTRY | VARCHAR2 | 2000 |  |  | Possible Values ALL/NULL/Comma separated Legislation code for multiple countries |  |
| DFLT_ASG_STATUS_TYPE_ID | NUMBER |  | 18 |  | DFLT_ASG_STATUS_TYPE_ID |  |
| IS_SYSTEM_ACTION | VARCHAR2 | 3 |  |  | Possible Values YES/NO |  |
| USED_IN_CONTRACT | VARCHAR2 | 30 |  |  | Signifies if this action is used for contract updates or no |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ACTIONS_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, ACTION_CODE |
| PER_ACTIONS_B_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACTIONS_B_N20 | Non Unique | Default | SGUID |
| PER_ACTIONS_B_N3 | Non Unique | Default | UPPER("ACTION_CODE") |
| PER_ACTIONS_B_N4 | Non Unique | Default | ACTION_TYPE_CODE |
| PER_ACTIONS_B_PK | Unique | Default | ACTION_ID, ORA_SEED_SET1 |
| PER_ACTIONS_B_PK1 | Unique | Default | ACTION_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
