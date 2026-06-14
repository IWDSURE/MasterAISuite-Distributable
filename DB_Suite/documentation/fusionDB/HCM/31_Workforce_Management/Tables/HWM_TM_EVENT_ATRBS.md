# HWM_TM_EVENT_ATRBS

Time event attributes table for TCD

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** FUSION_TS_INTERFACE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmeventatrbs-21887.html#hwmtmeventatrbs-21887](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmeventatrbs-21887.html#hwmtmeventatrbs-21887)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_TM_EVENT_ATRBS_PK | TM_EVENT_ATRB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TM_EVENT_ATRB_ID | NUMBER |  | 18 | Yes | TM_EVENT_ATRB_ID |
| NAME | VARCHAR2 | 240 |  | Yes | Attribute name |
| VALUE | VARCHAR2 | 150 |  | Yes | Attribute value |
| TM_EVENT_ID | NUMBER |  | 18 | Yes | TM_EVENT_ID |
| FACET | VARCHAR2 | 150 |  |  | Facet Value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_TM_EVENT_ATRBS_N1 | Non Unique | Default | TM_EVENT_ID |
| HWM_TM_EVENT_ATRBS_UK1 | Unique | Default | TM_EVENT_ATRB_ID |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
