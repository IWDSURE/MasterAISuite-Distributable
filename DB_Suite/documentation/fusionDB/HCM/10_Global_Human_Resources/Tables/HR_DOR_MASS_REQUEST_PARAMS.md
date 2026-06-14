# HR_DOR_MASS_REQUEST_PARAMS

This table contains information about the mass request's parameters .

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequestparams-7328.html#hrdormassrequestparams-7328](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrdormassrequestparams-7328.html#hrdormassrequestparams-7328)

## Primary Key

| Name | Columns |
|------|----------|
| hr_dor_mass_request_params_PK | MASS_REQUEST_ID, NAME |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | Uniquely identifies a mass request. |
| NAME | VARCHAR2 | 1000 |  | Yes | Mass request's parameter name. |
| DATATYPE | VARCHAR2 | 250 |  |  | Mass request's parameter data type. |
| VALUE | VARCHAR2 | 4000 |  |  | Mass request's parameter value. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HR_DOR_MASS_REQUEST_PARAMS_PK | Unique | HR_DOR_MASS_REQUEST_PARAMS_PK | MASS_REQUEST_ID, NAME |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
