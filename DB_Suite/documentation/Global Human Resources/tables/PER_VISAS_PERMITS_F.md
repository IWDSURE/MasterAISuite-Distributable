# PER_VISAS_PERMITS_F

This table supports storage of visa, work permit and residency data

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pervisaspermitsf-24015.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pervisaspermitsf-24015.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_VISAS_PERMITS_PK | VISA_PERMIT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| VISA_PERMIT_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies which person this row records data for |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | The legislation code of the visa or permit. It must be the same value as the ISSUING_COUNTRY value. |  |
| VISA_PERMIT_NUMBER | VARCHAR2 | 30 |  |  | Visa or permit number |  |
| VISA_PERMIT_TYPE | VARCHAR2 | 30 |  |  | Visa or permit type |  |
| VISA_PERMIT_STATUS | VARCHAR2 | 30 |  |  | Status of visa or permit |  |
| VISA_PERMIT_STATUS_DATE | DATE |  |  |  | Date the status came into effect |  |
| VISA_PERMIT_CATEGORY | VARCHAR2 | 30 |  |  | Category of visa or permit |  |
| ISSUE_DATE | DATE |  |  |  | Date of issue of visa or permit |  |
| EXPIRATION_DATE | DATE |  |  |  | Expiration date of visa or permit |  |
| ENTRY_DATE | DATE |  |  |  | Entry date of person to the country |  |
| CURRENT_VISA_PERMIT | VARCHAR2 | 30 |  | Yes | This is an obsoleted column. |  |
| ISSUING_AUTHORITY | VARCHAR2 | 100 |  |  | Issuing authority |  |
| ISSUING_COUNTRY | VARCHAR2 | 30 |  |  | Country of issue |  |
| ISSUING_LOCATION | VARCHAR2 | 100 |  |  | Place of issue |  |
| PROFESSION | VARCHAR2 | 30 |  |  | Profession of holder |  |
| VIS_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive flexfield structure defining column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield column | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| VIS_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Visa Legislative Information (PER_PERSON_VISA_LEG_DDF) |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Visa Permit Attributes (PER_VISA_PERMIT_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_VISAS_PERMITS_FK1 | Non Unique | Default | PERSON_ID |
| PER_VISAS_PERMITS_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_VISAS_PERMITS_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_VISAS_PERMITS_F_PK | Unique | Default | VISA_PERMIT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
