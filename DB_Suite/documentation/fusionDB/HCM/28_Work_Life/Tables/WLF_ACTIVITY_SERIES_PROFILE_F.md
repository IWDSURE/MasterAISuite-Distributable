# WLF_ACTIVITY_SERIES_PROFILE_F

Table to store activity series profile.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfactivityseriesprofilef-9445.html#wlfactivityseriesprofilef-9445](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfactivityseriesprofilef-9445.html#wlfactivityseriesprofilef-9445)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_ACT_SERIES_PRF_F_PK | SERIES_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SERIES_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| SERIES_NUMBER | VARCHAR2 | 30 |  |  | UserKey for uniquely identifying activity series. |
| REPEAT_TYPE | VARCHAR2 | 30 |  |  | Indicates repeat type of activity series. |
| REPEAT_UNTIL_DATE | TIMESTAMP |  |  |  | Indicates date till which actvities are to be created. |
| ACTIVITY_SUFFIX | VARCHAR2 | 250 |  |  | Indicates title suffix to be used while creating bulk activities. |
| WEEK_DAYS | VARCHAR2 | 250 |  |  | Indicates days of week activities are be created. |
| WEEK_NUMBER | VARCHAR2 | 250 |  |  | Indicates week number of the month. |
| DAY_NUMBER | VARCHAR2 | 250 |  |  | Indicates day number of the month. |
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
| WLF_ACT_SERIES_PRF_F_N1 | Non Unique | Default | SERIES_NUMBER |
| WLF_ACT_SERIES_PRF_F_U1 | Unique | Default | SERIES_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
