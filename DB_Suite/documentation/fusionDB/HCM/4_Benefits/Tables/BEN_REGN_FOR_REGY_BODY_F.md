# BEN_REGN_FOR_REGY_BODY_F

BEN_REGN_FOR_REGY_BODY_F identifies the discreet piece of legislation or policy and the group responsible for creating or administering it.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnforregybodyf-19159.html#benregnforregybodyf-19159](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benregnforregybodyf-19159.html#benregnforregybodyf-19159)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_REGN_FOR_REGY_BODY_F_PK | REGN_FOR_REGY_BODY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REGN_FOR_REGY_BODY_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| REGN_ADMIN_CD | VARCHAR2 | 30 |  |  | Regulation administrative code. |
| REGN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ORGANIZATION_UNITS. |
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
| BEN_REGN_F_REGY_BODY_F_FK2 | Non Unique | Default | ORGANIZATION_ID |
| BEN_REGN_F_REGY_BODY_F_N1 | Non Unique | Default | REGN_ID |
| BEN_REGN_F_REGY_BODY_F_PK | Unique | Default | REGN_FOR_REGY_BODY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
