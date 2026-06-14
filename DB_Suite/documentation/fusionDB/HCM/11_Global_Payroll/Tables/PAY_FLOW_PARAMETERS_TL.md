# PAY_FLOW_PARAMETERS_TL

Holds translated information for PAY_FLOW_PARAMETERS.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparameterstl-18009.html#payflowparameterstl-18009](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflowparameterstl-18009.html#payflowparameterstl-18009)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLOW_PARAMETERS_TL_PK | FLOW_PARAMETER_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLOW_PARAMETER_ID | NUMBER |  | 18 | Yes | FLOW_PARAMETER_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| PARAMETER_NAME | VARCHAR2 | 250 |  | Yes | PARAMETER_NAME |
| DESCRIPTION | VARCHAR2 | 250 |  |  | DESCRIPTION |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLOW_PARAMETERS_TL_PK | Unique | Default | FLOW_PARAMETER_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_FLOW_PARAMETERS_TL_PK1 | Unique | Default | FLOW_PARAMETER_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
