# BEN_PL_TYP_EXTEND_PERIOD

BEN_PL_TYP_EXTEND_PERIOD identifies the benefit plan types to extend the assessment period.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypextendperiod-15448.html#benpltypextendperiod-15448](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpltypextendperiod-15448.html#benpltypextendperiod-15448)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_TYP_EXTEND_PERIOD_PK | EXTEND_PL_TYP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXTEND_PL_TYP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PL_TYP_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PL_TYP_F.PL_TYP_ID. |
| ENTITLEMENT_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_ENTITLEMENT.ENTITLEMENT_ID. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_TYP_EXT_PERD_PK | Unique | FUSION_TS_TX_DATA | EXTEND_PL_TYP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
