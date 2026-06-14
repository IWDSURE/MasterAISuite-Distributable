# HWM_TM_TEMPLATES

table to store timecard template data

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmtemplates-25051.html#hwmtmtemplates-25051](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmtemplates-25051.html#hwmtmtemplates-25051)

## Primary Key

| Name | Columns |
|------|----------|
| hwm_tm_templates_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Template Identifier |
| NAME | VARCHAR2 | 256 |  | Yes | Name of template |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description of template |
| LAYOUT_ID | NUMBER |  | 18 | Yes | Timecard Layout Id |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Assignment Id |
| TEMPLATE | CLOB |  |  | Yes | Snapshot of Timecard |
| TEMPLATE_TYPE | VARCHAR2 | 15 |  | Yes | To distinguish between private and public Template |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hwm_tm_templates_PK | Unique | Default | TEMPLATE_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
