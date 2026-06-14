# PER_LOCATION_DETAILS_F_

PER_LOCATION_DETAILS_F stores the location details related attributes.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsf-20916.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsf-20916.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOCATION_DETAILS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_DETAILS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ACTIVE_STATUS | VARCHAR2 | 30 |  |  | Represents whether or not the location is active. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |
| MAIN_ADDRESS_ID | NUMBER |  | 18 |  | Represents the ID of the address for the location. |
| TELEPHONE_NUMBER_1 | VARCHAR2 | 240 |  |  | Represents the main phone number for the location. |
| MAINPHONE_COUNTRY_CODE1 | VARCHAR2 | 30 |  |  | Represents the country code of the main phone number for the location. |
| MAINPHONE_AREA_CODE1 | VARCHAR2 | 60 |  |  | Represents the area code of the main phone number for the location. |
| MAINPHONE_SUBSCRIBER_NUM1 | VARCHAR2 | 60 |  |  | Represents the local number of the main phone number for the location. |
| MAINPHONE_EXTENSION1 | VARCHAR2 | 60 |  |  | Represents the extension of the main phone number for the location. |
| TELEPHONE_NUMBER_2 | VARCHAR2 | 240 |  |  | Represents the fax number for the location. |
| FAX_COUNTRY_CODE2 | VARCHAR2 | 30 |  |  | Represents the country code of the fax number for the location. |
| FAX_AREA_CODE2 | VARCHAR2 | 60 |  |  | Represents the area code of the fax number for the location. |
| FAX_SUBSCRIBER_NUM2 | VARCHAR2 | 60 |  |  | Represents the local number of the fax number for the location. |
| FAX_EXTENSION2 | VARCHAR2 | 60 |  |  | Represents the extension of the fax number for the location. |
| TELEPHONE_NUMBER_3 | VARCHAR2 | 240 |  |  | Represents the other phone number for the location. |
| OTHERPHONE_COUNTRY_CODE3 | VARCHAR2 | 30 |  |  | Represents the country code of the other phone number for the location. |
| OTHERPHONE_AREA_CODE3 | VARCHAR2 | 60 |  |  | Represents the area code of the other phone number for the location. |
| OTHERPHONE_SUBSCRIBER_NUM3 | VARCHAR2 | 60 |  |  | Represents the local number of the other phone number for the location. |
| OTHERPHONE_EXTENSION3 | VARCHAR2 | 60 |  |  | Represents the extension of the other phone number for the location. |
| OFFICIAL_LANGUAGE_CODE | VARCHAR2 | 30 |  |  | Represents the code of the location's official language. |
| EMAIL_ADDRESS | VARCHAR2 | 240 |  |  | Represents the email address of the location. |
| SHIP_TO_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a ship to site. |
| SHIP_TO_LOCATION_ID | NUMBER |  | 18 |  | Represents the ID of the ship to site location. |
| RECEIVING_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a receiving site. |
| BILL_TO_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is a bill to site. |
| OFFICE_SITE_FLAG | VARCHAR2 | 30 |  |  | Indicates the location is an office site. |
| INVENTORY_ORGANIZATION_ID | NUMBER |  | 18 |  | Represents the inventory organization id the location is attached. |
| DESIGNATED_RECEIVER_ID | NUMBER |  | 18 |  | Represents the designated receiver for this location. |
| GEO_HIERARCHY_NODE_ID | VARCHAR2 | 32 |  |  | The system identifier of a geography tree node. |
| GEO_HIERARCHY_NODE_VALUE | VARCHAR2 | 100 |  |  | The value of the of a geography tree node that this location references. |
| STANDARD_WORKING_HOURS | NUMBER |  | 22 |  | Number of standard working hours |
| STANDARD_WORKING_FREQUENCY | VARCHAR2 | 30 |  |  | Frequency for the standard working hours |
| STD_ANNUAL_WORKING_DURATION | NUMBER |  | 8 |  | The standard annual working duration for the location. |
| ANNUAL_WORKING_DURATION_UNITS | VARCHAR2 | 10 |  |  | The unit of measure in hours, days, weeks, or months for the standard annual working duration. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Specifies the standard timezone boundary under which the address falls. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LOCATION_DETAILS_FN1_ | Non Unique | Default | LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LAST_UPDATE_DATE |
| PER_LOCATION_DETAILS_F_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
