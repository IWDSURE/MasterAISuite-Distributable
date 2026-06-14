# HR_DOCUMENT_DELIVERY_PREFS

HCM Reporting document delivery preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentdeliveryprefs-11290.html#hrdocumentdeliveryprefs-11290](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentdeliveryprefs-11290.html#hrdocumentdeliveryprefs-11290)

## Primary Key

| Name | Columns |
|------|----------|
| HR_DOCUMENT_DELIVERY_PREFS_PK | DOC_DELIVERY_PREF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOC_DELIVERY_PREF_ID | NUMBER |  | 18 | Yes | Preference Id |
| PERSON_ID | NUMBER |  | 18 |  | Person Indentifier |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 | Yes | Document ID |
| PSU_ID | NUMBER |  | 18 |  | PSU ID |
| LEMP_ID | NUMBER |  | 18 |  | Legal Employer ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation Code |
| LEVEL_CODE | VARCHAR2 | 40 |  |  | Level Code. |
| LEVEL_ID | NUMBER |  | 18 |  | Level ID. |
| ONLINE_ENABLED | VARCHAR2 | 30 |  |  | Online Enabled or not |
| PAPER_ENABLED | VARCHAR2 | 30 |  |  | Paper Enabled or not |
| EMAIL_ENABLED | VARCHAR2 | 30 |  |  | Email Enabled or not |
| OPTION1_ENABLED | VARCHAR2 | 30 |  |  | OPTION1_ENABLED |
| OPTION2_ENABLED | VARCHAR2 | 30 |  |  | OPTION2_ENABLED |
| OPTION3_ENABLED | VARCHAR2 | 30 |  |  | OPTION3_ENABLED |
| OPTION4_ENABLED | VARCHAR2 | 30 |  |  | OPTION4_ENABLED |
| OPTION5_ENABLED | VARCHAR2 | 30 |  |  | OPTION5_ENABLED |
| ALLOW_WORKER_OVERRIDE | VARCHAR2 | 30 |  |  | Allow Worker Override |
| ONLINE_CONSENT_REQ | VARCHAR2 | 30 |  |  | ONLINE_CONSENT_REQ |
| INITIAL_CONSENT_VALUE | VARCHAR2 | 30 |  |  | Initial value of the consent |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_DOCUMENT_DELIVERY_PREFS_FK1 | Non Unique | FUSION_TS_TX_IDX | DOCUMENT_TYPE_ID, LEVEL_CODE, LEVEL_ID |
| HR_DOCUMENT_DELIVERY_PREFS_FK2 | Non Unique | FUSION_TS_TX_IDX | LEVEL_CODE |
| HR_DOCUMENT_DELIVERY_PREFS_PK | Unique | FUSION_TS_TX_IDX | DOC_DELIVERY_PREF_ID, ORA_SEED_SET1 |
| HR_DOCUMENT_DELIVERY_PREFS_PK1 | Unique | FUSION_TS_TX_IDX | DOC_DELIVERY_PREF_ID, ORA_SEED_SET2 |
| HR_DOCUMENT_DELIVERY_PREF_N20 | Non Unique | Default | SGUID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
