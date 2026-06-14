# PAY_EVENT_VALUE_QUAL_F

This table holds teh Qualifiers for an Event Value Change.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventvaluequalf-24438.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventvaluequalf-24438.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_VALUE_QUAL_ID | NUMBER |  | 18 | Yes | Primary Key |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_VALUE_CHANGE_ID | NUMBER |  | 18 | Yes | Foreign Key to Value Change. |
| EVENT_QUALIFIER_ID | NUMBER |  | 18 | Yes | Foreign Key to Event Qualifiers |
| QUALIFIER_VALUE | VARCHAR2 | 80 |  | Yes | Qualifying value |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Legislative Data Group |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| ENTERPRISE_ID | NUMBER |  | 18 |  | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_EVENT_VALUE_QUAL_F_N1 | Non Unique | Default | EVENT_VALUE_CHANGE_ID |
| PAY_EVENT_VALUE_QUAL_F_N20 | Non Unique | PAY_EVENT_VALUE_QUAL_F_N20 | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_EVENT_VALUE_QUAL_F_PK | Unique | Default | EVENT_VALUE_QUAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_EVENT_VALUE_QUAL_F_PK1 | Unique | PAY_EVENT_VALUE_QUAL_F_PK1 | EVENT_VALUE_QUAL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
