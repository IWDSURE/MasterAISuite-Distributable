# PER_PERSON_LOC_FLOW_CONFIG

This table stores person sensitive information localization seed data. Localizations can use the seed data to specify which data items they wish to hide or make mandatory on ui.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonlocflowconfig-20126.html#perpersonlocflowconfig-20126](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonlocflowconfig-20126.html#perpersonlocflowconfig-20126)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_LOC_FLOW_CONFIG_PK | PERSON_LOCALIZATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_LOCALIZATION_ID | NUMBER |  | 18 | Yes | System generated part of primary key. Surrogate key |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| LEGISLATION_CODE | VARCHAR2 | 30 |  | Yes | Identifies the legislation of the localization |
| SYSTEM_PERSON_TYPE | VARCHAR2 | 30 |  |  | System person type that localization is applied to |
| ATTRIBUTE_NAME | VARCHAR2 | 50 |  | Yes | Localization type: hide an attribute, mandate an attribute, or require an attribute to use a LOV and ect. |
| ATTRIBUTE_VALUE | VARCHAR2 | 30 |  | Yes | The value for attribute_name column. |
| ATTRIBUTE_VALUE2 | VARCHAR2 | 30 |  |  | The additional value for attribute_name column. |
| DESCRIPTION | VARCHAR2 | 300 |  |  | Describe what the localization seed data is intended for |
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
| PER_PERSON_LOC_FLOW_CONFIG_PK | Unique | FUSION_TS_SEED | PERSON_LOCALIZATION_ID, ORA_SEED_SET1 |
| PER_PERSON_LOC_FLOW_CONFIG_PK1 | Unique | FUSION_TS_SEED | PERSON_LOCALIZATION_ID, ORA_SEED_SET2 |
| PER_PERSON_LOC_FLOW_CONFI_N20 | Non Unique | Default | SGUID |
| PER_PERSON_LOC_FLOW_FK1 | Non Unique | FUSION_TS_SEED | LEGISLATION_CODE, ATTRIBUTE_NAME |
| PER_PERSON_LOC_FLOW_U1 | Unique | FUSION_TS_SEED | BUSINESS_GROUP_ID, LEGISLATION_CODE, ATTRIBUTE_NAME, SYSTEM_PERSON_TYPE, ORA_SEED_SET1 |
| PER_PERSON_LOC_FLOW_U11 | Unique | FUSION_TS_SEED | BUSINESS_GROUP_ID, LEGISLATION_CODE, ATTRIBUTE_NAME, SYSTEM_PERSON_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
