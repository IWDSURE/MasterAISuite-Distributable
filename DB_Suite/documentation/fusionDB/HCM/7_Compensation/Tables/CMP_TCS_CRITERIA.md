# CMP_TCS_CRITERIA

Table holds Comp Tcs Criteria records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteria-26045.html#cmptcscriteria-26045](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcscriteria-26045.html#cmptcscriteria-26045)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_CRITERIA_PK | CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRITERIA_ID | NUMBER |  | 18 | Yes | System generate primary key |
| CRITERIA_DEF_ID | NUMBER |  | 18 |  | CRITERIA_DEF_ID |
| STMT_ID | NUMBER |  | 18 |  | Statement Id of the statement if this criteria tag is added in Welcome/Summary page RTE |
| STMT_PERD_ID | NUMBER |  | 18 |  | Statement Period Id of the statement if this criteria tag is added in Welcome page RTE |
| CAT_ID | NUMBER |  | 18 |  | Category Id of the category if this tag is added in Category RTE |
| TAG_PLACE | VARCHAR2 | 32 |  | Yes | RTE place from where tag is being added |
| CRITERIA | VARCHAR2 | 2000 |  |  | Complete Criteria Value |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| CRITERIA_NAME | VARCHAR2 | 80 |  |  | Placeholder string value for the criteria name |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_CRITERIA_U1 | Unique | Default | CRITERIA_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
