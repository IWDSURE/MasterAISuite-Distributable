# PER_ADDRESSES_F

This table holds addresses for a person or for a location.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraddressesf-7340.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraddressesf-7340.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ADDRESSES_F_PK | ADDRESS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ADDRESS_ID | NUMBER |  | 18 | Yes | System generated part of the primary key. Surrogate key. |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| ADDRESS_LINE_1 | VARCHAR2 | 240 |  |  | First line of address |  |
| ADDRESS_LINE_2 | VARCHAR2 | 240 |  |  | Second line of address |  |
| ADDRESS_LINE_3 | VARCHAR2 | 240 |  |  | Third line of address |  |
| ADDRESS_LINE_4 | VARCHAR2 | 240 |  |  | Fourth line of address |  |
| BUILDING | VARCHAR2 | 240 |  |  | Building name of the address |  |
| FLOOR_NUMBER | VARCHAR2 | 40 |  |  | Floor Number of the address |  |
| TOWN_OR_CITY | VARCHAR2 | 60 |  |  | Name of the Town or City for the address |  |
| REGION_1 | VARCHAR2 | 120 |  |  | Primary region in which the address is located. |  |
| REGION_2 | VARCHAR2 | 120 |  |  | Sub-region of Region 1. |  |
| REGION_3 | VARCHAR2 | 120 |  |  | Sub-region of Region 2. |  |
| COUNTRY | VARCHAR2 | 60 |  |  | Country of the address |  |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | Postal code of the address |  |
| LONG_POSTAL_CODE | VARCHAR2 | 30 |  |  | Long postal codes are used in some countries in addition to more well-known short postal codes. |  |
| TIMEZONE_CODE | VARCHAR2 | 50 |  |  | Specifies the standard timezone boundary under which the address falls. |  |
| DERIVED_LOCALE | VARCHAR2 | 240 |  |  | Displays the area where the address is, for example City, Country or City, State, Country. The exact format varies with country, and the contents are populated from the other fields on the address |  |
| GEOMETRY | UDT |  |  |  | Specifies coordinates of the location defined by the address. Special data type required to store. |  |
| LONGITUDE | NUMBER |  |  |  | Distance between the prime meridian and an address located to its east or west, expressed in degrees and minutes. |  |
| LATITUDE | NUMBER |  |  |  | Distance between the equator and an address located to its north or south, expressed in degrees and minutes. |  |
| VALIDATION_STATUS_CODE | VARCHAR2 | 120 |  |  | Level of accuracy of an address as determined by an address provider. |  |
| PROVIDER | VARCHAR2 | 150 |  |  | Company that has validated an address. |  |
| DQ_VALIDATION_LEVEL | NUMBER |  | 1 |  | Level of validation of the address, showing confidence in address quality |  |
| ADDL_ADDRESS_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Additional Address Columns for localization development. |  |
| ADDL_ADDRESS_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Additional Address Columns for localization development. |  |
| ADDL_ADDRESS_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Additional Address Columns for localization development. |  |
| ADDL_ADDRESS_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Additional Address Columns for localization development. |  |
| ADDL_ADDRESS_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Additional Address Columns for localization development. |  |
| ADDR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive flexfield structure defining column | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE2 | VARCHAR2 | 30 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| ADDR_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Addresses Attributes (PER_ADDRESSES_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| RECORD_CREATOR | VARCHAR2 | 30 |  |  | Module Identifier for address population. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ADDRESSES_FK1 | Non Unique | Default | BUSINESS_GROUP_ID |
| PER_ADDRESSES_F_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ADDRESSES_F_N4 | Non Unique | Default | DERIVED_LOCALE |
| PER_ADDRESSES_F_N5 | Non Unique | Default | COUNTRY |
| PER_ADDRESSES_F_N6 | Non Unique | Default | UPPER("TOWN_OR_CITY") |
| PER_ADDRESSES_F_N7 | Non Unique | Default | UPPER("POSTAL_CODE") |
| PER_ADDRESSES_F_PK | Unique | Default | ADDRESS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
