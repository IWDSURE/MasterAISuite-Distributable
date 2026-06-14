# HCM_EXTENDED_LOOKUP_CODES_B

This table is a common repository for HCM Application. It stores the Sub Categories of various Lookup Codes of HCM Lookups.  Extended Lookup Code names are stored in its corresponding TL table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hcmextendedlookupcodesb-18032.html#hcmextendedlookupcodesb-18032](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hcmextendedlookupcodesb-18032.html#hcmextendedlookupcodesb-18032)

## Primary Key

| Name | Columns |
|------|----------|
| HCM_EXTENDED_LOOKUP_CODES_PK | EXTENDED_LOOKUP_CODE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| EXTENDED_LOOKUP_CODE_ID | NUMBER |  | 18 | Yes | System generated primary key. Uniquely identifies a record. |  |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code derived from Legal Entity. |  |
| LOOKUP_TYPE | VARCHAR2 | 30 |  | Yes | Lookup Type value |  |
| LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | Lookup Code value |  |
| EXTENDED_LOOKUP_CODE | VARCHAR2 | 30 |  | Yes | Extended Lookup code value. |  |
| INFORMATION1 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION2 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION3 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION4 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION5 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION6 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION7 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION8 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION9 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION10 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION11 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION12 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION13 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION14 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION15 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION16 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION17 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION18 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION19 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION20 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION21 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION22 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION23 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION24 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION25 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION26 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION27 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION28 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION29 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION30 | VARCHAR2 | 150 |  |  | Developer Descriptive Flexfield: segment of the developer descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_CATEGORY | VARCHAR2 | 30 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Extended Lookup Codes Legislative Information (PER_EXT_LOOKUP_CODES_LEG_DDF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HCM_EXTENDED_LOOKUP_CODES_N1 | Non Unique | Default | LOOKUP_TYPE, LOOKUP_CODE, EXTENDED_LOOKUP_CODE |
| HCM_EXTENDED_LOOKUP_CODES_PK | Unique | Default | EXTENDED_LOOKUP_CODE_ID, ORA_SEED_SET1 |
| HCM_EXTENDED_LOOKUP_CODES_PK1 | Unique | Default | EXTENDED_LOOKUP_CODE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
