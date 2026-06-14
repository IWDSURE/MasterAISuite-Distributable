# ANC_GRP_CRITERIA

This table holds information of  the absence group criteria.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancgrpcriteria-5906.html#ancgrpcriteria-5906](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancgrpcriteria-5906.html#ancgrpcriteria-5906)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_GRP_CRITERIA_PK | GRP_CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GRP_CRITERIA_ID | NUMBER |  | 18 | Yes | GRP_CRITERIA_ID |
| GRP_ID | NUMBER |  | 18 |  | GRP_ID |
| ORDER_NUM | NUMBER |  | 9 |  | ORDER_NUM |
| LEFT_PARAM_NUM | NUMBER |  | 9 |  | LEFT_PARAM_NUM |
| CRITERIA_ID | NUMBER |  | 18 |  | CRITERIA_ID |
| CRITERIA_NAME | VARCHAR2 | 100 |  |  | CRITERIA_NAME |
| CRITERIA_DISPLAY_NAME | VARCHAR2 | 100 |  |  | CRITERIA_DISPLAY_NAME |
| OPERATOR_ID | NUMBER |  | 18 |  | OPERATOR_ID |
| OPERATOR_NAME | VARCHAR2 | 100 |  |  | OPERATOR_NAME |
| RIGHT_PARAM_NUM | NUMBER |  | 9 |  | RIGHT_PARAM_NUM |
| VALUE_CHAR | VARCHAR2 | 30 |  |  | VALUE_CHAR |
| VALUE_NUMBER | NUMBER |  | 18 |  | VALUE_NUMBER |
| VALUE_DATE | DATE |  |  |  | VALUE_DATE |
| VALUE_TS | TIMESTAMP |  |  |  | VALUE_TS |
| BOOL_OPER_CD | VARCHAR2 | 30 |  |  | BOOL_OPER_CD |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_GRP_CRITERIA_PK | Unique | Default | GRP_CRITERIA_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
