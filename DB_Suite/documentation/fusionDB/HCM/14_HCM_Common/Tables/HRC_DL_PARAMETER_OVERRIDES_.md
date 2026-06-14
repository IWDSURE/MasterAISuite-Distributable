# HRC_DL_PARAMETER_OVERRIDES_

The HRC DL PARAMETER OVERRIDES table is used for storing overridden VALUES of configuration parameters for the ESS processing of DataLoader Jobs.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparameteroverrides-9855.html#hrcdlparameteroverrides-9855](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlparameteroverrides-9855.html#hrcdlparameteroverrides-9855)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_PARAMETER_OVERRIDES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PARAMETER_OVERRIDE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARAMETER_OVERRIDE_ID | NUMBER |  | 18 | Yes | PARAMETER_OVERRIDE_ID |
| PARAMETER_ID | NUMBER |  | 18 |  | PARAMETER_ID |
| OVERRIDE_LEVEL | VARCHAR2 | 32 |  |  | OVERRIDE_LEVEL |
| OVERRIDE_VALUE | VARCHAR2 | 240 |  |  | OVERRIDE_VALUE |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_PARAM_OVERRIDES_N1_ | Non Unique | HRC_DL_PARAM_OVERRIDES_N1_ | PARAMETER_ID |
| HRC_DL_PARAM_OVERRIDES_U1_ | Unique | HRC_DL_PARAM_OVERRIDES_U1_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PARAMETER_OVERRIDE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
