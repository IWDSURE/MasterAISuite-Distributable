# PAY_RUN_TYPE_ORG_METHODS_F

Organisation level payment methods associated with a particular run type.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypeorgmethodsf-23078.html#payruntypeorgmethodsf-23078](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payruntypeorgmethodsf-23078.html#payruntypeorgmethodsf-23078)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RUN_TYPE_ORG_METHODS_PK | RUN_TYPE_ORG_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_TYPE_ORG_METHOD_ID | NUMBER |  | 18 | Yes | Primary key |
| RUN_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_RUN_TYPES_F |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_ORG_PAYMENT_METHODS_F |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PRIORITY | NUMBER |  | 18 | Yes | Priority order for different payment methods for a run type. |
| PERCENTAGE | NUMBER |  | 22 |  | Percentage to be allocated if there is more than one payment method. |
| AMOUNT | NUMBER |  |  |  | Fixed amount to be allocated if more than one payment method. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_RUN_TYPE_ORG_METHODS_F_N1 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_RUN_TYPE_ORG_METHODS_F_N2 | Non Unique | Default | RUN_TYPE_ID |
| PAY_RUN_TYPE_ORG_METHODS_PK | Unique | Default | RUN_TYPE_ORG_METHOD_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
