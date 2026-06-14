# PER_PAY_SCALE_POINTS_TL

Contains translated attributes of PER_PAY_SCALE_POINTS base table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpayscalepointstl-9878.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpayscalepointstl-9878.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PAY_SCALE_POINTS_TL_PK | PAY_SCALE_POINT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAY_SCALE_POINT_ID | NUMBER |  | 18 | Yes | This column holds the system generated identifier which is part of the primary key of this table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  | Yes | This column holds the Name of the Pay Scale Point. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PAY_SCALE_POINTS_TL_N1 | Non Unique | APPS_TS_TX_DATA | NAME, LANGUAGE |
| PER_PAY_SCALE_POINTS_TL_PK | Unique | Default | PAY_SCALE_POINT_ID, LANGUAGE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
