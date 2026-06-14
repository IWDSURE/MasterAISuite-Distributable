# WLF_LMC_OBJECTIVES

Objectives which measure granular knowlege

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcobjectives-7386.html#wlflmcobjectives-7386](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmcobjectives-7386.html#wlflmcobjectives-7386)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_OBJECTIVES_PK | OBJECTIVE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECTIVE_ID | NUMBER |  | 18 | Yes | OBJECTIVE_ID |
| OBJECTIVE_NAME | VARCHAR2 | 240 |  | Yes | OBJECTIVE_NAME |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 4000 |  |  | EXTERNAL_IDENTIFIER |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | DESCRIPTION |
| SEQUENCING_INFO_ID | NUMBER |  | 18 |  | SEQUENCING_INFO_ID |
| SCORM_OBJECTIVE_TYPE | VARCHAR2 | 1 |  |  | SCORM_OBJECTIVE_TYPE |
| SATISFIED_BY_MEASURE | VARCHAR2 | 1 |  |  | SATISFIED_BY_MEASURE |
| OBJECTIVE_MAP_OBJ_IDENTIFIER | VARCHAR2 | 4000 |  |  | OBJECTIVE_MAP_OBJ_IDENTIFIER |
| MIN_NORMALIZED_MEASURE | NUMBER |  |  |  | MIN_NORMALIZED_MEASURE |
| ATTEMPT_ID | NUMBER |  | 18 |  | ATTEMPT_ID |
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
| WLF_LMC_OBJECTIVES_N1 | Non Unique | Default | SEQUENCING_INFO_ID, EXTERNAL_IDENTIFIER |
| WLF_LMC_OBJECTIVES_PK | Unique | FUSION_TS_TX_DATA | OBJECTIVE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
