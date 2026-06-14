# PER_EMPL_CONFIGURATIONS

This is transcational table for storing configuration of conversion to hours based on fast formula.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplconfigurations-8518.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peremplconfigurations-8518.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_EMPL_CONFIGURATIONS_PK | CONFIGURATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | This column is used to store the CONFIGURATION_ID value. |
| RECORD_CREATOR | VARCHAR2 | 100 |  | Yes | This column is used to store the RECORD_CREATOR value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIGURATION_CODE | VARCHAR2 | 100 |  |  | This column is used to store the CONFIGURATION_CODE value. |
| CONFIGURATION_TYPE | VARCHAR2 | 100 |  |  | This column is used to store the CONFIGURATION_TYPE value. |
| HOURS_IN_DAY | NUMBER |  | 18 |  | This column is used to store the HOURS_IN_DAY value. |
| HOURS_IN_MONTH | NUMBER |  | 18 |  | This column is used to store the HOURS_IN_MONTH value. |
| HOURS_IN_YEAR | NUMBER |  | 18 |  | This column is used to store the HOURS_IN_YEAR value. |
| HOURS_SOURCE | VARCHAR2 | 30 |  |  | This column is used to store the HOURS_SOURCE value. |
| CONVERSION_FF_ID | NUMBER |  | 18 |  | This column is used to store the CONVERSION_FF value. |
| VERSION_CODE | VARCHAR2 | 30 |  |  | This column is used to store the VERSION_CODE value. |
| ATTRIBUTE_NAME | VARCHAR2 | 100 |  |  | This column is used to store the ATTRIBUTE_NAME value. |
| ATTRIBUTE_VALUE | VARCHAR2 | 200 |  |  | This column is used to store the ATTRIBUTE_VALUE value. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ATTR1_VALUE | VARCHAR2 | 100 |  |  | This column has been added for use in future. |
| ATTR2_VALUE | VARCHAR2 | 100 |  |  | This column has been added for use in future. |
| ATTR_NUMBER1 | NUMBER |  | 18 |  | This column has been added for use in future. |
| ATTR_NUMBER2 | NUMBER |  | 18 |  | This column has been added for use in future. |
| ATTR_DATE1 | DATE |  |  |  | This column has been added for use in future. |
| ATTR_DATE2 | DATE |  |  |  | This column has been added for use in future. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_EMPL_CONFIGURATIONS_U1 | Unique | Default | CONFIGURATION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
