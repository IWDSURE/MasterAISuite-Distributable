# PER_LOCATION_DETAILS_F

PER_LOCATION_DETAILS_F stores the location details related attributes.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsf-19296.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsf-19296.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOCATION_DETAILS_PK | LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| LOCATION_DETAILS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ACTIVE_STATUS | VARCHAR2 | 30 |  | Yes | Represents whether or not the location is active. |  |
| LOCATION_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_LOCATIONS table. |  |
| MAIN_ADDRESS_ID | NUMBER |  | 18 | Yes | Represents the ID of the address for the location. |  |
| TELEPHONE_NUMBER_1 | VARCHAR2 | 240 |  |  | Represents the main phone number for the location. |  |
| MAINPHONE_COUNTRY_CODE1 | VARCHAR2 | 30 |  |  | Represents the country code of the main phone number for the location. |  |
| MAINPHONE_AREA_CODE1 | VARCHAR2 | 60 |  |  | Represents the area code of the main phone number for the location. |  |
| MAINPHONE_SUBSCRIBER_NUM1 | VARCHAR2 | 60 |  |  | Represents the local number of the main phone number for the location. |  |
| MAINPHONE_EXTENSION1 | VARCHAR2 | 60 |  |  | Represents the extension of the main phone number for the location. |  |
| TELEPHONE_NUMBER_2 | VARCHAR2 | 240 |  |  | Represents the fax number for the location. |  |
| FAX_COUNTRY_CODE2 | VARCHAR2 | 30 |  |  | Represents the country code of the fax number for the location. |  |
| FAX_AREA_CODE2 | VARCHAR2 | 60 |  |  | Represents the area code of the fax number for the location. |  |
| FAX_SUBSCRIBER_NUM2 | VARCHAR2 | 60 |  |  | Represents the local number of the fax number for the location. |  |
| FAX_EXTENSION2 | VARCHAR2 | 60 |  |  | Represents the extension of the fax number for the location. |  |
| TELEPHONE_NUMBER_3 | VARCHAR2 | 240 |  |  | Represents the other phone number for the location. |  |
| OTHERPHONE_COUNTRY_CODE3 | VARCHAR2 | 30 |  |  | Represents the country code of the other phone number for the location. |  |
| OTHERPHONE_AREA_CODE3 | VARCHAR2 | 60 |  |  | Represents the area code of the other phone number for the location. |  |
| OTHERPHONE_SUBSCRIBER_NUM3 | VARCHAR2 | 60 |  |  | Represents the local number of the other phone number for the location. |  |
| OTHERPHONE_EXTENSION3 | VARCHAR2 | 60 |  |  | Represents the extension of the other phone number for the location. |  |
| OFFICIAL_LANGUAGE_CODE | VARCHAR2 | 30 |  |  | Represents the code of the location's official language. |  |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Represents the email address of the location. |  |
| SHIP_TO_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a ship to site. |  |
| SHIP_TO_LOCATION_ID | NUMBER |  | 18 |  | Represents the ID of the ship to site location. |  |
| RECEIVING_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a receiving site. |  |
| BILL_TO_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a bill to site. |  |
| OFFICE_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is an office site. |  |
| INVENTORY_ORGANIZATION_ID | NUMBER |  | 18 |  | Represents the inventory organization id the location is attached. |  |
| DESIGNATED_RECEIVER_ID | NUMBER |  | 18 |  | Represents the designated receiver for this location. |  |
| GEO_HIERARCHY_NODE_ID | VARCHAR2 | 32 |  |  | The system identifier of a geography tree node. |  |
| GEO_HIERARCHY_NODE_VALUE | VARCHAR2 | 100 |  |  | The value of the of a geography tree node that this location references. |  |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Number of standard working hours |  |
| STANDARD_WORKING_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the standard working hours |  |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the location. |  |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 10 |  |  | The unit of measure in hours, days, weeks, or months for the standard annual working duration. |  |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Location Attributes (PER_LOCATIONS_DF) |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Specifies the standard timezone boundary under which the address falls. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LOCATION_DETAILS_F1 | Non Unique | Default | LOCATION_ID |
| PER_LOCATION_DETAILS_F2 | Non Unique | Default | MAIN_ADDRESS_ID |
| PER_LOCATION_DETAILS_F3 | Non Unique | Default | INVENTORY_ORGANIZATION_ID |
| PER_LOCATION_DETAILS_F4 | Non Unique | Default | GEO_HIERARCHY_NODE_ID |
| PER_LOCATION_DETAILS_F5 | Non Unique | Default | SHIP_TO_LOCATION_ID |
| PER_LOCATION_DETAILS_F6 | Non Unique | Default | DESIGNATED_RECEIVER_ID |
| PER_LOCATION_DETAILS_F_N1 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| PER_LOCATION_DETAILS_F_N10 | Non Unique | Default | ATTRIBUTE10 |
| PER_LOCATION_DETAILS_F_N2 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| PER_LOCATION_DETAILS_F_N21 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| PER_LOCATION_DETAILS_F_N22 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| PER_LOCATION_DETAILS_F_N23 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| PER_LOCATION_DETAILS_F_N24 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| PER_LOCATION_DETAILS_F_N25 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| PER_LOCATION_DETAILS_F_N3 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| PER_LOCATION_DETAILS_F_N31 | Non Unique | Default | ATTRIBUTE_DATE1 |
| PER_LOCATION_DETAILS_F_N32 | Non Unique | Default | ATTRIBUTE_DATE2 |
| PER_LOCATION_DETAILS_F_N33 | Non Unique | Default | ATTRIBUTE_DATE3 |
| PER_LOCATION_DETAILS_F_N34 | Non Unique | Default | ATTRIBUTE_DATE4 |
| PER_LOCATION_DETAILS_F_N35 | Non Unique | Default | ATTRIBUTE_DATE5 |
| PER_LOCATION_DETAILS_F_N4 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| PER_LOCATION_DETAILS_F_N5 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| PER_LOCATION_DETAILS_F_N6 | Non Unique | Default | ATTRIBUTE6 |
| PER_LOCATION_DETAILS_F_N7 | Non Unique | Default | ATTRIBUTE7 |
| PER_LOCATION_DETAILS_F_N8 | Non Unique | Default | ATTRIBUTE8 |
| PER_LOCATION_DETAILS_F_N9 | Non Unique | Default | ATTRIBUTE9 |
| PER_LOCATION_DETAILS_F_U1 | Unique | Default | LAST_UPDATE_DATE, LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOCATION_DETAILS_F_U2 | Unique | Default | LOCATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOCATION_DETAILS_PK | Unique | Default | LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
