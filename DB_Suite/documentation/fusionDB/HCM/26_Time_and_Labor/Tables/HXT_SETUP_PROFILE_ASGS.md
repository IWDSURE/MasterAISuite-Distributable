# HXT_SETUP_PROFILE_ASGS

Table that holds profile assignments

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupprofileasgs-3112.html#hxtsetupprofileasgs-3112](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupprofileasgs-3112.html#hxtsetupprofileasgs-3112)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_SETUP_PROFILE_ASGS_PK | SETUP_PROFILE_ASG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PROFILE_ASG_ID | NUMBER |  | 18 | Yes | SETUP_PROFILE_ASG_ID |
| SETUP_PROFILE_ASG_CD | VARCHAR2 | 80 |  |  | Alternate Key |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| SETUP_PROFILE_ID | NUMBER |  | 18 | Yes | SETUP_PROFILE_ID |
| ASSIGN_TO | VARCHAR2 | 80 |  | Yes | ASSIGN_TO |
| OBJECT_ID | NUMBER |  | 18 | Yes | OBJECT_ID |
| DATE_FROM | DATE |  |  | Yes | DATE_FROM |
| DATE_TO | DATE |  |  |  | DATE_TO |
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
| HXT_SETUP_PROFILE_ASGS_FK1 | Non Unique | Default | SETUP_PROFILE_ID |
| HXT_SETUP_PROFILE_ASGS_N20 | Non Unique | Default | SGUID |
| HXT_SETUP_PROFILE_ASGS_PK | Unique | Default | SETUP_PROFILE_ASG_ID, ORA_SEED_SET1 |
| HXT_SETUP_PROFILE_ASGS_PK1 | Unique | Default | SETUP_PROFILE_ASG_ID, ORA_SEED_SET2 |
| HXT_SETUP_PROFILE_ASGS_U1 | Unique | Default | ASSIGN_TO, OBJECT_ID, DATE_FROM, DATE_TO, SETUP_PROFILE_ID, ORA_SEED_SET1 |
| HXT_SETUP_PROFILE_ASGS_U11 | Unique | Default | ASSIGN_TO, OBJECT_ID, DATE_FROM, DATE_TO, SETUP_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
