# HRC_SEM_INT_JOB_WORK_LOCS

This table is to store the internal job locations.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemintjobworklocs-23099.html#hrcsemintjobworklocs-23099](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemintjobworklocs-23099.html#hrcsemintjobworklocs-23099)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_INT_JOB_WORK_LOCS_PK | INT_JOB_WORK_LOC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INT_JOB_WORK_LOC_ID | NUMBER |  | 18 | Yes | This is the primary key of the internal job location table. |
| INTERNAL_JOB_ID | NUMBER |  | 18 | Yes | This column contains the Internal Job ID referenced to the Internal Job table. |
| WORKLOCATION_ID | VARCHAR2 | 128 |  | Yes | This is the worklocation id of the address. |
| LATITUDE | NUMBER |  |  |  | This is the lattitude of the location. |
| LONGITUDE | NUMBER |  |  |  | This is the longitude of the location. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_INT_JOB_WORK_LOCS_N1 | Non Unique | FUSION_TS_TX_DATA | WORKLOCATION_ID |
| HRC_SEM_INT_JOB_WORK_LOCS_N2 | Non Unique | FUSION_TS_TX_DATA | INTERNAL_JOB_ID |
| HRC_SEM_INT_JOB_WORK_LOCS_U1 | Unique | FUSION_TS_TX_DATA | INT_JOB_WORK_LOC_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
