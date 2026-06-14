# HRC_DL_OBJECT_HIERARCHIES

Table to store the top object in the hierarchy for required objects as defined from product annotation

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlobjecthierarchies-22294.html#hrcdlobjecthierarchies-22294](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlobjecthierarchies-22294.html#hrcdlobjecthierarchies-22294)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_OBJECT_HIERS_PK | OBJECT_HIERARCHY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_HIERARCHY_ID | NUMBER |  | 18 | Yes | OBJECT_HIERARCHY_ID |
| TOP_BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | TOP_BUSINESS_OBJECT_ID |
| HIERARCHY_HASH | VARCHAR2 | 100 |  |  | HIERARCHY_HASH |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_OBJECT_HIERS_N1 | Non Unique | Default | TOP_BUSINESS_OBJECT_ID |
| HRC_DL_OBJECT_HIERS_U1 | Unique | Default | OBJECT_HIERARCHY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
