# HHR_VLTR_SETTINGS_B

This table will store Volunteer Settings details

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrsettingsb-30250.html#hhrvltrsettingsb-30250](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrsettingsb-30250.html#hhrvltrsettingsb-30250)

## Primary Key

| Name | Columns |
|------|----------|
| HHR_VLTR_SETTINGS_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | ID |
| WELCOME_IMAGE_ID | NUMBER |  | 18 |  | WELCOME_IMAGE_ID |
| EINREF_START_DATE | DATE |  |  |  | EINREF_START_DATE |
| EINREF_START_TIME | TIMESTAMP |  |  |  | EINREF_START_TIME |
| EINREF_FREQUENCY | NUMBER |  | 18 |  | EINREF_FREQUENCY |
| EINREF_NEXT_RUN_DATE | DATE |  |  |  | EINREF_NEXT_RUN_DATE |
| EINREF_NEXT_RUN_TIME | TIMESTAMP |  |  |  | EINREF_NEXT_RUN_TIME |
| EIN_VALIDATION_ON | NUMBER |  | 1 |  | EIN_VALIDATION_ON |
| IRS_URL | VARCHAR2 | 100 |  |  | IRS_URL |
| WELCOME_IMAGE_URL | VARCHAR2 | 100 |  |  | WELCOME_IMAGE_URL |
| ADMIN_ROLE | VARCHAR2 | 100 |  |  | ADMIN_ROLE |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| PHOTO_APPROVAL_SETTING | NUMBER |  | 1 |  | PHOTO_APPROVAL_SETTING |
| PHOTO_AGREEMENT_SETTING | NUMBER |  | 1 |  | PHOTO_AGREEMENT_SETTING |
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
| HHR_VLTR_SETTINGS_B_U1 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET1 |
| HHR_VLTR_SETTINGS_B_U11 | Unique | FUSION_TS_TX_DATA | ID, ORA_SEED_SET2 |

---

[← Back to Index](../8_Corporate_Social_Responsibility_Tables_Index.md)
