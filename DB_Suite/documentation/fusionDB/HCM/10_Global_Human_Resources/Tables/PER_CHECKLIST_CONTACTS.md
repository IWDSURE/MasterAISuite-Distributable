# PER_CHECKLIST_CONTACTS

PER_CHECKLIST_CONTACTS : This table has checklist contacts

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcontacts-9307.html#perchecklistcontacts-9307](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistcontacts-9307.html#perchecklistcontacts-9307)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHECKLIST_CONTACTS_PK | CHECKLIST_CONTACT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_CONTACT_ID | NUMBER |  | 18 | Yes | CHECKLIST_CONTACT_ID |  |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHECKLISTS_B.CHECKLIST_ID |  |
| CONTACT_TITLE_CODE | VARCHAR2 | 30 |  | Yes | Contact Title:
Extensible Lookup: ORA_CHK_CONTACT_TITLES
Values:
ORA_ONBOARDING_SPONSOR - Onboarding Sponsor |  |
| CONTACT_TYPE | VARCHAR2 | 30 |  | Yes | Contact Type:
System Lookup: ORA_CHK_CONTACT_TYPES
Values:
ORA_LN_MGR - Line Manager
ORA_ADHOC_USER - Specific User
ORA_RESP_TYPE - Responsibility Type
ORA_CUSTOM - Custom |  |
| CUSTOM_CONTACT | VARCHAR2 | 400 |  |  | Custom Contact Details |  |
| ADHOC_USER_GUID | VARCHAR2 | 64 |  |  | Specific User Details |  |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | Responsibility Type |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_CONTACTS_N1 | Non Unique | FUSION_TS_TX_DATA | CHECKLIST_ID |
| PER_CHECKLIST_CONTACTS_PK | Unique | FUSION_TS_TX_DATA | CHECKLIST_CONTACT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
