# FAI_ML_USECASES_B

This Table stores the ML Use Cases Information

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimlusecasesb-27794.html#faimlusecasesb-27794](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faimlusecasesb-27794.html#faimlusecasesb-27794)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_ML_USECASES_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | Auto generated primary key for this table. |
| USECASE_CODE | VARCHAR2 | 80 |  | Yes | The internal code for the usecase which also represents the ML Apps that is deployed in OCI |
| FAMILY | VARCHAR2 | 80 |  | Yes | Product family for the UseCase, e.g., ERP, HCM, SCM |
| INTRODUCED_IN_RELEASE | VARCHAR2 | 20 |  | Yes | In which Fusion release this usecase was introduced |
| ADDN_INFO | CLOB |  |  |  | Any additional seed information that needs to be captured for the ML usecase. |
| ADDN_TXN_INFO | CLOB |  |  |  | Any additional lifecycle information that needs to be captured for the ML usecase during lifecycle activities. |
| STATUS | VARCHAR2 | 80 |  | Yes | Life Cycle Status of the UseCase |
| STATUS_DETAILS | VARCHAR2 | 4000 |  |  | Details of the lifecycle status of the usecase. May contain detailed error message in case of error during lifecycle operation |
| ML_APP_NAME | VARCHAR2 | 200 |  | Yes | Corresponding ML Application Name |
| ML_APP_IMPL_NAME | VARCHAR2 | 200 |  |  | ML Application Implementation Name |
| ML_APP_VERSION | VARCHAR2 | 20 |  | Yes | ML Application Implementation Version |
| ML_APP_INSTANCE_ID | VARCHAR2 | 200 |  |  | ML Application Instance identifier post activation |
| LAST_ACTIVATION_DATE | TIMESTAMP |  |  |  | Date the ML Application last activated |
| LAST_DEACTIVATION_DATE | TIMESTAMP |  |  |  | Date the ML Application last deactivated |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_ML_USECASES_B_U1 | Unique | Default | ID, ORA_SEED_SET1 |
| FAI_ML_USECASES_B_U11 | Unique | Default | ID, ORA_SEED_SET2 |
| FAI_ML_USECASES_B_U2 | Unique | Default | USECASE_CODE, ML_APP_VERSION, ORA_SEED_SET1 |
| FAI_ML_USECASES_B_U21 | Unique | Default | USECASE_CODE, ML_APP_VERSION, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
