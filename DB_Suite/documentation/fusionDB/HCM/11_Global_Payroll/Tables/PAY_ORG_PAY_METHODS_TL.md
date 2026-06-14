# PAY_ORG_PAY_METHODS_TL

Holds translated information for PAY_ORG_PAY_METHODS_F.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodstl-24148.html#payorgpaymethodstl-24148](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpaymethodstl-24148.html#payorgpaymethodstl-24148)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ORG_PAY_METHODS_TL_PK | ORG_PAYMENT_METHOD_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | ORG_PAYMENT_METHOD_ID |
| ORG_PAYMENT_METHOD_NAME | VARCHAR2 | 80 |  | Yes | ORG_PAYMENT_METHOD_NAME |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ORG_PAY_METHODS_TL_N2 | Non Unique | Default | LANGUAGE, ORG_PAYMENT_METHOD_NAME |
| PAY_ORG_PAY_METHODS_TL_N3 | Non Unique | Default | UPPER("ORG_PAYMENT_METHOD_NAME") |
| PAY_ORG_PAY_METHODS_TL_PK | Unique | Default | ORG_PAYMENT_METHOD_ID, LANGUAGE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
