# HR_ALL_ORGANIZATION_UNITS_F

This is the master table which holds all the organization IDs.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallorganizationunitsf-18857.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallorganizationunitsf-18857.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ALL_ORGANIZATION_UNITS_PK | ORGANIZATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |  | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |  |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  | Active |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  | Active |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_ACTION_OCCURRENCES. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  | Active |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Represents a legl entity. |  |  |
| ESTABLISHMENT_ID | NUMBER |  | 18 |  | Foreign Key to HRT_ESTABLISHMENTS_B |  |  |
| INTERNAL_EXTERNAL_FLAG | VARCHAR2 | 30 |  |  | Indicates if the organization is internal or external. |  | Active |
| TYPE | VARCHAR2 | 30 |  |  | This is a user defined type for differentiating between organizations. For example you many want to differentiate between different kinds of Departments, say as Health and Safety , Service Departments, Training. |  | Active |
| INTERNAL_ADDRESS_LINE | VARCHAR2 | 80 |  |  | Internal address of the organization. |  | Active |
| COST_ALLOCATION_KEYFLEX_ID | NUMBER |  | 18 |  | Key flex structure identifier for cost allocation. |  | Active |
| LOCATION_ID | NUMBER |  | 18 |  | Identifier of location to which the Organization Unit belongs. |  | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Organization Attributes (PER_ORGANIZATION_UNIT_DFF) | Active |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  | Active |
| ORGANIZATION_CODE | VARCHAR2 | 500 |  |  | Code of the organization. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  | Active |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ALL_ORGANIZATION_UNITS_PK | Unique | FUSION_TS_TX_IDX | ORGANIZATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ALL_ORG_UNITS_F_U1 | Unique | Default | LAST_UPDATE_DATE, ORGANIZATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HR_ORGANIZATION_UNITS_FK1 | Non Unique | FUSION_TS_TX_IDX | BUSINESS_GROUP_ID |
| HR_ORGANIZATION_UNITS_FK3 | Non Unique | FUSION_TS_TX_IDX | LOCATION_ID |
| HR_ORGANIZATION_UNITS_F_N11 | Non Unique | Default | UPPER("ATTRIBUTE1") |
| HR_ORGANIZATION_UNITS_F_N12 | Non Unique | Default | UPPER("ATTRIBUTE2") |
| HR_ORGANIZATION_UNITS_F_N13 | Non Unique | Default | UPPER("ATTRIBUTE3") |
| HR_ORGANIZATION_UNITS_F_N14 | Non Unique | Default | UPPER("ATTRIBUTE4") |
| HR_ORGANIZATION_UNITS_F_N15 | Non Unique | Default | UPPER("ATTRIBUTE5") |
| HR_ORGANIZATION_UNITS_F_N16 | Non Unique | Default | ATTRIBUTE6 |
| HR_ORGANIZATION_UNITS_F_N17 | Non Unique | Default | ATTRIBUTE7 |
| HR_ORGANIZATION_UNITS_F_N18 | Non Unique | Default | ATTRIBUTE8 |
| HR_ORGANIZATION_UNITS_F_N19 | Non Unique | Default | ATTRIBUTE9 |
| HR_ORGANIZATION_UNITS_F_N20 | Non Unique | Default | ATTRIBUTE10 |
| HR_ORGANIZATION_UNITS_F_N31 | Non Unique | Default | ATTRIBUTE_NUMBER1 |
| HR_ORGANIZATION_UNITS_F_N32 | Non Unique | Default | ATTRIBUTE_NUMBER2 |
| HR_ORGANIZATION_UNITS_F_N33 | Non Unique | Default | ATTRIBUTE_NUMBER3 |
| HR_ORGANIZATION_UNITS_F_N34 | Non Unique | Default | ATTRIBUTE_NUMBER4 |
| HR_ORGANIZATION_UNITS_F_N35 | Non Unique | Default | ATTRIBUTE_NUMBER5 |
| HR_ORGANIZATION_UNITS_F_N41 | Non Unique | Default | ATTRIBUTE_DATE1 |
| HR_ORGANIZATION_UNITS_F_N42 | Non Unique | Default | ATTRIBUTE_DATE2 |
| HR_ORGANIZATION_UNITS_F_N43 | Non Unique | Default | ATTRIBUTE_DATE3 |
| HR_ORGANIZATION_UNITS_F_N44 | Non Unique | Default | ATTRIBUTE_DATE4 |
| HR_ORGANIZATION_UNITS_F_N45 | Non Unique | Default | ATTRIBUTE_DATE5 |
| HR_ORGANIZATION_UNITS_N1 | Non Unique | Default | ESTABLISHMENT_ID |
| HR_ORGANIZATION_UNITS_N2 | Non Unique | Default | LEGAL_ENTITY_ID |
| HR_ORGANIZATION_UNITS_N3 | Non Unique | Default | ORGANIZATION_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
