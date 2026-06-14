# WLF_LMC_OBJECTIVE_MAPS

Maps local objectives to global objectives

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcobjectivemaps-12612.html#wlflmcobjectivemaps-12612](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcobjectivemaps-12612.html#wlflmcobjectivemaps-12612)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_OBJECTIVE_MAPS_PK | OBJECTIVE_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECTIVE_MAP_ID | NUMBER |  | 18 | Yes | OBJECTIVE_MAP_ID |
| SEQUENCING_INFO_ID | NUMBER |  | 18 | Yes | SEQUENCING_INFO_ID |
| OBJECTIVE_ID | NUMBER |  | 18 |  | OBJECTIVE_ID |
| OBJECTIVE_MAP_SEQUENCE | NUMBER |  |  | Yes | OBJECTIVE_MAP_SEQUENCE |
| TARGET_OBJECTIVE_IDENTIFIER | VARCHAR2 | 4000 |  | Yes | TARGET_OBJECTIVE_IDENTIFIER |
| TARGET_OBJECTIVE_ID | NUMBER |  | 18 |  | TARGET_OBJECTIVE_ID |
| READ_SATISFIED_STATUS | VARCHAR2 | 1 |  |  | READ_SATISFIED_STATUS |
| READ_NORMALIZED_MEASURE | VARCHAR2 | 1 |  |  | READ_NORMALIZED_MEASURE |
| WRITE_SATISFIED_STATUS | VARCHAR2 | 1 |  |  | WRITE_SATISFIED_STATUS |
| WRITE_NORMALIZED_MEASURE | VARCHAR2 | 1 |  |  | WRITE_NORMALIZED_MEASURE |
| READ_RAW_SCORE | VARCHAR2 | 1 |  |  | READ_RAW_SCORE |
| WRITE_RAW_SCORE | VARCHAR2 | 1 |  |  | WRITE_RAW_SCORE |
| READ_MIN_SCORE | VARCHAR2 | 1 |  |  | READ_MIN_SCORE |
| WRITE_MIN_SCORE | VARCHAR2 | 1 |  |  | WRITE_MIN_SCORE |
| READ_MAX_SCORE | VARCHAR2 | 1 |  |  | READ_MAX_SCORE |
| WRITE_MAX_SCORE | VARCHAR2 | 1 |  |  | WRITE_MAX_SCORE |
| READ_COMPLETION_STATUS | VARCHAR2 | 1 |  |  | READ_COMPLETION_STATUS |
| WRITE_COMPLETION_STATUS | VARCHAR2 | 1 |  |  | WRITE_COMPLETION_STATUS |
| READ_PROGRESS_MEASURE | VARCHAR2 | 1 |  |  | READ_PROGRESS_MEASURE |
| WRITE_PROGRESS_MEASURE | VARCHAR2 | 1 |  |  | WRITE_PROGRESS_MEASURE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LMC_OBJECTIVE_MAPS_N1 | Non Unique | Default | SEQUENCING_INFO_ID, OBJECTIVE_ID |
| WLF_LMC_OBJECTIVE_MAPS_PK | Unique | FUSION_TS_TX_DATA | OBJECTIVE_MAP_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
