# WLF_PROVIDER_TEMPLATES

Table to store provider templates information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidertemplates-26256.html#wlfprovidertemplates-26256](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfprovidertemplates-26256.html#wlfprovidertemplates-26256)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_TEMPLATES_PK | PROVIDER_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_TEMPLATE_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_TEMPLATE_NUMBER | VARCHAR2 | 30 |  |  | PROVIDER_TEMPLATE_NUMBER |
| PROVIDER_INSTR_ACCOUNT_ID | NUMBER |  | 18 | Yes | Indicates relation id |
| STATUS | VARCHAR2 | 32 |  | Yes | Indicates status of a template |
| TEMPLATE_ID | VARCHAR2 | 240 |  |  | Indicates Template Id |
| TEMPLATE_TYPE | VARCHAR2 | 30 |  |  | Indicates type of a template |
| TEMPLATE_NAME | VARCHAR2 | 240 |  |  | Indicates value of a template |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_TEMPLATES_N1 | Non Unique | Default | PROVIDER_INSTR_ACCOUNT_ID, STATUS |
| WLF_PROVIDER_TEMPLATES_N2 | Non Unique | Default | TEMPLATE_TYPE, STATUS |
| WLF_PROVIDER_TEMPLATES_N3 | Non Unique | Default | PROVIDER_TEMPLATE_NUMBER |
| WLF_PROVIDER_TEMPLATES_U1 | Unique | Default | PROVIDER_TEMPLATE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
