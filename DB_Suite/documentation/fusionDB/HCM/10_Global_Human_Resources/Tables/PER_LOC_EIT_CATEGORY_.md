# PER_LOC_EIT_CATEGORY_

Table that stores the Location EIT category information.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perloceitcategory-20517.html#perloceitcategory-20517](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perloceitcategory-20517.html#perloceitcategory-20517)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOC_EIT_CATEGORY_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_ID | NUMBER |  | 18 | Yes | LOCATION_ID |
| CATEGORY_CODE | VARCHAR2 | 80 |  |  | CATEGORY_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LOC_EIT_CATEGORYN1_ | Non Unique | Default | LOCATION_ID |
| PER_LOC_EIT_CATEGORY_U1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
