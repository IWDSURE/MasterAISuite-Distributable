# PER_PUBLIC_PRSN_SEC_PROFILES

Public Person Security Profile Table-Each Record stores conditions used to generate security condition based on person and assignment related objects.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpublicprsnsecprofiles-15407.html#perpublicprsnsecprofiles-15407](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpublicprsnsecprofiles-15407.html#perpublicprsnsecprofiles-15407)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PUBLIC_PRSN_SEC_PROFIL_PK | PUBLIC_PRSN_SEC_PROF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PUBLIC_PRSN_SEC_PROF_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | This option provides unrestricted security access to the specific public person security profile |
| NAME | VARCHAR2 | 240 |  | Yes | Name for the Public Person Security Profiles. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether a person security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| ACCESS_TO_OWN_RECORD | VARCHAR2 | 1 |  | Yes | This option allows users access to their own records, those records belong to the instance set defined by the profile, regardless of whether they satisfy the other criteria in the profile. If users are denied access to their own records, then users are unable to access them even if they would otherwise belong to the instance set defined by the profile. |
| INCLUDE_FUTURE_ASSIGNMENT | VARCHAR2 | 1 |  | Yes | This option allows accessing future dated assignments. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description for the public person security profile. |
| SECURE_BY_USER_LEGAL_EMPLOYER | VARCHAR2 | 1 |  | Yes | Secure by logged-on user legal employer. |
| SECURE_BY_USER_BUSINESS_UNIT | VARCHAR2 | 1 |  | Yes | Secure by logged-on user business unit. |
| SECURE_BY_SYSTEM_PERSON_TYPE | VARCHAR2 | 1 |  | Yes | Secure by system person type. |
| SECURE_BY_USER_PERSON_TYPE | VARCHAR2 | 1 |  | Yes | Secure by user person type. |
| SECURE_BY_PERSON_TYPE | VARCHAR2 | 1 |  | Yes | Secure by person type. |
| SECURE_BY_LEGAL_EMPLOYER | VARCHAR2 | 1 |  | Yes | Secure by legal employer. |
| SECURE_BY_BUSINESS_UNIT | VARCHAR2 | 1 |  | Yes | Secure by business unit. |
| SECURE_BY_DEPARTMENT | VARCHAR2 | 1 |  | Yes | Secure by department. |
| SECURE_BY_JOB | VARCHAR2 | 1 |  | Yes | Secure by job. |
| SECURE_BY_GRADE | VARCHAR2 | 1 |  | Yes | Secure by grade. |
| SECURE_BY_PERSON | VARCHAR2 | 1 |  | Yes | Secure by person. |
| SECURE_BY_ASGN_STATUS | VARCHAR2 | 1 |  | Yes | Secure by Assignment Status. |
| SECURE_BY_USER_DEFINED_FILTER | VARCHAR2 | 1 |  | Yes | Secure by user defined filter. |
| USER_DEFINED_PWA_FILTER | CLOB |  |  |  | User defined PWA filter |
| USER_DEFINED_EXPRESSION | VARCHAR2 | 4000 |  |  | User defined expression. |
| SECURE_BY_WORKER_ATTRIBUTE | VARCHAR2 | 1 |  | Yes | Secure by worker attribute. |
| SECURE_BY_OTHER_INCLUSION | VARCHAR2 | 1 |  |  | Secure by other inclusion criteria. |
| INDEX_NAME | VARCHAR2 | 240 |  |  | Index name. |
| IS_ENTERPRISE_LEVEL | VARCHAR2 | 1 |  |  | Enterprise level configuration. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PUBLIC_PRSN_SEC_PROF_PK | Unique | FUSION_TS_TX_DATA | PUBLIC_PRSN_SEC_PROF_ID |
| PER_PUBLIC_PRSN_SEC_PROF_U1 | Unique | Default | UPPER("NAME") |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
