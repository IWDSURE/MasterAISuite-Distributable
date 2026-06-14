# IRC_TP_CATEGORY_PHASES

Stores the phases in which partner is involved in a third party integration category.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpcategoryphases-26239.html#irctpcategoryphases-26239](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctpcategoryphases-26239.html#irctpcategoryphases-26239)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TP_CATEGORY_PHASES_PK | CATEGORY_PHASE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_PHASE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CATEGORY_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_CATEGORIES_B |
| PHASE_CODE | VARCHAR2 | 30 |  | Yes | Stores the code identifying the category phase to which the partner service belongs. The corresponding lookup type is ORA_IRC_TP_CATEGORY_PHASE |
| PHASE_SEQUENCE | NUMBER |  | 18 |  | Stores the phase sequence for this category |
| CATEGORY_PHASE_LABEL | VARCHAR2 | 500 |  |  | Stores the resource bundle key for label to be displayed against partner service for this category phase |
| INTERACTION_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the code identifying the type of interaction with partner service. The corresponding lookup type is ORA_IRC_TP_INTEGRATION_TYPE |
| DEFAULT_PARAMS | VARCHAR2 | 2000 |  |  | Stores the default params to be appended when invoking partner service. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TP_CATEGORY_PHASES_FK1 | Non Unique | FUSION_TS_SEED | CATEGORY_ID |
| IRC_TP_CATEGORY_PHASES_PK | Unique | FUSION_TS_SEED | CATEGORY_PHASE_ID, ORA_SEED_SET1 |
| IRC_TP_CATEGORY_PHASES_PK1 | Unique | FUSION_TS_SEED | CATEGORY_PHASE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
