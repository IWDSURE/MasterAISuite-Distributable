# IRC_AI_GIG_FILTERS

This table is used to store the gig recommendation filters

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaigigfilters-25226.html#ircaigigfilters-25226](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaigigfilters-25226.html#ircaigigfilters-25226)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AI_GIG_FILTERS_PK | GIG_FILTER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GIG_FILTER_ID | NUMBER |  | 18 | Yes | Primary key of the table. Populated by  sequence. |
| LEGAL_EMPLOYER_ID | NUMBER |  | 18 |  | Stores the selected legal employer id |
| JOB_ID | NUMBER |  | 18 |  | Stores the selected job id |
| BUSINESS_UNIT_ID | NUMBER |  | 18 |  | Stores the selected business unit id |
| DEPARTMENT_ID | NUMBER |  | 18 |  | Stores the selected department id |
| JOB_GRADE_CODE | VARCHAR2 | 32 |  |  | Stores the selected jobgrade code |
| LOCATION_ID | NUMBER |  | 18 |  | Stores the selected location id |
| FILTER_TYPE_CODE | VARCHAR2 | 32 |  |  | Reference to the filter type against hich this record is created.if we are storing legal employed id then value will be ORA_LEGAL_EMPLOYER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AI_GIG_FILTERS_PK | Unique | Default | GIG_FILTER_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
