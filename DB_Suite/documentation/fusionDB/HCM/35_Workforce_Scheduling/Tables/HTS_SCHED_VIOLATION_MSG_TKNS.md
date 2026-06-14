# HTS_SCHED_VIOLATION_MSG_TKNS

This table is associated with a specific violation message and represents the typed message tokens that were used to format it the violation message.

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolationmsgtkns-30726.html#htsschedviolationmsgtkns-30726](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htsschedviolationmsgtkns-30726.html#htsschedviolationmsgtkns-30726)

## Primary Key

| Name | Columns |
|------|----------|
| HTS_SCHED_VIOLATION_TKNS_PK | SCHED_VIOLATION_MSG_TKN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SCHED_VIOLATION_MSG_TKN_ID | NUMBER |  | 18 | Yes | The unique ID of the validation message token. |
| SCHED_VIOLATION_ID | NUMBER |  | 18 | Yes | The identifier of the associated validation violation whose error message this token is contributing to. |
| SCHED_FULL_VALIDATION_ID | NUMBER |  | 18 | Yes | The validation this error message token belongs to. |
| TOKEN_NAME | VARCHAR2 | 30 |  | Yes | The name used in the message format as placeholder for the token value. |
| TOKEN_TYPE_CODE | VARCHAR2 | 30 |  | Yes | The code identifying both the type of the token value and the way to format it, so to translate it as a string. |
| TOKEN_DATA_TYPE_CODE | VARCHAR2 | 30 |  | Yes | A code indicating if the token value is a number, string or date. |
| TOKEN_NUMBER_VALUE | NUMBER |  |  |  | This column stores the token value for the number token types. |
| TOKEN_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | This column stores the value's lookup type for any
token that is a LOOKUP_CODE |
| TOKEN_STRING_VALUE | VARCHAR2 | 30 |  |  | This column stores the token value for the string token types. |
| TOKEN_DATE_VALUE | DATE |  |  |  | This column stores the token value for the date token types. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | EnterpriseId |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HTS_SCHED_VIOLATION_TKNS_N1 | Non Unique | Default | SCHED_VIOLATION_ID |
| HTS_SCHED_VIOLATION_TKNS_N2 | Non Unique | Default | SCHED_FULL_VALIDATION_ID |
| HTS_SCHED_VIOLATION_TKNS_PK | Unique | Default | SCHED_VIOLATION_MSG_TKN_ID |

---

[← Back to Index](../35_Workforce_Scheduling_Tables_Index.md)
