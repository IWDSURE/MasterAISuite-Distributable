# CMP_TCS_CRITERIA_DEF

Table hold Comp Tcs Criteria Definition records

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteriadef-18097.html#cmptcscriteriadef-18097](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteriadef-18097.html#cmptcscriteriadef-18097)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CRITERIA_DEF_PK | CRITERIA_DEF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRITERIA_DEF_ID | NUMBER |  | 18 | Yes | Criteria Def Id - Primary Key |
| CRITERIA_NAME | VARCHAR2 | 80 |  | Yes | Criteria/ Field Name |
| CRITERIA | VARCHAR2 | 2000 |  |  | Complete Condition |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CRITERIA_DEF_U1 | Unique | Default | CRITERIA_DEF_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
