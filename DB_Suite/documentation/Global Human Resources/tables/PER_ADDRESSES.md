# PER_ADDRESSES

Address information for people.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraddresses-15456.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraddresses-15456.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ADDRESSES_PK | ADDRESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ADDRESS_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key identifier for PER_PEOPLE table. |
| DATE_FROM | DATE |  |  | Yes | Start date at the address. |
| STYLE | VARCHAR2 | 30 |  | Yes | Address style - foreign key to FND_TERRITORIES. |
| ADDRESS_LINE1 | VARCHAR2 | 240 |  |  | The first line of the address. |
| ADDRESS_LINE2 | VARCHAR2 | 240 |  |  | The second line of the address. |
| ADDRESS_LINE3 | VARCHAR2 | 240 |  |  | The third line of the address. |
| ADDRESS_TYPE | VARCHAR2 | 30 |  |  | Address type, for example, home, business, weekend. |
| COUNTRY | VARCHAR2 | 60 |  |  | Country where this address belongs. |
| DATE_TO | DATE |  |  |  | End date at this address. |
| POSTAL_CODE | VARCHAR2 | 30 |  |  | National code to identify addresses in a specific country. |
| REGION_1 | VARCHAR2 | 120 |  |  | Primary region in which the address is located. |
| REGION_2 | VARCHAR2 | 120 |  |  | Sub region of region 1 in which the address is located. |
| REGION_3 | VARCHAR2 | 120 |  |  | Sub region of region 2 in which the address is located. |
| TOWN_OR_CITY | VARCHAR2 | 30 |  |  | Name of the town or city. |
| ADDR_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ADDR_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ADD_INFORMATION13 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION14 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION15 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION16 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION17 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION18 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION19 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| ADD_INFORMATION20 | VARCHAR2 | 150 |  |  | Developers Descriptive flexfield column. |
| DERIVED_LOCALE | VARCHAR2 | 240 |  |  | Displays the area where the address is, for example City, Country or City, State, Country. The exact format varies with country, and the contents are populated from the other fields on the address |
| GEOMETRY | UDT |  |  |  | Specifies coordinates of the location defined by the address. Special datatype required to store. |
| ADDR_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADDR_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ADD_INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |
| ADD_INFORMATION30 | VARCHAR2 | 200 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ADDRESSES_PK | Unique | Default | ADDRESS_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
