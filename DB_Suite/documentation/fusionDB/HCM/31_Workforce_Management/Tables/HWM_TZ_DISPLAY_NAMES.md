# HWM_TZ_DISPLAY_NAMES

This table contains the Long and Short display names for Time zone for different languages.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtzdisplaynames-10763.html#hwmtzdisplaynames-10763](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtzdisplaynames-10763.html#hwmtzdisplaynames-10763)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TZ_DISPLAY_NAMES_PK | TZ_DISPLAY_NAMES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TZ_DISPLAY_NAMES_ID | NUMBER |  | 19 | Yes | Primary Key column containing a random
generated number.  This column is not updateable. |
| TIME_ZONE_CODE | VARCHAR2 | 50 |  | Yes | IANA based time zone identifier (e.g. Europe/Paris, America/Los_Angeles). |
| LANGUAGE_CODE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| LANGUAGE_TAG | VARCHAR2 | 30 |  |  | The language tag (e.g. fr-CA for French Canadian). This can be used to get the associated Locale Java object. |
| LONG_NAME | VARCHAR2 | 150 |  | Yes | The generic long display name of the timezone in the specified language, e.g. (UTC-08:00) Tijuana - Pacifique (HNP). |
| SHORT_NAME | VARCHAR2 | 50 |  | Yes | The generic short display name of the timezone in the specified language. For instance, HNP is the short generic display name corresponding to the long name "(UTC-08:00) Tijuana - Pacifique (HNP)". |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TZ_DISPLAY_NAMES_N20 | Non Unique | Default | SGUID |
| HWM_TZ_DISPLAY_NAMES_U1 | Unique | Default | TZ_DISPLAY_NAMES_ID, ORA_SEED_SET1 |
| HWM_TZ_DISPLAY_NAMES_U11 | Unique | Default | TZ_DISPLAY_NAMES_ID, ORA_SEED_SET2 |
| HWM_TZ_DISPLAY_NAMES_U2 | Unique | Default | TIME_ZONE_CODE, LANGUAGE_CODE, ORA_SEED_SET1 |
| HWM_TZ_DISPLAY_NAMES_U21 | Unique | Default | TIME_ZONE_CODE, LANGUAGE_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
