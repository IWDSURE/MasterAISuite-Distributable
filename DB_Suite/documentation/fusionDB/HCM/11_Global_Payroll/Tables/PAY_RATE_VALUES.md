# PAY_RATE_VALUES

This table contains the calculated rate values for the Payroll Relationship.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratevalues-27305.html#payratevalues-27305](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payratevalues-27305.html#payratevalues-27305)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RATE_VALUES_PK | RATE_VALUE_ID, START_DATE, END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RATE_VALUE_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| RATE_DEFINITION_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_DATE_DEFINITIONS_F |
| PAYROLL_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_PAY_RELATIONSHIPS_DN |
| START_DATE | DATE |  |  | Yes | Start Date of Rate |
| END_DATE | DATE |  |  | Yes | End Date Of Rate |
| VALUE | NUMBER |  |  | Yes | Value of the Rate |
| PERIODICITY | VARCHAR2 | 30 |  | Yes | Periodicity of the Value |
| FTE_FLAG | VARCHAR2 | 30 |  | Yes | Indicates if FTE is applyed. |
| PAYROLL_TERM_ID | NUMBER |  | 18 |  | Forein key to PAY_PAYROLL_TERMS |
| PAYROLL_ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLL_ASSIGNMENTS |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CURRENCY | VARCHAR2 | 30 |  |  | Rate Currency Code |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_RATE_VALUES_N1 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, START_DATE, END_DATE, RATE_DEFINITION_ID |
| PAY_RATE_VALUES_N2 | Non Unique | Default | PAYROLL_RELATIONSHIP_ID, RATE_DEFINITION_ID, PAYROLL_TERM_ID, PAYROLL_ASSIGNMENT_ID |
| PAY_RATE_VALUES_PK | Unique | Default | RATE_VALUE_ID, START_DATE, END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
