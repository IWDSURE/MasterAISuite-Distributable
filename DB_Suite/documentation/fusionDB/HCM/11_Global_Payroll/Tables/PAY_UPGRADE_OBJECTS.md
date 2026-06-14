# PAY_UPGRADE_OBJECTS

This Table is used to capture the Object change which will be used for the upgrade process.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payupgradeobjects-20464.html#payupgradeobjects-20464](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payupgradeobjects-20464.html#payupgradeobjects-20464)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_UPGRADE_OBJECTS_PK | UPGRADE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| UPGRADE_OBJECT_ID | NUMBER |  | 18 | Yes | UPGRADE_OBJECT_ID |
| IS_LDG_REQUIRED | VARCHAR2 | 2 |  |  | IS_LDG_REQUIRED |
| IS_DISABLED_IN_PRODUCTION | VARCHAR2 | 2 |  |  | Is disabled in production |
| IS_RERUNNABLE | VARCHAR2 | 2 |  |  | IS_RERUNNABLE |
| UPGRADE_OBJECT_BASE_NAME | VARCHAR2 | 120 |  | Yes | Example - EARNINGS_REP_UNIT |
| UPGRADE_MODE | VARCHAR2 | 50 |  | Yes | Type of upgrade Mandatory, Recommended, Optional |
| INCOMPATIBILITY_LEVEL | VARCHAR2 | 30 |  |  | INCOMPATIBILITY_LEVEL |
| UPGRADE_OBJECT_DATE | TIMESTAMP |  |  |  | Date when last upgrade is defined |
| OBJECT_ID | VARCHAR2 | 50 |  |  | If OBJECT_TYPE is TEMPLATE then, it will be Foreign Key to PAY_TMPLT_VERSION_F or it will be Primary Key of the object which got changed. |
| OBJECT_TYPE | VARCHAR2 | 50 |  | Yes | Object Type that we are going to Upgrade E.g : TEMPLATE |
| OBJECT_NAME | VARCHAR2 | 3000 |  |  | Store the alternative keys of "Object Types" |
| UPGRADE_STYLE | VARCHAR2 | 2 |  |  | The process in which the feature can be upgraded. Automatic, Manual or Both |
| RELEASE_LEVEL | VARCHAR2 | 20 |  |  | Release and Patch Bundle info of when the template is updated |
| FINAL_RELEASE_LEVEL | VARCHAR2 | 20 |  |  | Final release and Patch Bundle info of when the template is updated |
| QUALIFYING_METHOD | VARCHAR2 | 50 |  |  | Similar terms to threading level in EBS |
| QUALIFYING_PROCEDURE | VARCHAR2 | 150 |  |  | This is the name of a PL/SQL package procedure that will identify the eligible objects for upgrade. |
| UPGRADE_METHOD | VARCHAR2 | 50 |  |  | This is type of the Upgrade method like java or SQL. |
| UPGRADE_PROCEDURE | VARCHAR2 | 150 |  |  | This is the name of a PL/SQL package procedure that will perform the upgrade. The procedure will take as input the object id that it is processing for. |
| PRE_PROCESS_METHOD | VARCHAR2 | 50 |  |  | This is type of the Pre Process method like java or SQL. |
| PRE_PROCESS_PROCEDURE | VARCHAR2 | 150 |  |  | This is the name of a PL/SQL package procedure that will be performed before the upgrade. |
| LEGISLATIVELY_ENABLED | VARCHAR2 | 1 |  |  | This can be set to Y or N, it can only be set to Y for patch definitions that are Global. This indicates that the localizations teams need to enable a upgrade that has been defined by the Core team. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
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
| PRE_HOOK_CLASS | VARCHAR2 | 150 |  |  | PRE_HOOK_CLASS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_UPGRADE_OBJECTS_FK1 | Non Unique | Default | OBJECT_ID |
| PAY_UPGRADE_OBJECTS_N20 | Non Unique | Default | SGUID |
| PAY_UPGRADE_OBJECTS_PK | Unique | Default | UPGRADE_OBJECT_ID, ORA_SEED_SET1 |
| PAY_UPGRADE_OBJECTS_PK1 | Unique | Default | UPGRADE_OBJECT_ID, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
