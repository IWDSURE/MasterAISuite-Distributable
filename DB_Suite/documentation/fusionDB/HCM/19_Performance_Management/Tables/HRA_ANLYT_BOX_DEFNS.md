# HRA_ANLYT_BOX_DEFNS

This table is used to store the set id, performance rating model and potential rating model for which 9-box labels can be defined.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraanlytboxdefns-18488.html#hraanlytboxdefns-18488](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraanlytboxdefns-18488.html#hraanlytboxdefns-18488)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_ANLYT_BOX_DEFNS_PK | ANALYTIC_BOX_DEFN_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ANALYTIC_BOX_DEFN_ID | NUMBER |  | 18 | Yes | Unique Id for the Box definition set by the system |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| SET_ID | NUMBER |  | 18 | Yes | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |  |
| PERFORMANCE_RATING_MODEL_ID | NUMBER |  | 18 | Yes | Performance Rating Model |  |
| POTENTIAL_RATING_MODEL_ID | NUMBER |  | 18 | Yes | Potential Rating Model |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_ANLYT_BOX_DEFNS_PK | Unique | Default | ANALYTIC_BOX_DEFN_ID, BUSINESS_GROUP_ID |
| HRA_ANLYT_BOX_DEFNS_UK1 | Unique | Default | SET_ID, PERFORMANCE_RATING_MODEL_ID, POTENTIAL_RATING_MODEL_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
