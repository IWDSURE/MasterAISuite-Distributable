# HRC_DL_CANDIDATE_ERR_OBJS

HRC_DL_CANDIDATE_ERR_OBJS table is used to hold details about imported candidates load errors.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcandidateerrobjs-3466.html#hrcdlcandidateerrobjs-3466](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlcandidateerrobjs-3466.html#hrcdlcandidateerrobjs-3466)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_CANDIDATE_ERR_OBJS_PK | CANDIDATE_ERR_OBJ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CANDIDATE_ERR_OBJ_ID | NUMBER |  | 18 | Yes | CANDIDATE_ERR_OBJ_ID |
| CANDIDATE_IMPORT_ID | NUMBER |  | 18 | Yes | CANDIDATE_IMPORT_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | OBJECT_TYPE |
| LOGICAL_OBJECT | BLOB |  |  |  | LOGICAL_OBJECT |
| LOGICAL_OBJECT_SECURE | BLOB |  |  |  | LOGICAL_OBJECT_SECURE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| DATA_SET_BUS_OBJ_ID | NUMBER |  | 18 | Yes | DATA_SET_BUS_OBJ_ID |
| ERROR_CODE | VARCHAR2 | 80 |  |  | ERROR_CODE |
| ERROR_DESCRIPTION | VARCHAR2 | 4000 |  |  | ERROR_DESCRIPTION |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_CANDIDATE_ERR_OBJS_N1 | Non Unique | Default | CANDIDATE_IMPORT_ID |
| HRC_DL_CANDIDATE_ERR_OBJS_U1 | Unique | Default | CANDIDATE_ERR_OBJ_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
