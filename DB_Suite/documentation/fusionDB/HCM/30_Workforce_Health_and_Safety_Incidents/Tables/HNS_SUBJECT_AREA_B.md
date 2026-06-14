# HNS_SUBJECT_AREA_B

HNS SUBJECT AREA. This table is the base for Analysis Subject area.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjectareab-25465.html#hnssubjectareab-25465](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnssubjectareab-25465.html#hnssubjectareab-25465)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_SUBJECT_AREA_B_PK | SUBJECT_AREA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBJECT_AREA_ID | NUMBER |  | 18 | Yes | Primary key for HNS_SUBJECT_AREA_B table. |
| SUBJECT_AREA_CODE | VARCHAR2 | 18 |  | Yes | Code defined for each analysis subject area. |
| DISPLAY_SEQUENCE | NUMBER |  | 18 | Yes | Display order sequence.This field is editable from UI. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Enabled flag. This column signifies whether the subject area is enabled. |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag. This column signifies whether the subject area is deleted |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HNS_SUBJECT_AREA_B_UK1 | Unique | Default | SUBJECT_AREA_ID |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
