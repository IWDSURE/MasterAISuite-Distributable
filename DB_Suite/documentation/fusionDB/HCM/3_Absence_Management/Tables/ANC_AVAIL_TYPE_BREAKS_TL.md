# ANC_AVAIL_TYPE_BREAKS_TL

This table holds the translated short description of defined availability type breaks.

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailtypebreakstl-29765.html#ancavailtypebreakstl-29765](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancavailtypebreakstl-29765.html#ancavailtypebreakstl-29765)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_AVAIL_TYPE_BREAKS_TL_PK | AVAILABILITY_TYPE_BREAK_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AVAILABILITY_TYPE_BREAK_ID | NUMBER |  | 18 | Yes | The Identifier of Availability Type Break. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| NAME | VARCHAR2 | 240 |  | Yes | Translated availability type break name. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_AVAIL_TYPE_BREAKS_TL_PK | Unique | Default | AVAILABILITY_TYPE_BREAK_ID, LANGUAGE |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
