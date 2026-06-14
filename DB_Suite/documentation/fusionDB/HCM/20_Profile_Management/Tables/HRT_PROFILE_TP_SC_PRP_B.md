# HRT_PROFILE_TP_SC_PRP_B

Profile Type Section Properties Base table is used to save the section properties

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletpscprpb-21001.html#hrtprofiletpscprpb-21001](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletpscprpb-21001.html#hrtprofiletpscprpb-21001)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TP_SEC_PROPS_PK | SECTION_PROP_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SECTION_PROP_ID | NUMBER |  | 18 | Yes | Section Prop Id |
| ATTRIBUTE_LABEL_KEY | VARCHAR2 | 250 |  |  | To store resource bundle key for the Label. |
| INPUT_FIELD_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies user preference based on field type. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SECTION_ID | NUMBER |  | 18 | Yes | Section ID |
| FIELD_NAME | VARCHAR2 | 30 |  |  | Field Name |
| VIEW_ATTRB_NAME | VARCHAR2 | 240 |  |  | View Attribute Name |
| COLUMN_NAME | VARCHAR2 | 240 |  |  | Column Name |
| VALUE_SET_NAME | VARCHAR2 | 240 |  |  | Value Set Name |
| PROPERTY_SOURCE | VARCHAR2 | 30 |  |  | Property Source |
| REQUIRED_FLAG | VARCHAR2 | 30 |  |  | Required Flag |
| DEFAULT_VALUE | VARCHAR2 | 30 |  |  | Default Value |
| DISPLAY_FLAG | VARCHAR2 | 30 |  |  | Display Flag |
| DISPLAY_ORDER | NUMBER |  | 3 |  | Field to store the order of the property |
| SEARCH_FLAG | VARCHAR2 | 30 |  |  | Search Flag |
| SOURCE_CODE | VARCHAR2 | 30 |  |  | Source Code |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TP_SC_PRP_B_N1 | Non Unique | Default | SECTION_ID, PROPERTY_SOURCE, SOURCE_CODE, DISPLAY_ORDER |
| HRT_PROFILE_TP_SC_PRP_B_N20 | Non Unique | Default | SGUID |
| HRT_PROFILE_TP_SC_PRP_B_U1 | Unique | Default | SECTION_PROP_ID, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| HRT_PROFILE_TP_SC_PRP_B_U11 | Unique | Default | SECTION_PROP_ID, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
