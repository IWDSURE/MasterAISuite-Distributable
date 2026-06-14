# HWR_FLW_OPERATION_B

The operation table is used to store operations.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwoperationb-9788.html#hwrflwoperationb-9788](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrflwoperationb-9788.html#hwrflwoperationb-9788)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_FLW_OPERATION_B_PK | OPERATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| OPERATION_ID | NUMBER |  | 18 | Yes | This is the primary key of the operation table. | Active |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. | Active |
| UUID | VARCHAR2 | 255 |  | Yes | This is the generated instance identifier associated to this operation. | Active |
| REST_ID | VARCHAR2 | 256 |  |  | ID of the REST Operation. | Active |
| REQUEST_OD | VARCHAR2 | 256 |  |  | The request object definition of the operation. | Active |
| RESPONSE_OD | VARCHAR2 | 256 |  |  | The response object definition of the Operation. | Active |
| NAME | VARCHAR2 | 255 |  | Yes | The display name value for the operation. | Active |
| OPERATION_TYPE | VARCHAR2 | 64 |  |  | This stores the type of Operation. | Active |
| CONNECTION_SPEC | CLOB |  |  |  | The connection spec for the operation. | Active |
| IS_SEEDED_DATA | VARCHAR2 | 1 |  | Yes | A flag to indicate the whether the operation is seeded: Y for yes; N for no. | Active |
| IS_INTERNAL | VARCHAR2 | 1 |  | Yes | A flag to indicate the internal state: Y for yes; N for no. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_FLW_OPERATION_B_U1 | Unique | FUSION_TS_TX_DATA | OPERATION_ID | Active |
| HWR_FLW_OPERATION_B_U2 | Unique | FUSION_TS_TX_DATA | UUID | Active |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
