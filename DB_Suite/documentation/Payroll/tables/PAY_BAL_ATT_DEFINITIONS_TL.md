# PAY_BAL_ATT_DEFINITIONS_TL

This table contains translated information for PAY_BAL_ATT_DEFINITIONS.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalattdefinitionstl-24169.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paybalattdefinitionstl-24169.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_BAL_ATT_DEFNS_TL_PK | ATTRIBUTE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_BAL_ATT_DEFINITIONS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| USER_ATTRIBUTE_NAME | VARCHAR2 | 240 |  | Yes | User balance attribute name |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_BAL_ATT_DEFNS_TL_N1 | Non Unique | Default | USER_ATTRIBUTE_NAME, LANGUAGE |
| PAY_BAL_ATT_DEFNS_TL_PK | Unique | Default | ATTRIBUTE_ID, LANGUAGE, ORA_SEED_SET1 |
| PAY_BAL_ATT_DEFNS_TL_PK1 | Unique | Default | ATTRIBUTE_ID, LANGUAGE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
