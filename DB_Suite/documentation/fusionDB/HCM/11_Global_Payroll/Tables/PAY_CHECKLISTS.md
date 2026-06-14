# PAY_CHECKLISTS

Table stores checklist template utilized while checklist is created at runrtime

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklists-24951.html#paychecklists-24951](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paychecklists-24951.html#paychecklists-24951)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_CHECKLISTS_PK | CHECKLIST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_ID | NUMBER |  | 18 | Yes | CHECKLIST_ID |
| BASE_CHECKLIST_ID | NUMBER |  | 18 | Yes | BASE_CHECKLIST_ID |
| BASE_CHECKLIST_NAME | VARCHAR2 | 100 |  | Yes | BASE_CHECKLIST_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PARENT_CHECKLIST_ID | NUMBER |  | 18 |  | PARENT_CHECKLIST_ID |
| BASE_FLOW_ID | NUMBER |  | 18 | Yes | BASE_FLOW_ID |
| BASE_FLOW_TASK_ID | NUMBER |  | 18 |  | BASE_FLOW_TASK_ID |
| CHECKLIST_TYPE | VARCHAR2 | 30 |  | Yes | CHECKLIST_TYPE |
| OWNER_TYPE | VARCHAR2 | 18 |  |  | OWNER_TYPE |
| OWNER_ID | VARCHAR2 | 4000 |  |  | OWNER_ID |
| RUN_SEQUENCE | NUMBER |  | 18 |  | RUN_SEQUENCE |
| CATEGORY_TYPE | VARCHAR2 | 30 |  |  | CATEGORY_TYPE |
| SUB_CATEGORY_TYPE | VARCHAR2 | 30 |  |  | SUB_CATEGORY_TYPE |
| DEST_UI_URL | VARCHAR2 | 200 |  |  | DEST_UI_URL |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_CHECKLISTS_N1 | Non Unique | Default | BASE_CHECKLIST_ID |
| PAY_CHECKLISTS_N2 | Non Unique | Default | BASE_FLOW_TASK_ID |
| PAY_CHECKLISTS_N20 | Non Unique | Default | SGUID |
| PAY_CHECKLISTS_PK | Unique | Default | CHECKLIST_ID, ORA_SEED_SET1 |
| PAY_CHECKLISTS_PK1 | Unique | Default | CHECKLIST_ID, ORA_SEED_SET2 |
| PAY_CHECKLISTS_U2 | Unique | Default | BASE_FLOW_ID, BASE_CHECKLIST_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET1 |
| PAY_CHECKLISTS_U21 | Unique | Default | BASE_FLOW_ID, BASE_CHECKLIST_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
