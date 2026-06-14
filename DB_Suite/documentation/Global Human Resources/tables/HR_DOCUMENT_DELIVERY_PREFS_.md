# HR_DOCUMENT_DELIVERY_PREFS_

HCM Reporting document delivery preferences

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentdeliveryprefs-3266.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdocumentdeliveryprefs-3266.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_DOCUMENT_DELIVERY_PREFS_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_DELIVERY_PREF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOC_DELIVERY_PREF_ID | NUMBER |  | 18 | Yes | Preference Id |
| PERSON_ID | NUMBER |  | 18 |  | Person Indentifier |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Document ID |
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
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise ID |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_DOCUMENT_DELIVERY_PREFS_PK_ | Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_DELIVERY_PREF_ID |
| HR_DOCUMENT_DEL_PREFSN1_ | Non Unique | Default | DOC_DELIVERY_PREF_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
