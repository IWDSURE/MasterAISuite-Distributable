# PAY_TIME_DEPEND_VALUES

This table hold the definition of a value that can change over time.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimedependvalues-14246.html#paytimedependvalues-14246](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytimedependvalues-14246.html#paytimedependvalues-14246)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TIME_DEPEND_VALUES_PK | TIME_DEPEND_VALUE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TIME_DEPEND_VALUE_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| BASE_NAME | VARCHAR2 | 30 |  | Yes | BASE_NAME |
| SOURCE_ID | NUMBER |  | 18 | Yes | SOURCE_ID |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Source of the value |
| LEVEL_TYPE | VARCHAR2 | 30 |  | Yes | At what level is te value calculated. |
| STORE_HISTORY | VARCHAR2 | 20 |  | Yes | Store Historical values |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 16 |  | LEGISLATIVE_DATA_GROUP_ID |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_TIME_DEPEND_VALUES_PK | Unique | Default | TIME_DEPEND_VALUE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
