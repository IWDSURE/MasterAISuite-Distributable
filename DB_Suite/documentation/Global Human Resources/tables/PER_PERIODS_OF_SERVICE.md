# PER_PERIODS_OF_SERVICE

This table stores all information related to the person?s Work Relationships. An Work Relationship denotes a formal relationship between a person and a legal employer.  Therefore, this table will hold information for employees and contingent workers.

Current design allows for a person to have multiple active ?periods of service? as long as they are for different legal entities. This is not Effective Dated.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perperiodsofservice-4169.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perperiodsofservice-4169.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERIODS_OF_SERVICE_PK | PERIOD_OF_SERVICE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| PERIOD_OF_SERVICE_ID | NUMBER |  | 18 | Yes | System generated primary key. |  | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| TERMINATION_ACCEPTED_PERSON_ID | NUMBER |  | 18 |  | Person who accepted or authorized employee termination. Foreign key to PER_PERSONS. |  | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS. |  | Active |
| DATE_START | DATE |  |  | Yes | Start date of the period of employment. |  | Active |
| ACCEPTED_TERMINATION_DATE | DATE |  |  |  | Date when termination of employment was accepted. |  | Active |
| ACTUAL_TERMINATION_DATE | DATE |  |  |  | Actual date of termination of employment. |  | Active |
| NOTIFIED_TERMINATION_DATE | DATE |  |  |  | Date when the termination of employment was noted. |  | Active |
| PROJECTED_TERMINATION_DATE | DATE |  |  |  | Projected employment termination date. |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| ADJUSTED_SVC_DATE | DATE |  |  |  | Adjusted Service Date. For example, a rehire that was part of an acquisition, all of his plans might use original hire date if rehired within 90 days of termination except a 401k plan which might use adjusted service date which was originally populated upon acquisition. |  | Active |
| PDS_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) | Active |
| PDS_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| PDS_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Work Relationship Legislative Information (PER_PPS_LEG_DDF) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Work Relationship Attributes (PER_PPS_DF) |  |
| DATE_EMPLOYEE_DATA_VERIFIED | DATE |  |  |  | Date when the employee last verified the data. |  | Active |
| FAST_PATH_EMPLOYEE | VARCHAR2 | 30 |  | Yes | Accepts values of ?Yes?  or ?No?. |  | Active |
| LAST_WORKING_DATE | DATE |  |  |  | Last Date Worked (for terminated workers). |  | Active |
| LEGAL_ENTITY_ID | NUMBER |  | 18 | Yes | Represents Legal Entity. |  | Active |
| LEGISLATION_CODE | VARCHAR2 | 150 |  | Yes | Legislation code derived from Legal Entity. |  | Active |
| ON_MILITARY_SERVICE | VARCHAR2 | 30 |  | Yes | Accepts Yes or No values. If Yes, employee is also on military service. |  | Active |
| ORIGINAL_DATE_OF_HIRE | DATE |  |  |  | Original date of hire. |  | Active |
| PERIOD_TYPE | VARCHAR2 | 30 |  | Yes | Determines whether it is a period of service for an Employee, or Contingent worker: ?E? or ?C?, or ?N?: non-worker. |  | Active |
| PRIMARY_FLAG | VARCHAR2 | 30 |  | Yes | Accepts Yes or No values. If Yes, this employment period is considered the primary for the Legal Entity. |  | Active |
| REHIRE_AUTHORIZOR | VARCHAR2 | 30 |  |  | Obsolete |  | Active |
| REHIRE_REASON | VARCHAR2 | 60 |  |  | If rehire recommendation is ?yes?, then reason from recommending person is tracked via this field. |  | Active |
| REHIRE_RECOMMENDATION | VARCHAR2 | 30 |  | Yes | Accepts Yes or No values. If Yes, person is recommended for re-hiring. |  | Active |
| WORKER_NUMBER | VARCHAR2 | 30 |  |  | Uniquely identifies an employee or contingent worker. Can be system-generated or manually populated. |  | Active |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |  |  |
| COMMENTS | VARCHAR2 | 1000 |  |  | This stores a comment associated with termination of work relationship. |  |  |
| WORKER_COMMENTS | VARCHAR2 | 1000 |  |  | This stores a worker comment associated with the Resignation Process. |  |  |
| REHIRE_AUTHORIZER_PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PERSONS. Represents the person who recommends the worker for rehire. |  |  |
| REVOKE_USER_ACCESS | VARCHAR2 | 30 |  |  | This stores user?s option of revoking user access on Termination. Values accepted are ?I? for Immediately or ?A? for After termination |  |  |
| READY_TO_CONVERT | VARCHAR2 | 10 |  |  | Column to use to convert pending worker to employee based on flag |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERIODS_OF_SERVICE_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_PERIODS_OF_SERVICE_FK2 | Non Unique | Default | REHIRE_AUTHORIZER_PERSON_ID |
| PER_PERIODS_OF_SERVICE_N2 | Non Unique | Default | TERMINATION_ACCEPTED_PERSON_ID |
| PER_PERIODS_OF_SERVICE_N3 | Non Unique | Default | PERSON_ID, PERIOD_TYPE, LEGAL_ENTITY_ID |
| PER_PERIODS_OF_SERVICE_PK | Unique | Default | PERIOD_OF_SERVICE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
