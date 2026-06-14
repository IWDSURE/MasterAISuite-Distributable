# HRT_CONTENT_ITEMS_B_BK

Backup table for HRT_CONTENT_ITEMS_B

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemsbbk-14112.html#hrtcontentitemsbbk-14112](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtcontentitemsbbk-14112.html#hrtcontentitemsbbk-14112)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_CONTENT_ITEMS_B_BK_PK | INSTANCE_ID, CONTENT_ITEM_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| INSTANCE_ID | NUMBER |  | 18 | Yes | Instance Id |  |
| CONTENT_ITEM_ID | NUMBER |  | 18 | Yes | Unique identifier of Content Item | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. | Active |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to Content Type | Active |
| CONTENT_VALUE_SET_ID | NUMBER |  | 18 |  | Foreign Key to Content Type Value Sets |  |
| CONTENT_ITEM_CODE | VARCHAR2 | 30 |  |  | Content Item code | Active |
| DATE_FROM | DATE |  |  | Yes | Start date of Content Item | Active |
| DATE_TO | DATE |  |  |  | End date of Content Item | Active |
| CONTENT_SUPPLIER_CODE | VARCHAR2 | 30 |  |  | Content Supplier Code defines where the Content Item came from | Active |
| RATING_MODEL_ID | NUMBER |  | 18 |  | Foreign key to Rating Model table | Active |
| COUNTRY_ID | NUMBER |  | 18 |  | Country Id referencing HZ_GEOGRAPHIES |  |
| STATE_PROVINCE_ID | NUMBER |  | 18 |  | State Id referencing HZ_GEOGRAPHIES |  |
| CONTENT_KEYFLEX_ID | NUMBER |  | 18 |  | Content key flexfield identifier | Active |
| ITEM_NUMBER_1 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_2 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_3 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_4 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_5 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_6 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_7 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_8 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_9 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_NUMBER_10 | NUMBER |  |  |  | Number column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_1 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_2 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_3 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_4 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_5 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_6 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_7 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_8 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_9 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_DATE_10 | DATE |  |  |  | Date column in Content Item that are used in defining Content Type properties | Active |
| ITEM_TEXT_1 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_2 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_3 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_4 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_5 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_6 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_7 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_8 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_9 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_10 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_11 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_12 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_13 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_14 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_15 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_16 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_17 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_18 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_19 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_20 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_21 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_22 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_23 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_24 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_25 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_26 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_27 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_28 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_29 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| ITEM_TEXT_30 | VARCHAR2 | 30 |  |  | Non translatable Text column in Content Item that are used in defining Content Type properties. | Active |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developers descriptive flexfield structure defining column |  |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developers descriptive flexfield column |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_CONTENT_ITEMS_B_BK_PK | Unique | Default | INSTANCE_ID, CONTENT_ITEM_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_CONTENT_ITEMS_B_BK_PK1 | Unique | Default | INSTANCE_ID, CONTENT_ITEM_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
