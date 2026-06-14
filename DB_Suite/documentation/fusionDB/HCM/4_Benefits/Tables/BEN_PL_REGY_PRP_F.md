# BEN_PL_REGY_PRP_F

BEN_PL_REGY_PRP_F identifies the role and purpose for this regulatory body in the administration of this plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplregyprpf-17026.html#benplregyprpf-17026](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplregyprpf-17026.html#benplregyprpf-17026)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_REGY_PRP_F_PK | PL_REGY_PRPS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_REGY_PRPS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PL_REGY_PRPS_CD | VARCHAR2 | 30 |  |  | Plan regulatory purpose. |
| PL_REGY_BOD_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_REGY_BODY_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_REGY_PRP_F_N1 | Non Unique | Default | PL_REGY_BOD_ID |
| BEN_PL_REGY_PRP_F_PK | Unique | Default | PL_REGY_PRPS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
