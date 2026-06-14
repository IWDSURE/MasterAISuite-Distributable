# HXT_SETUP_OPTION_VALS

This table holds the setup option values

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupoptionvals-22924.html#hxtsetupoptionvals-22924](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtsetupoptionvals-22924.html#hxtsetupoptionvals-22924)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_SETUP_OPTION_VALS_PK | SETUP_OPTION_VAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_OPTION_VAL_ID | NUMBER |  | 18 | Yes | SETUP_OPTION_VAL_ID |
| SETUP_OPTION_VAL_CD | VARCHAR2 | 80 |  |  | Alternate Key |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| TYPE | VARCHAR2 | 20 |  | Yes | Can contain WORKER or MANAGER |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SETUP_PROFILE_ID | NUMBER |  | 18 | Yes | SETUP_PROFILE_ID |
| VALUE1 | VARCHAR2 | 80 |  |  | VALUE1 |
| VALUE2 | VARCHAR2 | 80 |  |  | VALUE2 |
| VALUE3 | VARCHAR2 | 80 |  |  | VALUE3 |
| VALUE4 | VARCHAR2 | 80 |  |  | VALUE4 |
| VALUE5 | VARCHAR2 | 80 |  |  | VALUE5 |
| VALUE6 | VARCHAR2 | 80 |  |  | VALUE6 |
| VALUE7 | VARCHAR2 | 80 |  |  | VALUE7 |
| VALUE8 | VARCHAR2 | 80 |  |  | VALUE8 |
| VALUE9 | VARCHAR2 | 80 |  |  | VALUE9 |
| VALUE10 | VARCHAR2 | 80 |  |  | VALUE10 |
| VALUE11 | VARCHAR2 | 80 |  |  | VALUE11 |
| VALUE12 | VARCHAR2 | 80 |  |  | VALUE12 |
| VALUE13 | VARCHAR2 | 80 |  |  | VALUE13 |
| VALUE14 | VARCHAR2 | 80 |  |  | VALUE14 |
| VALUE15 | VARCHAR2 | 80 |  |  | VALUE15 |
| VALUE16 | VARCHAR2 | 80 |  |  | VALUE16 |
| VALUE17 | VARCHAR2 | 80 |  |  | VALUE17 |
| VALUE18 | VARCHAR2 | 80 |  |  | VALUE18 |
| VALUE19 | VARCHAR2 | 80 |  |  | VALUE19 |
| VALUE20 | VARCHAR2 | 80 |  |  | VALUE20 |
| VALUE21 | VARCHAR2 | 80 |  |  | VALUE21 |
| VALUE22 | VARCHAR2 | 80 |  |  | VALUE22 |
| VALUE23 | VARCHAR2 | 80 |  |  | VALUE23 |
| VALUE24 | VARCHAR2 | 80 |  |  | VALUE24 |
| VALUE25 | VARCHAR2 | 80 |  |  | VALUE25 |
| VALUE26 | VARCHAR2 | 80 |  |  | VALUE26 |
| VALUE27 | VARCHAR2 | 80 |  |  | VALUE27 |
| VALUE28 | VARCHAR2 | 80 |  |  | VALUE28 |
| VALUE29 | VARCHAR2 | 80 |  |  | VALUE29 |
| VALUE30 | NUMBER |  | 18 |  | VALUE30 |
| VALUE31 | NUMBER |  | 18 |  | VALUE31 |
| VALUE32 | NUMBER |  | 18 |  | VALUE32 |
| VALUE33 | NUMBER |  | 18 |  | VALUE33 |
| VALUE34 | NUMBER |  | 18 |  | VALUE34 |
| VALUE35 | NUMBER |  | 18 |  | VALUE35 |
| VALUE36 | NUMBER |  | 18 |  | VALUE36 |
| VALUE37 | NUMBER |  | 18 |  | VALUE37 |
| VALUE38 | NUMBER |  | 18 |  | VALUE38 |
| VALUE39 | NUMBER |  | 18 |  | VALUE39 |
| VALUE40 | NUMBER |  | 18 |  | VALUE40 |
| VALUE41 | NUMBER |  | 18 |  | VALUE41 |
| VALUE42 | NUMBER |  | 18 |  | VALUE42 |
| VALUE43 | NUMBER |  | 18 |  | VALUE43 |
| VALUE44 | NUMBER |  | 18 |  | VALUE44 |
| VALUE45 | NUMBER |  | 18 |  | VALUE45 |
| VALUE46 | NUMBER |  | 18 |  | VALUE46 |
| VALUE47 | NUMBER |  | 18 |  | VALUE47 |
| VALUE48 | NUMBER |  | 18 |  | VALUE48 |
| VALUE49 | NUMBER |  | 18 |  | VALUE49 |
| VALUE50 | NUMBER |  | 18 |  | VALUE50 |
| VALUE51 | NUMBER |  | 18 |  | VALUE51 |
| VALUE52 | NUMBER |  | 18 |  | VALUE52 |
| VALUE53 | NUMBER |  | 18 |  | VALUE53 |
| VALUE54 | NUMBER |  | 18 |  | VALUE54 |
| VALUE55 | NUMBER |  | 18 |  | VALUE55 |
| VALUE56 | NUMBER |  | 18 |  | VALUE56 |
| VALUE57 | NUMBER |  | 18 |  | VALUE57 |
| VALUE58 | NUMBER |  | 18 |  | VALUE58 |
| VALUE59 | NUMBER |  | 18 |  | VALUE59 |
| VALUE60 | NUMBER |  | 18 |  | VALUE60 |
| VALUE61 | NUMBER |  | 18 |  | VALUE61 |
| VALUE62 | NUMBER |  | 18 |  | VALUE62 |
| VALUE63 | NUMBER |  | 18 |  | VALUE63 |
| VALUE64 | NUMBER |  | 18 |  | VALUE64 |
| VALUE65 | NUMBER |  | 18 |  | VALUE65 |
| VALUE66 | NUMBER |  | 18 |  | VALUE66 |
| VALUE67 | NUMBER |  | 18 |  | VALUE67 |
| VALUE68 | NUMBER |  | 18 |  | VALUE68 |
| VALUE69 | NUMBER |  | 18 |  | VALUE69 |
| VALUE70 | NUMBER |  | 18 |  | VALUE70 |
| VALUE71 | NUMBER |  | 18 |  | VALUE71 |
| VALUE72 | NUMBER |  | 18 |  | VALUE72 |
| VALUE73 | NUMBER |  | 18 |  | VALUE73 |
| VALUE74 | NUMBER |  | 18 |  | VALUE74 |
| VALUE75 | NUMBER |  | 18 |  | VALUE75 |
| VALUE76 | NUMBER |  | 18 |  | VALUE76 |
| VALUE77 | NUMBER |  | 18 |  | VALUE77 |
| VALUE78 | NUMBER |  | 18 |  | VALUE78 |
| VALUE79 | NUMBER |  | 18 |  | VALUE79 |
| VALUE80 | VARCHAR2 | 80 |  |  | VALUE80 |
| VALUE81 | VARCHAR2 | 80 |  |  | VALUE81 |
| VALUE82 | VARCHAR2 | 80 |  |  | VALUE82 |
| VALUE83 | VARCHAR2 | 80 |  |  | VALUE83 |
| VALUE84 | VARCHAR2 | 80 |  |  | VALUE84 |
| VALUE85 | VARCHAR2 | 80 |  |  | VALUE85 |
| VALUE86 | VARCHAR2 | 80 |  |  | VALUE86 |
| VALUE87 | VARCHAR2 | 80 |  |  | VALUE87 |
| VALUE88 | VARCHAR2 | 80 |  |  | VALUE88 |
| VALUE89 | VARCHAR2 | 80 |  |  | VALUE89 |
| VALUE90 | VARCHAR2 | 80 |  |  | VALUE90 |
| VALUE91 | VARCHAR2 | 80 |  |  | VALUE91 |
| VALUE92 | VARCHAR2 | 80 |  |  | VALUE92 |
| VALUE93 | VARCHAR2 | 80 |  |  | VALUE93 |
| VALUE94 | VARCHAR2 | 80 |  |  | VALUE94 |
| VALUE95 | VARCHAR2 | 80 |  |  | VALUE95 |
| VALUE96 | VARCHAR2 | 80 |  |  | VALUE96 |
| VALUE97 | VARCHAR2 | 80 |  |  | VALUE97 |
| VALUE98 | VARCHAR2 | 80 |  |  | VALUE98 |
| VALUE99 | VARCHAR2 | 80 |  |  | VALUE99 |
| VALUE100 | VARCHAR2 | 80 |  |  | VALUE100 |
| VALUE101 | VARCHAR2 | 80 |  |  | VALUE101 |
| VALUE102 | VARCHAR2 | 80 |  |  | VALUE102 |
| VALUE103 | VARCHAR2 | 80 |  |  | VALUE103 |
| VALUE104 | VARCHAR2 | 80 |  |  | VALUE104 |
| VALUE105 | VARCHAR2 | 80 |  |  | VALUE105 |
| VALUE106 | VARCHAR2 | 80 |  |  | VALUE106 |
| VALUE107 | VARCHAR2 | 80 |  |  | VALUE107 |
| VALUE108 | VARCHAR2 | 80 |  |  | VALUE108 |
| VALUE109 | VARCHAR2 | 80 |  |  | VALUE109 |
| VALUE110 | VARCHAR2 | 80 |  |  | VALUE110 |
| VALUE111 | VARCHAR2 | 80 |  |  | VALUE111 |
| VALUE112 | VARCHAR2 | 80 |  |  | VALUE112 |
| VALUE113 | VARCHAR2 | 80 |  |  | VALUE113 |
| VALUE114 | VARCHAR2 | 80 |  |  | VALUE114 |
| VALUE115 | VARCHAR2 | 80 |  |  | VALUE115 |
| VALUE116 | VARCHAR2 | 80 |  |  | VALUE116 |
| VALUE117 | VARCHAR2 | 80 |  |  | VALUE117 |
| VALUE118 | VARCHAR2 | 80 |  |  | VALUE118 |
| VALUE119 | VARCHAR2 | 80 |  |  | VALUE119 |
| VALUE120 | VARCHAR2 | 80 |  |  | VALUE120 |
| VALUE121 | VARCHAR2 | 80 |  |  | VALUE121 |
| VALUE122 | VARCHAR2 | 80 |  |  | VALUE122 |
| VALUE123 | VARCHAR2 | 80 |  |  | VALUE123 |
| VALUE124 | VARCHAR2 | 80 |  |  | VALUE124 |
| VALUE125 | VARCHAR2 | 80 |  |  | VALUE125 |
| VALUE126 | VARCHAR2 | 80 |  |  | VALUE126 |
| VALUE127 | VARCHAR2 | 80 |  |  | VALUE127 |
| VALUE128 | VARCHAR2 | 80 |  |  | VALUE128 |
| VALUE129 | VARCHAR2 | 80 |  |  | VALUE129 |
| VALUE130 | VARCHAR2 | 80 |  |  | VALUE130 |
| VALUE131 | VARCHAR2 | 80 |  |  | VALUE131 |
| VALUE132 | VARCHAR2 | 80 |  |  | VALUE132 |
| VALUE133 | VARCHAR2 | 80 |  |  | VALUE133 |
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
| HXT_SETUP_OPTION_VALS_FK2 | Non Unique | Default | SETUP_PROFILE_ID |
| HXT_SETUP_OPTION_VALS_N1 | Non Unique | Default | VALUE30 |
| HXT_SETUP_OPTION_VALS_N2 | Non Unique | Default | TYPE, VALUE55, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HXT_SETUP_OPTION_VALS_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HXT_SETUP_OPTION_VALS_N3 | Non Unique | Default | TYPE, VALUE50, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| HXT_SETUP_OPTION_VALS_PK | Unique | Default | SETUP_OPTION_VAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| HXT_SETUP_OPTION_VALS_PK1 | Unique | Default | SETUP_OPTION_VAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
