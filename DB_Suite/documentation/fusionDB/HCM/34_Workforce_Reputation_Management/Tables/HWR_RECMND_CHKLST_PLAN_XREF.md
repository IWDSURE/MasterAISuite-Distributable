# HWR_RECMND_CHKLST_PLAN_XREF

This table stores recommended checklist.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecmndchklstplanxref-3115.html#hwrrecmndchklstplanxref-3115](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrecmndchklstplanxref-3115.html#hwrrecmndchklstplanxref-3115)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RECMND_CHKLST_PLAN_XREF_PK | PLAN_ID, CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PLAN_ID | NUMBER |  | 18 | Yes | This is the composite key for this table. |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | This is the composite key for this table. |
| IS_COMPLETED | VARCHAR2 | 5 |  | Yes | Whether the checklist is complete or not. |
| PERSON_ID | NUMBER |  | 18 |  | This is the person id. |
| COMPLETED_DATE | TIMESTAMP |  |  |  | Checklist plan completion date. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RECMND_CHKLST_PLAN_XREF_U1 | Unique | Default | PLAN_ID, CHECKLIST_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
