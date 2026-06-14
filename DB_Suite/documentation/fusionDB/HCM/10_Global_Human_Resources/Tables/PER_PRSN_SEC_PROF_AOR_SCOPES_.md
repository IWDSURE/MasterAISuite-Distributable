# PER_PRSN_SEC_PROF_AOR_SCOPES_

Person Security Profile AOR Scopes Table: This table will hold scope of areas of responsibility preference selected by end-user when 'Secure by Areas Of Responsibility' option is enabled for person security profile.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecprofaorscopes-17454.html#perprsnsecprofaorscopes-17454](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perprsnsecprofaorscopes-17454.html#perprsnsecprofaorscopes-17454)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PRSN_SEC_PROF_AOR_SCO_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PRSN_SEC_PROF_AOR_SCOPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRSN_SEC_PROF_AOR_SCOPE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign key to PER_PERSON_SECURITY_PROFILES. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | Responsibility type for areas of responsibility. |
| SCOPE_OF_RESPONSIBILITY | VARCHAR2 | 30 |  |  | Scope of areas of responsibility which will be used to identify secured access. |
| ALL_EMPLOYEE_ACCESS | VARCHAR2 | 1 |  |  | This field indicates access to all employees. |
| ALL_CONT_WORKER_ACCESS | VARCHAR2 | 1 |  |  | This field indicates access to all contingent workers. |
| ALL_PENDING_WORKER_ACCESS | VARCHAR2 | 1 |  |  | This field indicates access to all pending workers. |
| ALL_NON_WORKER_ACCESS | VARCHAR2 | 1 |  |  | This field indicates access to all non workers. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ALL_CAND_WITH_OFFER_ACCESS | VARCHAR2 | 1 |  |  | This field indicates access to all candidates with offer. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PRSN_SEC_PROF_AORN1_ | Non Unique | Default | PRSN_SEC_PROF_AOR_SCOPE_ID, LAST_UPDATE_DATE |
| PER_PRSN_SEC_PROF_AOR_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, PRSN_SEC_PROF_AOR_SCOPE_ID |
| PER_PRSN_SEC_PROF_AOR_SCO_U1_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, PERSON_SECURITY_PROFILE_ID, RESPONSIBILITY_TYPE, SCOPE_OF_RESPONSIBILITY |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
