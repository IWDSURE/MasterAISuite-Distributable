# PER_ROLES_DN_TL

Translated role names for roles used in the system

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdntl-30693.html#perrolesdntl-30693](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perrolesdntl-30693.html#perrolesdntl-30693)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ROLES_DN_TL_PK | ROLE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ROLE_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| ROLE_NAME | VARCHAR2 | 4000 |  |  | Denotes the name for the Role. | Active |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Denotes description for the Role. | Active |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. | Active |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ROLES_DN_TL_N1 | Non Unique | FUSION_TS_SEED | ROLE_NAME |
| PER_ROLES_DN_TL_U1 | Unique | FUSION_TS_SEED | ROLE_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
