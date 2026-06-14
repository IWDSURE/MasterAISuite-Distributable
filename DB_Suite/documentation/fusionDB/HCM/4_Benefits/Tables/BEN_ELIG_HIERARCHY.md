# BEN_ELIG_HIERARCHY

Complex eligibility criteria from different tables will be populated into this table through a procedure for displaying the view all hierarchy for any eligiblity profile.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelighierarchy-25430.html#benelighierarchy-25430](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelighierarchy-25430.html#benelighierarchy-25430)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_HIERARCHY_PK | BATCH_ID, ELIGY_PRFL_ID, LINE_NUMBER |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_ID | NUMBER |  | 18 | Yes | process generated primary key id |
| ELIGY_PRFL_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_ELIGY_PRFL |
| LINE_NUMBER | NUMBER |  | 18 | Yes | Identifies the line sequence number |
| SUB_CATEGORY_ID | NUMBER |  | 18 |  | SUB_CATEGORY_ID |
| ELIG_CAT_CODE | VARCHAR2 | 30 |  | Yes | Category code for the eligibility profile |
| ELIG_SUB_CAT_CODE | VARCHAR2 | 30 |  | Yes | Sub category code of the eligibility profile |
| NAME | VARCHAR2 | 200 |  | Yes | Derived criteria name |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| BEN_ELIG_HIERARCHY_U1 | Unique | BATCH_ID, ELIGY_PRFL_ID, LINE_NUMBER |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
