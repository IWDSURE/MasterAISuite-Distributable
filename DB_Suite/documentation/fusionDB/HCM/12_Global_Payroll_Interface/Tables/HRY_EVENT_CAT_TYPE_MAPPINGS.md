# HRY_EVENT_CAT_TYPE_MAPPINGS

Event Category Mappings details gives information mapping for each event category.

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventcattypemappings-20046.html#hryeventcattypemappings-20046](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventcattypemappings-20046.html#hryeventcattypemappings-20046)

## Primary Key

| Name | Columns |
|------|----------|
| HRY_EVENT_CAT_TYPE_MAPPING_PK | EVENT_CAT_TYPE_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_CAT_TYPE_MAP_ID | NUMBER |  | 18 | Yes | System generated Primary Key column |
| EVENT_CATEGORY_ID | NUMBER |  | 18 | Yes | Forein key mapping to HRY_EVENT_CATEGORIES table |
| EVENT_TYPE_ID | NUMBER |  | 18 |  | Mapping to EVENT_TYPE_ID column of HRC_EVT_TYPES table |
| DATED_TABLE_ID | NUMBER |  | 18 |  | Mapping to DATED_TABLE_ID column of PAY_DATED_TABLES |
| EVENT_FUNC_CAT_MAP_ID | NUMBER |  | 18 |  | Foreign key mapping to HRY_EVENT_FUNC_CAT_MAPPINGS_B table |
| IS_DATE_EFFECTIVE | VARCHAR2 | 1 |  | Yes | Specifies if the event category is date effective record or not. |
| KEY_NAME1 | VARCHAR2 | 60 |  |  | Name of the Key1 for event category |
| KEY_NAME2 | VARCHAR2 | 60 |  |  | Name of the Key2 for event category. |
| KEY_NAME3 | VARCHAR2 | 60 |  |  | Name of the Key3 for event category. |
| KEY_NAME4 | VARCHAR2 | 60 |  |  | Name of the Key4 for event category. |
| KEY_NAME5 | VARCHAR2 | 60 |  |  | Name of the Key4 for event category. |
| KEY_IDENTIFIER1 | VARCHAR2 | 60 |  |  | Identifier Value for the Key name |
| KEY_IDENTIFIER2 | VARCHAR2 | 60 |  |  | Identifier Valule for the Key Name. |
| KEY_IDENTIFIER3 | VARCHAR2 | 60 |  |  | Identifier Value for the Key Name. |
| KEY_IDENTIFIER_QUERY1 | VARCHAR2 | 4000 |  |  | Query for the Key Identifier Column 1 is stored. |
| KEY_IDENTIFIER_QUERY2 | VARCHAR2 | 4000 |  |  | Query for the Key Identifier Column 2 is stored. |
| KEY_IDENTIFIER_QUERY3 | VARCHAR2 | 4000 |  |  | Query for the Key Identifier Column 3 is stored. |
| PERSON_ID_QUERY | VARCHAR2 | 4000 |  |  | Query to fetch the Person ID is stored. |
| PAYROLL_ID_QUERY | VARCHAR2 | 4000 |  |  | Query to fetch Payroll Id is stored. |
| RESOLVE_QUERY | VARCHAR2 | 4000 |  |  | Query for resolving some Id based on desired value. |
| ENABLED | VARCHAR2 | 1 |  | Yes | Identifier if the event is enabled or disabled |
| EFFECTIVE_FROM | VARCHAR2 | 60 |  |  | When is the record effective from creation date or Effective from any particular date. |
| OPERATION_TYPE | VARCHAR2 | 20 |  |  | What is the type of the Operation Insert/Update/Delete |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE6 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE7 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE8 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE9 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE10 | VARCHAR2 | 250 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
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
| ACTIVE | VARCHAR2 | 1 |  |  | Identifier to describe if the row is active or inactive |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRY_EVENT_CAT_TYPE_MAPPING_N1 | Non Unique | Default | EVENT_CATEGORY_ID, EVENT_TYPE_ID |
| HRY_EVENT_CAT_TYPE_MAPPING_N2 | Non Unique | Default | EVENT_TYPE_ID |
| HRY_EVENT_CAT_TYPE_MAPPING_N3 | Non Unique | Default | EVENT_CATEGORY_ID, DATED_TABLE_ID |
| HRY_EVENT_CAT_TYPE_MAPPING_N4 | Non Unique | Default | DATED_TABLE_ID |
| HRY_EVENT_CAT_TYPE_MAPPING_PK | Unique | Default | EVENT_CAT_TYPE_MAP_ID, ORA_SEED_SET1 |
| HRY_EVENT_CAT_TYPE_MAPPING_PK1 | Unique | Default | EVENT_CAT_TYPE_MAP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../12_Global_Payroll_Interface_Tables_Index.md)
