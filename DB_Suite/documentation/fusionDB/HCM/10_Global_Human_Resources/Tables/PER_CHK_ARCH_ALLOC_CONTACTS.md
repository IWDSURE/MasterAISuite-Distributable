# PER_CHK_ARCH_ALLOC_CONTACTS

PER_CHK_ARCH_ALLOC_CONTACTS : This table has contacts for allocated checklist.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloccontacts-13536.html#perchkarchalloccontacts-13536](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkarchalloccontacts-13536.html#perchkarchalloccontacts-13536)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_ARCH_ALLOC_CONTACTS_PK | ALLOC_CHKLST_CONTACT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_CHKLST_CONTACT_ID | NUMBER |  | 18 | Yes | ALLOC_CHKLST_CONTACT_ID |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 | Yes | ALLOCATED_CHECKLIST_ID |
| CHECKLIST_CONTACT_ID | NUMBER |  | 18 |  | CHECKLIST_CONTACT_ID |
| CONTACT_TITLE_CODE | VARCHAR2 | 30 |  | Yes | CONTACT_TITLE_CODE |
| CONTACT_TYPE | VARCHAR2 | 30 |  | Yes | CONTACT_TYPE |
| CUSTOM_CONTACT | VARCHAR2 | 400 |  |  | CUSTOM_CONTACT |
| ADHOC_USER_GUID | VARCHAR2 | 64 |  |  | ADHOC_USER_GUID |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | RESPONSIBILITY_TYPE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SYNCH_HISTORY | VARCHAR2 | 4000 |  |  | SYNCH_HISTORY |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_ARCH_ALLOC_CONTACTS_PK | Unique | FUSION_TS_TX_DATA | ALLOC_CHKLST_CONTACT_ID |
| PER_CHK_ARCH_ALLOC_CONTACTS_N1 | Non Unique | Default | ALLOCATED_CHECKLIST_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
