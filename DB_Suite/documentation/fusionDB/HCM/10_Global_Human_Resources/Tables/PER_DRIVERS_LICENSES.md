# PER_DRIVERS_LICENSES

This table records drivers license details of a person

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdriverslicenses-14915.html#perdriverslicenses-14915](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdriverslicenses-14915.html#perdriverslicenses-14915)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DRIVERS_LICENSES_PK | DRIVERS_LICENSE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| DRIVERS_LICENSE_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate key. |  |  |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifies which person this row records data for. Foreign key to PER_ALL_PEOPLE_F. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | The legislation code of the driver license. It must be the same value as the ISSUING_COUNTRY value. |  |  |
| LICENSE_NUMBER | VARCHAR2 | 150 |  |  | Identifies the number for the driving license. |  |  |
| DATE_FROM | DATE |  |  |  | Start date for the drivers license. |  |  |
| DATE_TO | DATE |  |  |  | End date for the drivers license. |  |  |
| ISSUING_AUTHORITY | VARCHAR2 | 100 |  |  | Authority issuing license |  |  |
| ISSUING_COUNTRY | VARCHAR2 | 30 |  |  | Country of issue |  |  |
| ISSUING_LOCATION | VARCHAR2 | 100 |  |  | Place of issue |  |  |
| LICENSE_SUSPENDED | VARCHAR2 | 30 |  | Yes | Indicates whether license is suspended or not. |  |  |
| SUSPENDED_FROM_DATE | DATE |  |  |  | Date of suspension, if suspended |  |  |
| SUSPENDED_TO_DATE | DATE |  |  |  | Last Date of suspension, if suspended |  |  |
| NUMBER_OF_POINTS | NUMBER |  | 18 |  | Number of penalty points against license |  |  |
| VIOLATIONS | NUMBER |  | 18 |  | Number of violations |  |  |
| LIC_INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Oracle-reserved descriptive flexfield structure defining column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION1 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION2 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION3 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION4 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION5 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION6 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION7 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION8 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION9 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION10 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION11 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION12 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION13 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION14 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION15 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION16 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION17 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION18 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION19 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION20 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) | Active |
| LIC_INFORMATION21 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION22 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION23 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION24 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION25 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION26 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION27 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION28 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION29 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION30 | VARCHAR2 | 150 |  |  | Oracle-reserved descriptive flexfield column. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| LIC_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Person Drivers License Legislative Information (PER_PERSONDRIVERS_LICENSE_LEG_DDF) |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_DRIVERS_LICENSES_FK1 | Non Unique | Default | PERSON_ID |
| PER_DRIVERS_LICENSES_FK2 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_DRIVERS_LICENSES_PK | Unique | Default | DRIVERS_LICENSE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
