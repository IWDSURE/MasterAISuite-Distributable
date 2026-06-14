# PAY_BAL_GRP_USAGES_TL

This table contains translated information for PAY_BAL_GRP_USAGES.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalgrpusagestl-13152.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalgrpusagestl-13152.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_GRP_USAGES_TL_PK | BAL_GRP_USAGE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BAL_GRP_USAGE_ID | NUMBER |  | 18 | Yes | BAL_GRP_USAGE_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| GROUP_USAGE_NAME | VARCHAR2 | 120 |  | Yes | GROUP_USAGE_NAME |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_GRP_USAGES_TL_N1 | Non Unique | Default | GROUP_USAGE_NAME, LANGUAGE |
| PAY_BAL_GRP_USAGES_TL_PK | Unique | Default | BAL_GRP_USAGE_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_BAL_GRP_USAGES_TL_PK1 | Unique | Default | BAL_GRP_USAGE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
