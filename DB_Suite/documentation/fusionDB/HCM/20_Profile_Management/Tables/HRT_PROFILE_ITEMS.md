# HRT_PROFILE_ITEMS

This table contains profile items that make up a Profile. The items can be of any Content Type (Competencies, Objectives, etc.)

It contains all the Developer Descriptive Flex (DDFF) attributes where all the developer defined flex related information is stored and also contains all the Descriptive Flex (DFF) attributes where all the customer defined flex related information is stored.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileitems-28864.html#hrtprofileitems-28864](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileitems-28864.html#hrtprofileitems-28864)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_ITEMS_PK | PROFILE_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| PROFILE_ITEM_ID | NUMBER |  | 18 | Yes | System generated primary key |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| PARENT_PROFILE_ITEM_ID | NUMBER |  | 18 |  | Parent Profile Item Id |  |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILES_B |  |
| SECTION_ID | NUMBER |  | 18 |  | Foreign Key to HRT_PROFILE_TYP_SECTIONS |  |
| CONTENT_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_CONTENT_TYPES_B |  |
| CONTENT_ITEM_ID | NUMBER |  | 18 |  | Foreign Key to HRT_CONTENT_ITEMS_B |  |
| SOURCE_ID | NUMBER |  | 18 |  | Syndication source profile ID. Use this property to display the source profile of a syndicated item |  |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source Type. For example, IRC, OTA |  |
| SOURCE_KEY1 | NUMBER |  | 18 |  | Alternative Source Key |  |
| SOURCE_KEY2 | NUMBER |  | 18 |  | Alternative Source Key |  |
| SOURCE_KEY3 | NUMBER |  | 18 |  | Alternative Source Key |  |
| DATE_FROM | DATE |  |  | Yes | Date From |  |
| DATE_TO | DATE |  |  |  | Date To |  |
| QUALIFIER_ID1 | NUMBER |  | 18 |  | The instance qualifier to use for the item |  |
| QUALIFIER_ID2 | NUMBER |  | 18 |  | The instance qualifier to use for the item |  |
| COUNTRY_ID | NUMBER |  | 18 |  | Country Id referencing HZ_GEOGRAPHIES |  |
| COUNTRY_CODE | VARCHAR2 | 30 |  |  | CountryCode is based upon tables FND_TERRITORIES_VL |  |
| STATE_PROVINCE_ID | NUMBER |  | 18 |  | State Id referencing HZ_GEOGRAPHIES |  |
| STATE_PROVINCE_CODE | VARCHAR2 | 360 |  |  | StateProvinceCode is based upon tables HZ_GEOGRAPHY_IDENTIFIERS and  HZ_GEOGRAPHIES |  |
| RATING_MODEL_ID1 | NUMBER |  | 18 |  | The rating model |  |
| RATING_MODEL_ID2 | NUMBER |  | 18 |  | The rating model |  |
| RATING_MODEL_ID3 | NUMBER |  | 18 |  | The rating model |  |
| RATING_LEVEL_ID1 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |  |
| RATING_LEVEL_ID2 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |  |
| RATING_LEVEL_ID3 | NUMBER |  | 18 |  | The rating value. The values depend on the rating model selected. |  |
| INTEREST_LEVEL | VARCHAR2 | 30 |  |  | Interest level |  |
| MANDATORY | VARCHAR2 | 30 |  |  | A generic mandatory check box |  |
| IMPORTANCE | NUMBER |  | 18 |  | Relative importance. This field is used in Search and Compare Profiles |  |
| ITEM_TEXT240_1 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_2 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_3 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_4 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_5 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_6 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_7 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_8 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_9 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_10 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_11 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_12 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_13 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_14 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT240_15 | VARCHAR2 | 240 |  |  | A comments field of up to 240 characters |  |
| ITEM_TEXT2000_1 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |  |
| ITEM_TEXT2000_2 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |  |
| ITEM_TEXT2000_3 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |  |
| ITEM_TEXT2000_4 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |  |
| ITEM_TEXT2000_5 | VARCHAR2 | 2000 |  |  | A comments field of up to 2000 characters |  |
| ITEM_TEXT30_1 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_2 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_3 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_4 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_5 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_6 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_7 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_8 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_9 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_10 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_11 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_12 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_13 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_14 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_TEXT30_15 | VARCHAR2 | 30 |  |  | A comments field of up to 30 characters |  |
| ITEM_DATE_1 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_2 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_3 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_4 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_5 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_6 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_7 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_8 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_9 | DATE |  |  |  | A generic date field |  |
| ITEM_DATE_10 | DATE |  |  |  | A generic date field |  |
| ITEM_NUMBER_1 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_2 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_3 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_4 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_5 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_6 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_7 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_8 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_9 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_NUMBER_10 | NUMBER |  | 18 |  | A generic number field |  |
| ITEM_DECIMAL_1 | NUMBER |  | 15 |  | A generic decimal field |  |
| ITEM_DECIMAL_2 | NUMBER |  | 15 |  | A generic decimal field |  |
| ITEM_DECIMAL_3 | NUMBER |  | 15 |  | A generic decimal field |  |
| ITEM_DECIMAL_4 | NUMBER |  | 15 |  | A generic decimal field |  |
| ITEM_DECIMAL_5 | NUMBER |  | 15 |  | A generic decimal field |  |
| ITEM_CLOB_1 | CLOB |  |  |  | A generic CLOB field |  |
| ITEM_CLOB_2 | CLOB |  |  |  | A generic CLOB field |  |
| ITEM_CLOB_3 | CLOB |  |  |  | A generic CLOB field |  |
| ITEM_CLOB_4 | CLOB |  |  |  | A generic CLOB field |  |
| ITEM_CLOB_5 | CLOB |  |  |  | A generic CLOB field |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 80 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE1 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE2 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE3 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE4 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE5 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE6 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE7 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE8 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE9 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE10 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE11 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE12 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE13 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE14 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE15 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE16 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE17 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE18 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE19 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE20 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE21 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE22 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE23 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE24 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE25 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE26 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE27 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE28 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE29 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE30 | VARCHAR2 | 2000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Profile Items (HRT_PROFILE_ITEMS) |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Descriptive flexfield column |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_ITEMS_N1 | Non Unique | Default | PROFILE_ID, DATE_TO, DATE_FROM, RATING_LEVEL_ID1, CONTENT_ITEM_ID |
| HRT_PROFILE_ITEMS_N10 | Non Unique | Default | UPPER("ITEM_TEXT240_1"), CONTENT_TYPE_ID |
| HRT_PROFILE_ITEMS_N11 | Non Unique | Default | CONTENT_TYPE_ID, SECTION_ID, RATING_MODEL_ID1 |
| HRT_PROFILE_ITEMS_N2 | Non Unique | Default | PROFILE_ID, CONTENT_TYPE_ID, BUSINESS_GROUP_ID |
| HRT_PROFILE_ITEMS_N3 | Non Unique | Default | CONTENT_ITEM_ID |
| HRT_PROFILE_ITEMS_N4 | Non Unique | Default | PARENT_PROFILE_ITEM_ID |
| HRT_PROFILE_ITEMS_N5 | Non Unique | Default | BUSINESS_GROUP_ID, ATTRIBUTE_CATEGORY |
| HRT_PROFILE_ITEMS_N6 | Non Unique | Default | SOURCE_KEY1 |
| HRT_PROFILE_ITEMS_N7 | Non Unique | Default | SECTION_ID |
| HRT_PROFILE_ITEMS_N8 | Non Unique | Default | CONTENT_TYPE_ID, PROFILE_ID, BUSINESS_GROUP_ID, UPPER("ITEM_TEXT240_1") |
| HRT_PROFILE_ITEMS_N9 | Non Unique | HRT_PROFILE_ITEMS_N9 | SOURCE_KEY2 |
| HRT_PROFILE_ITEMS_PK | Unique | Default | PROFILE_ITEM_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
