# BEN_VALD_HRCHY_DETAILS

BEN_VALD_HRCHY_DETAILS holds aggregate or detail information for a particular path in the compensation object hierarchy with repect to a reporting rule.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldhrchydetails-10815.html#benvaldhrchydetails-10815](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benvaldhrchydetails-10815.html#benvaldhrchydetails-10815)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_VALD_HRCHY_DETAILS_PK | VALD_HRCHY_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VALD_HRCHY_DETAIL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| POPL_VALD_HRCHY_ID | NUMBER |  | 18 |  | Foreign key to BEN_POPL_VALD_HRCHY. |
| VALD_HRCHY_SMRY_ID | NUMBER |  | 18 |  | Foreign key to BEN_VALD_HRCHY_SMRY. |
| VALD_RPT_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_VALD_RPT_TYP. |
| COMP_LVL_CD | VARCHAR2 | 30 |  |  | Compensation level code. |
| AGG_TYP_CD | VARCHAR2 | 30 |  |  | Aggregate type cd. |
| VALUE1 | VARCHAR2 | 30 |  |  | Attribute to store additional varchar information. |
| VALUE2 | VARCHAR2 | 30 |  |  | Attribute to store additional varchar information. |
| VALUE3 | VARCHAR2 | 30 |  |  | Attribute to store additional varchar information. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_VALD_HRCHY_DETAILS_U1 | Unique | Default | VALD_HRCHY_DETAIL_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
