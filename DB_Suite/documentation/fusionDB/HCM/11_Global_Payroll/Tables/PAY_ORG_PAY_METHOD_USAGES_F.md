# PAY_ORG_PAY_METHOD_USAGES_F

Org Pay Method Usages is the Date Tracked table that stores details of the different payment methods that are used as personal payment methods for assignments on a given Payroll. e.g For Payroll A we have Cash and Cheque as payment methods for Payroll B we can have Mag Tape and Cheque as payment methods. So if the employee has Payroll A attached to him he can use Cash and Cheque as personal payments and if has Payroll B attached he can have Mag Tape and Cheque as personal payment methods..

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodusagesf-22522.html#payorgpaymethodusagesf-22522](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodusagesf-22522.html#payorgpaymethodusagesf-22522)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ORG_PAY_METHOD_USAGES_PK | ORG_PAY_METHOD_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_PAY_METHOD_USAGE_ID | NUMBER |  | 18 | Yes | Surrogate primary key for DateTrack entity. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ORG_PAYMENT_METHODS. |
| PAYROLL_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_PAYROLLS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ORG_PAY_METHOD_USAGES_FK1 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_ORG_PAY_METHOD_USAGES_PK | Unique | Default | ORG_PAY_METHOD_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
