# BEN_PRTT_ASSOCD_INSTN_F

BEN_PRTT_ASSOCD_INSTN_F  identifies multiple values for reimbursement or other processing instructions.  For example, if a person requests reimbursement for a higher amount than is currently available, each increment reimbursed  of part of the requested value will be associated with each additional increment thus identifying the parts of the total payment.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttassocdinstnf-23675.html#benprttassocdinstnf-23675](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttassocdinstnf-23675.html#benprttassocdinstnf-23675)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_ASSOCD_INSTN_F_PK | PRTT_ASSOCD_INSTN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTT_ASSOCD_INSTN_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| TAKE_BOTH_FLAG | VARCHAR2 | 30 |  | Yes | Take Both Y or N. |
| SOURCE_ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRIES_F. |
| TARGET_ELEMENT_ENTRY_VALUE_ID | NUMBER |  | 18 |  | Foreign key to PAY_ELEMENT_ENTRIES_F. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTT_ASSOCD_INSTN_F_N1 | Non Unique | Default | SOURCE_ELEMENT_ENTRY_VALUE_ID |
| BEN_PRTT_ASSOCD_INSTN_F_N2 | Non Unique | Default | TARGET_ELEMENT_ENTRY_VALUE_ID |
| BEN_PRTT_ASSOCD_INSTN_F_PK | Unique | Default | PRTT_ASSOCD_INSTN_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
