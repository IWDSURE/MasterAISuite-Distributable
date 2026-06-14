# PER_AOR_TEMPLATE

This table holds the basic information of a responsibility template

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplate-9388.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraortemplate-9388.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_AOR_TEMPLATE_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| USAGE | VARCHAR2 | 4000 |  |  | Indicates the purpose for which the responsibility is used |
| BYPASS_PREVIEW | VARCHAR2 | 30 |  |  | Indicates whether to bypass the preview while autoprovisioning. |
| TEMPLATE_NAME | VARCHAR2 | 240 |  | Yes | A name which describes this template |
| TEMPLATE_CODE | VARCHAR2 | 30 |  | Yes | A code which uniquely identifies this template |
| START_DATE | DATE |  |  | Yes | The effective start date of the template |
| END_DATE | DATE |  |  |  | The effective end date of the template |
| REPSONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | The responsibility type which would be used for creating areas of responsibility data |
| SYNC_ENABLED | VARCHAR2 | 30 |  |  | Indicates whether to allow synchronization for this template |
| WORK_CONTACTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether to include this row in work contacts evaluation |
| STATUS | VARCHAR2 | 30 |  |  | Indicates whether this template is active or not. |
| TEMPLATE_DESCRIPTION | VARCHAR2 | 1000 |  |  | Detailed description for this template |
| STATUS_INDICATOR | VARCHAR2 | 30 |  |  | This flag indicates template's current status with respect to auto provision. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_AOR_TEMPLATE_N1 | Non Unique | Default | TEMPLATE_NAME |
| PER_AOR_TEMPLATE_PK | Unique | Default | TEMPLATE_ID |
| PER_AOR_TEMPLATE_U1 | Unique | Default | TEMPLATE_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
