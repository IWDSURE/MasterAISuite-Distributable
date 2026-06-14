# HXT_SETUP_PROFILES_B

A base table that holds Setup Profiles.

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupprofilesb-15423.html#hxtsetupprofilesb-15423](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupprofilesb-15423.html#hxtsetupprofilesb-15423)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_SETUP_PROFILES_B_PK | SETUP_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PROFILE_ID | NUMBER |  | 18 | Yes | SETUP_PROFILE_ID |
| STATUS | VARCHAR2 | 80 |  |  | Draft or submit mode |
| SETUP_PROFILE_CD | VARCHAR2 | 80 |  |  | This column would be used as Alternate Key |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PRECEDENCE | NUMBER |  |  | Yes | PRECEDENCE |
| PRODUCT_AREA | VARCHAR2 | 80 |  | Yes | PRODUCT_AREA |
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
| HXT_SETUP_PROFILES_B_N1 | Non Unique | Default | SETUP_PROFILE_CD, PRODUCT_AREA |
| HXT_SETUP_PROFILES_B_N20 | Non Unique | Default | SGUID |
| HXT_SETUP_PROFILES_B_PK | Unique | Default | SETUP_PROFILE_ID, ORA_SEED_SET1 |
| HXT_SETUP_PROFILES_B_PK1 | Unique | Default | SETUP_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
