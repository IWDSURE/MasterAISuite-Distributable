# FAI_APPLICATIONS

Stores the data related to the applications

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiapplications-4938.html#faiapplications-4938](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiapplications-4938.html#faiapplications-4938)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_APPLICATIONS_PK | APPLICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| APPLICATION_ID | NUMBER |  | 18 | Yes | Unique identifier for the application |
| APPLICATION_NAME | VARCHAR2 | 300 |  | Yes | Stores the name of the application |
| APPLICATION_CODE | VARCHAR2 | 300 |  | Yes | Stores the code of the application |
| VERSION | NUMBER |  | 9 | Yes | This column specifies the application version. |
| STATUS | VARCHAR2 | 32 |  |  | This column provides status of the application. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the application. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the application. |
| SPECIFICATION | CLOB |  |  |  | Stores the specification related to the application |
| LAUNCHABLE | VARCHAR2 | 32 |  |  | Identifies whether the application can be launched by systems |
| SEEDED_FLAG | VARCHAR2 | 1 |  |  | This column differentiates seeded data from customer created. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_APPLICATIONS_U1 | Unique | Default | APPLICATION_ID, ORA_SEED_SET1 |
| FAI_APPLICATIONS_U11 | Unique | Default | APPLICATION_ID, ORA_SEED_SET2 |
| FAI_APPLICATIONS_U2 | Unique | Default | APPLICATION_CODE, VERSION, STATUS, ORA_SEED_SET1 |
| FAI_APPLICATIONS_U21 | Unique | Default | APPLICATION_CODE, VERSION, STATUS, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
