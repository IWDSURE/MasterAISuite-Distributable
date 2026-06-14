# HR_ALL_POSITIONS_F_TL

Positions table storing translatable position attributes

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsftl-31127.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrallpositionsftl-31127.html)

## Primary Key

| Name | Columns |
|------|----------|
| HR_ALL_POSITIONS_F_TL_PK | POSITION_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POSITION_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Surrogate key. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| NAME | VARCHAR2 | 240 |  | Yes | Denotes the translated name of the position. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| HR_ALL_POSITIONS_F_TL_N1 | Non Unique | Default | NAME, LANGUAGE |
| HR_ALL_POSITIONS_F_TL_N2 | Non Unique | Default | UPPER("NAME"), LANGUAGE, EFFECTIVE_END_DATE, EFFECTIVE_START_DATE |
| HR_ALL_POSITIONS_F_TL_N3 | Non Unique | Default | LAST_UPDATE_DATE |
| HR_ALL_POSITIONS_F_TL_PK | Unique | Default | POSITION_ID, LANGUAGE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
