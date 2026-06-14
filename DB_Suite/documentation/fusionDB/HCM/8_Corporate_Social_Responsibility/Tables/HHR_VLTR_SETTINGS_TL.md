# HHR_VLTR_SETTINGS_TL

THIS TABLE STORES THE DATA FOR VOLUNTEER SETTINGS

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrsettingstl-26983.html#hhrvltrsettingstl-26983](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrsettingstl-26983.html#hhrvltrsettingstl-26983)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_SETTINGS_TL_PK | ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| USER_AGREEMENT | CLOB |  |  |  | USER_AGREEMENT |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| WELCOME_MESSAGE | VARCHAR2 | 100 |  |  | WELCOME_MESSAGE |
| WAIVER_AGREEMENT | VARCHAR2 | 100 |  |  | WAIVER_AGREEMENT |
| WAIVER_TITLE | VARCHAR2 | 100 |  |  | WAIVER_TITLE |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
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
| HHR_VLTR_SETTINGS_TL_U1 | Unique | FUSION_TS_TX_DATA | ID, LANGUAGE, ORA_SEED_SET1 |
| HHR_VLTR_SETTINGS_TL_U11 | Unique | FUSION_TS_TX_DATA | ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
