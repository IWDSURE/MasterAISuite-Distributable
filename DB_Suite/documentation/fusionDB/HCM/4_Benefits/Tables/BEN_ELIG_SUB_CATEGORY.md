# BEN_ELIG_SUB_CATEGORY

BEN_ELIG_SUB_CATEGORY identifies various sub categories within eligibility categories.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsubcategory-9223.html#beneligsubcategory-9223](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligsubcategory-9223.html#beneligsubcategory-9223)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_SUB_CATEGORY_PK | SUB_CATEGORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUB_CATEGORY_ID | NUMBER |  | 18 | Yes | Eligibility Sub category Identifier |
| CATEGORY_ID | NUMBER |  | 18 | Yes | Identifies Eligibility Category |
| NAME | VARCHAR2 | 80 |  | Yes | Name of the eligibility sub Category |
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
| BEN_ELIG_SUB_CATEGORY_U1 | Unique | SUB_CATEGORY_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
