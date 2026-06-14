# PER_ACTION_REASONS_B

This table stores all the action reasons for an action

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionreasonsb-26882.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peractionreasonsb-26882.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACTION_REASONS_B_PK | ACTION_REASON_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping |
|---|---|---|---|---|---|---|
| ACTION_REASON_ID | NUMBER |  | 18 | Yes | System generated primary key. Surrogate Key. |  |
| ACTION_REASON_CODE | VARCHAR2 | 30 |  | Yes | Uniquely identifies and action reason. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| START_DATE | DATE |  |  | Yes | The date from which the Action reason is active. |  |
| END_DATE | DATE |  |  |  | The date till when the Action Reason is active. |  |
| RSN_ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| RSN_ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. | Additional Action Reason Attributes (PER_ACT_REASONS_DFF) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ACTION_REASONS_B_N1 | Non Unique | Default | BUSINESS_GROUP_ID, ACTION_REASON_CODE |
| PER_ACTION_REASONS_B_N2 | Non Unique | Default | LAST_UPDATE_DATE |
| PER_ACTION_REASONS_B_N20 | Non Unique | Default | SGUID |
| PER_ACTION_REASONS_B_N3 | Non Unique | Default | UPPER("ACTION_REASON_CODE") |
| PER_ACTION_REASONS_B_PK | Unique | Default | ACTION_REASON_ID, ORA_SEED_SET1 |
| PER_ACTION_REASONS_B_PK1 | Unique | Default | ACTION_REASON_ID, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
