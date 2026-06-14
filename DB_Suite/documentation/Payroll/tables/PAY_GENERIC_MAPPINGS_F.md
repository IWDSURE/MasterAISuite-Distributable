# PAY_GENERIC_MAPPINGS_F

Generic table to store value mappings for use with LOVs

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericmappingsf-14811.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paygenericmappingsf-14811.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_GENERIC_MAPPINGS_PK | GENERIC_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GENERIC_MAPPING_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| TYPE_NAME | VARCHAR2 | 30 |  | Yes | The Type of value being stored. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group that owns the row |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation that owns the row |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Enterprise Id that owns the row |
| VALUE1 | VARCHAR2 | 30 |  |  | VALUE1 |
| VALUE2 | VARCHAR2 | 30 |  |  | VALUE2 |
| VALUE3 | VARCHAR2 | 30 |  |  | VALUE3 |
| VALUE4 | VARCHAR2 | 30 |  |  | VALUE4 |
| VALUE5 | VARCHAR2 | 30 |  |  | VALUE5 |
| VALUE6 | VARCHAR2 | 30 |  |  | VALUE6 |
| VALUE7 | VARCHAR2 | 30 |  |  | VALUE7 |
| VALUE8 | VARCHAR2 | 30 |  |  | VALUE8 |
| VALUE9 | VARCHAR2 | 30 |  |  | VALUE9 |
| VALUE10 | VARCHAR2 | 30 |  |  | VALUE10 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_GENERIC_MAPPINGS_N1 | Non Unique | Default | TYPE_NAME, VALUE1, VALUE2, VALUE3 |
| PAY_GENERIC_MAPPINGS_PK | Unique | Default | GENERIC_MAPPING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
