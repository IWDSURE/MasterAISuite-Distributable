# HWR_RECMND_CHECKLIST_B

This table stores recommended checklist.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecmndchecklistb-3943.html#hwrrecmndchecklistb-3943](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecmndchecklistb-3943.html#hwrrecmndchecklistb-3943)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RECMND_CHECKLIST_B_PK | CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| IS_SEEDED | VARCHAR2 | 5 |  | Yes | Whether the checklist is seeded or not. |
| IS_ACTIVE | VARCHAR2 | 5 |  | Yes | Whether the checklist is active. |
| ORDER_RANK | NUMBER |  | 3 |  | This is the rank order of recommended checklist. |
| CHECKLST_ATTR_1 | VARCHAR2 | 400 |  |  | This is the checklist attribute 1. |
| CHECKLST_ATTR_2 | VARCHAR2 | 400 |  |  | This is the checklist attribute 2. |
| CHECKLST_ATTR_3 | VARCHAR2 | 400 |  |  | This is the checklist attribute 3. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
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
| HWR_RECMND_CHECKLIST_B_U1 | Unique | Default | CHECKLIST_ID, ORA_SEED_SET1 |
| HWR_RECMND_CHECKLIST_B_U11 | Unique | Default | CHECKLIST_ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
