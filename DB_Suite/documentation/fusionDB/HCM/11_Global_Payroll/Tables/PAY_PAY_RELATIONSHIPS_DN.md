# PAY_PAY_RELATIONSHIPS_DN

Payroll relationships non datetrack table

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrelationshipsdn-15366.html#paypayrelationshipsdn-15366](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypayrelationshipsdn-15366.html#paypayrelationshipsdn-15366)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PAY_RELATIONSHIPS_DN_PK | PAYROLL_RELATIONSHIP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | PAYROLL_RELATIONSHIP_ID |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  | Yes | END_DATE |
| PAYROLL_RELATIONSHIP_NUMBER | VARCHAR2 | 30 |  | Yes | Relationship Number |
| PAYROLL_STAT_UNIT_ID | NUMBER |  | 18 | Yes | PAYROLL_STAT_UNIT_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| RELATIONSHIP_TYPE_ID | NUMBER |  | 18 | Yes | RELATIONSHIP_TYPE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PAY_RELATIONSHIPS_DN_N1 | Non Unique | Default | PERSON_ID |
| PAY_PAY_RELATIONSHIPS_DN_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_NUMBER |
| PAY_PAY_RELATIONSHIPS_DN_N3 | Non Unique | Default | LEGISLATIVE_DATA_GROUP_ID |
| PAY_PAY_RELATIONSHIPS_DN_N4 | Non Unique | Default | UPPER("PAYROLL_RELATIONSHIP_NUMBER") |
| PAY_PAY_RELATIONSHIPS_DN_N5 | Non Unique | Default | PAYROLL_STAT_UNIT_ID |
| PAY_PAY_RELATIONSHIPS_DN_PK | Unique | Default | PAYROLL_RELATIONSHIP_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
