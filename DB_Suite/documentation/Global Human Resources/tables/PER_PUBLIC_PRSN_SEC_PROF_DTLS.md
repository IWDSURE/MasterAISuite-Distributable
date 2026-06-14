# PER_PUBLIC_PRSN_SEC_PROF_DTLS

Public Person Security Profile Detail Table-Each Record stores conditions used to generate security condition based on person and assignment related objects.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpublicprsnsecprofdtls-3241.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpublicprsnsecprofdtls-3241.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PUB_PRSN_SECPROF_DTL_PK | PUBLIC_PRSN_SEC_PROF_DTL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PUBLIC_PRSN_SEC_PROF_DTL_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PUBLIC_PRSN_SEC_PROF_ID | NUMBER |  | 18 | Yes | Foreign key to public person security profile |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CRITERIA | VARCHAR2 | 30 |  | Yes | Security criteria |
| SCOPE | VARCHAR2 | 1 |  | Yes | Included or excluded |
| ID_VALUE | NUMBER |  | 18 |  | Id value to be used for condition |
| STR_VALUE | VARCHAR2 | 500 |  |  | String value to be used for condition |
| OPERATOR | VARCHAR2 | 80 |  |  | String operator to be used for condition |
| PWA_WORKER_ATTRIBUTE | VARCHAR2 | 80 |  |  | Attribute to be used for condition |
| PWA_WORKER_ATTRIBUTE_PATH | VARCHAR2 | 500 |  |  | Attribute path. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PUB_PRSN_SECPROF_DTL_N1 | Non Unique | Default | PUBLIC_PRSN_SEC_PROF_ID |
| PER_PUB_PRSN_SECPROF_DTL_PK | Unique | Default | PUBLIC_PRSN_SEC_PROF_DTL_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
