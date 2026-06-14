# WLF_PROVIDER_INSTR_ACCOUNTS

Table to store provider instructor accounts information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderinstraccounts-31038.html#wlfproviderinstraccounts-31038](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfproviderinstraccounts-31038.html#wlfproviderinstraccounts-31038)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PROVIDER_INSTR_ACCOUNTS_PK | PROVIDER_INSTR_ACCOUNT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROVIDER_INSTR_ACCOUNT_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| PROVIDER_INSTR_ACCOUNT_NUMBER | VARCHAR2 | 30 |  |  | PROVIDER_INSTR_ACCOUNT_NUMBER |
| PROVIDER_ACCOUNT_ID | NUMBER |  | 18 | Yes | Indicates provider id |
| INSTRUCTOR_ID | NUMBER |  | 18 | Yes | Indicates instructor id |
| USERNAME | VARCHAR2 | 100 |  | Yes | Indicates username of a provider account |
| STATUS | VARCHAR2 | 32 |  | Yes | Indicates status of a provider instructor account |
| ADDITIONAL_INFO | VARCHAR2 | 1000 |  |  | Indicates additional information of a provider account |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PROVIDER_INSTR_ACCOUNTS_N1 | Non Unique | Default | PROVIDER_ACCOUNT_ID, STATUS |
| WLF_PROVIDER_INSTR_ACCOUNTS_N2 | Non Unique | Default | INSTRUCTOR_ID, STATUS |
| WLF_PROVIDER_INSTR_ACCOUNTS_N3 | Non Unique | Default | PROVIDER_INSTR_ACCOUNT_NUMBER |
| WLF_PROVIDER_INSTR_ACCOUNTS_U1 | Unique | Default | PROVIDER_INSTR_ACCOUNT_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
