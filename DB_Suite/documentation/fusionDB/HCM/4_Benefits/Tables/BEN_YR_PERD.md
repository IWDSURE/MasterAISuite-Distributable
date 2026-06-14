# BEN_YR_PERD

BEN_YR_PERD  identifies the start and stop dates for a plan year which may apply to multiple plans and/or programs.  Typically, the elapsed time represents a year; however, in certain limited situations such as, a short year necessitated by realigning the plan's year, the period of time can be less than a year.  This period of time is an important factor for many plans.   For example: some plans specify year-to-date contribution limits that apply to this year instead of to a calendar or fiscal year also  in some countries, many plans require that participant elections remain in force for the duration of the plan unless a life event occurs which allows an enrollment change.The financial disclosure of plan assets and liabilities may be stated in the plan year.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benyrperd-6420.html#benyrperd-6420](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benyrperd-6420.html#benyrperd-6420)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_YR_PERD_PK | YR_PERD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| YR_PERD_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERDS_IN_YR_NUM | NUMBER |  | 18 |  | Periods in year. |
| PERD_TM_UOM_CD | VARCHAR2 | 30 |  |  | Period time unit of measure. |
| PERD_TYP_CD | VARCHAR2 | 30 |  |  | Period type. |
| END_DATE | DATE |  |  | Yes | End date. |
| START_DATE | DATE |  |  | Yes | Start Date. |
| LMTN_YR_STRT_DT | DATE |  |  |  | Limitation year start date. |
| LMTN_YR_END_DT | DATE |  |  |  | Limitation year end date. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_YR_PERD_PK | Unique | Default | YR_PERD_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
