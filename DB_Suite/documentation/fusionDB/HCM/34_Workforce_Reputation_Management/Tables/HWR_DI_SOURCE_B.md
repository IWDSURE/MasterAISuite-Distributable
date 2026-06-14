# HWR_DI_SOURCE_B

This table stores the seeded sources for hwr.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdisourceb-23941.html#hwrdisourceb-23941](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdisourceb-23941.html#hwrdisourceb-23941)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_SOURCE_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. |
| SOURCE_NAME | VARCHAR2 | 500 |  |  | This is the source name. |
| SOURCE_TYPE_ID | NUMBER |  | 18 |  | The id of the data source type. |
| SOURCE_ID | NUMBER |  | 18 |  | The id of the data source. |
| META_DATA | VARCHAR2 | 4000 |  |  | Additional meta data for the source. |
| SOURCE_CATEGORY | VARCHAR2 | 500 |  |  | This is the source category. |
| SETUP_STATUS | VARCHAR2 | 500 |  |  | This is the setup status. |
| IS_ACTIVE | NUMBER |  | 1 |  | The enable status.The value is either 0 or 1. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_SOURCE_B_U1 | Unique | Default | ID, ORA_SEED_SET1 |
| HWR_DI_SOURCE_B_U11 | Unique | Default | ID, ORA_SEED_SET2 |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
