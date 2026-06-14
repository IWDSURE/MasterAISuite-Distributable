# ANC_CAL_EVENTSET_B

Organization Calendar Event Set Table

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccaleventsetb-18495.html#anccaleventsetb-18495](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/anccaleventsetb-18495.html#anccaleventsetb-18495)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_CAL_EVENTSET_PK | CAL_EVENTSET_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAL_EVENTSET_ID | NUMBER |  | 18 | Yes | Calendar Event Set ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise ID |
| START_DATE | DATE |  |  | Yes | Start Date |
| END_DATE | DATE |  |  | Yes | End Date |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_CAL_EVENTSET_PK | Unique | Default | CAL_EVENTSET_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
