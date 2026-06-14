# HRA_PF_TASK_ROLES_TL

Performance Process flow Task Roles (Translates)

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapftaskrolestl-12215.html#hrapftaskrolestl-12215](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapftaskrolestl-12215.html#hrapftaskrolestl-12215)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_PF_TASK_ROLES_TL_PK | PROCESS_TASK_ROLE_ID, BUSINESS_GROUP_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PROCESS_TASK_ROLE_ID | NUMBER |  | 18 | Yes | Foreign Key Process tak role Id which also forms a part of the composite Id |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |  |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |  |
| MGR_TASK_NAME | VARCHAR2 | 240 |  |  | Translated task  name for Manager |  |
| WKR_TASK_NAME | VARCHAR2 | 240 |  |  | Translated task name for worker |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_PF_TASK_ROLES_TL_PK | Unique | FUSION_TS_TX_DATA | PROCESS_TASK_ROLE_ID, BUSINESS_GROUP_ID, LANGUAGE |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
