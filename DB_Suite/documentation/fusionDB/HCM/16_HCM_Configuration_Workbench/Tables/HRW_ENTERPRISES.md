# HRW_ENTERPRISES

An Enterprise Configuration Enterprise contains information for the enterprise defined within an Enterprise Configuration. An enterprise is a collection of companies and or other legal entities recognized in law that are under common control. An enterprise is the high-level container for all data in the Fusion application.

## Details

**Schema:** FUSION

**Object owner:** HRW

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwenterprises-20933.html#hrwenterprises-20933](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrwenterprises-20933.html#hrwenterprises-20933)

## Primary Key

| Name | Columns |
|------|----------|
| HRW_ENTERPRISES_PK | ENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENT_ID | NUMBER |  | 18 | Yes | Primary key for the HRW_ENTERPRISES table |
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 100 |  | Yes | NAME |
| SHORT_NAME | VARCHAR2 | 10 |  | Yes | SHORT_NAME |
| PREVIOUS_NAME | VARCHAR2 | 100 |  |  | SAVE THE NAME ON LOADING |
| PRIMARY_INDUSTRY | VARCHAR2 | 80 |  | Yes | PRIMARY_INDUSTRY |
| BUSINESS_UNIT_OPTION | VARCHAR2 | 30 |  |  | BUSINESS_UNIT_OPTION |
| LOCATION_ID | NUMBER |  | 18 |  | LOCATION_ID |
| PREVIOUS_LOCATION_ID | NUMBER |  | 18 |  | SAVE LOCATION ID ON LOADING |
| WORKER_NUMBER_GENERATION | VARCHAR2 | 50 |  |  | Worker Number Generation Method |
| EMPLOYMENT_MODEL | VARCHAR2 | 50 |  |  | Employment Model |
| ALLOW_EMP_TERMS_OVERRIDE | VARCHAR2 | 1 |  |  | Allow Employment Terms Override at Assignment flag |
| EFFECTIVE_START_DATE | DATE |  |  |  | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRW_ENTERPRISES_F1 | Non Unique | Default | CONFIGURATION_ID |
| HRW_ENTERPRISES_F2 | Non Unique | Default | LOCATION_ID |
| HRW_ENTERPRISES_PK | Unique | Default | ENT_ID |

---

[← Back to Index](../16_HCM_Configuration_Workbench_Tables_Index.md)
