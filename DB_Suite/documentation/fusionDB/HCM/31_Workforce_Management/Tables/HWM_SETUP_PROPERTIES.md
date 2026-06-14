# HWM_SETUP_PROPERTIES

To store Time Decimal format as property values against Properties.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmsetupproperties-25814.html#hwmsetupproperties-25814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmsetupproperties-25814.html#hwmsetupproperties-25814)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_SETUP_PROPERTIES_PK | SETUP_PROPERTY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SETUP_PROPERTY_ID | NUMBER |  | 18 | Yes | SETUP_PROPERTY_ID |
| CONTEXT | VARCHAR2 | 30 |  | Yes | CONTEXT |
| CATEGORY | VARCHAR2 | 30 |  | Yes | CATEGORY |
| PROPERTY_NAME | VARCHAR2 | 80 |  | Yes | PROPERTY_NAME |
| VARCHAR_VALUE1 | VARCHAR2 | 80 |  |  | VARCHAR_VALUE1 |
| VARCHAR_VALUE2 | VARCHAR2 | 80 |  |  | VARCHAR_VALUE2 |
| VARCHAR_VALUE3 | VARCHAR2 | 80 |  |  | VARCHAR_VALUE3 |
| VARCHAR_VALUE4 | VARCHAR2 | 80 |  |  | VARCHAR_VALUE4 |
| VARCHAR_VALUE5 | VARCHAR2 | 80 |  |  | VARCHAR_VALUE5 |
| NUMBER_VALUE1 | NUMBER |  |  |  | NUMBER_VALUE1 |
| NUMBER_VALUE2 | NUMBER |  |  |  | NUMBER_VALUE2 |
| NUMBER_VALUE3 | NUMBER |  |  |  | NUMBER_VALUE3 |
| NUMBER_VALUE4 | NUMBER |  |  |  | NUMBER_VALUE4 |
| NUMBER_VALUE5 | NUMBER |  |  |  | NUMBER_VALUE5 |
| SETUP_VERSION | NUMBER |  |  | Yes | SETUP_VERSION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| ENABLE_TZ_FLAG | VARCHAR2 | 30 |  |  | ENABLE_TZ_FLAG |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_SETUP_PROPERTIES_U1 | Unique | Default | SETUP_PROPERTY_ID |
| HWM_SETUP_PROPERTIES_U2 | Unique | Default | CONTEXT, CATEGORY, PROPERTY_NAME |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
