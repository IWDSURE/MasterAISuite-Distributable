# IRC_SEARCH_INDEX_UPGRADES

Table contains release-to-release index upgrade information.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchindexupgrades-8660.html#ircsearchindexupgrades-8660](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircsearchindexupgrades-8660.html#ircsearchindexupgrades-8660)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_SEARCH_INDEX_UPGRADES_PK | UPGRADE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UPGRADE_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| RELEASE | VARCHAR2 | 32 |  | Yes | Release (ex: 20A) in which the index is upgraded. |
| VERSION | VARCHAR2 | 32 |  | Yes | Version (ex: 1) in a particular release in which an index is upgraded. |
| ENTITY_TYPE | VARCHAR2 | 32 |  | Yes | The entity (ex: REQUISITION) for which the index must be upgraded. |
| UPGRADE_STATUS | VARCHAR2 | 32 |  | Yes | Status of the index upgrade. |
| NEW_INDEX_SCHEMA | CLOB |  |  |  | The new index structure as a json. |
| UPGRADE_START_DATE | TIMESTAMP |  |  |  | Timestamp for when the upgrade has started (when the status moves to ORA_INPROGRESS). |
| UPGRADE_END_DATE | TIMESTAMP |  |  |  | Timestamp for when the upgrade has started (when the status moves to ORA_ACTIVE or ORA_FAILED). |
| UPGRADE_DEPRECATION_DATE | TIMESTAMP |  |  |  | Timestamp for when the upgrade has started (when the status moves to ORA_DEPRECATED). |
| UPGRADE_FAILURE_REASON | CLOB |  |  |  | The upgrade failure reason. |
| UPGRADE_SOURCE_VERSIONS | VARCHAR2 | 32 |  |  | Comma separated value of OSCS Index versions to be upgraded |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_SEARCH_INDEX_UPGRADES_PK | Unique | FUSION_TS_SEED | UPGRADE_ID, ORA_SEED_SET1 |
| IRC_SEARCH_INDEX_UPGRADES_PK1 | Unique | FUSION_TS_SEED | UPGRADE_ID, ORA_SEED_SET2 |
| IRC_SEARCH_INDEX_UPGRADES_UK1 | Unique | FUSION_TS_SEED | RELEASE, VERSION, ENTITY_TYPE, ORA_SEED_SET1 |
| IRC_SEARCH_INDEX_UPGRADES_UK11 | Unique | FUSION_TS_SEED | RELEASE, VERSION, ENTITY_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
