# PAY_ORG_PAYER_MAPPINGS_F

Rules used within an Organization Payment Method to determine the appropriate source bank account.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpayermappingsf-25181.html#payorgpayermappingsf-25181](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payorgpayermappingsf-25181.html#payorgpayermappingsf-25181)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_ORG_PAYER_MAPPINGS_F_PK | ORG_PAYER_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ORG_PAYER_MAPPING_ID | NUMBER |  | 18 | Yes | ORG_PAYER_MAPPING_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ORG_PAYMENT_METHOD_ID | NUMBER |  | 18 | Yes | ORG_PAYMENT_METHOD_ID |
| DEFAULT_FLAG | VARCHAR2 | 5 |  |  | DEFAULT_FLAG |
| TAX_UNIT_ID | NUMBER |  | 18 |  | TAX_UNIT_ID |
| PAYMENT_CRITERIA | VARCHAR2 | 60 |  |  | PAYMENT_CRITERIA |
| THIRD_PARTY_FLAG | VARCHAR2 | 5 |  |  | Flag to indicate that this is for a Third Party Payment. |
| THIRD_PARTY_PAYEE_ID | NUMBER |  | 18 |  | The Payee to be paid by this method. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_ORG_PAYER_MAPPINGS_F_FK1 | Non Unique | Default | ORG_PAYMENT_METHOD_ID |
| PAY_ORG_PAYER_MAPPINGS_F_PK | Unique | Default | ORG_PAYER_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
