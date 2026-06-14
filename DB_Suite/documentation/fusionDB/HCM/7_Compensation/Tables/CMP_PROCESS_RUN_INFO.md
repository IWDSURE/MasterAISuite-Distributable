# CMP_PROCESS_RUN_INFO

Stores information about the persons processed in a compensation process run. It stores all processed employee information, errors and warnings. For example, it can be used to run a post process audit report to reflect all the employees eligible for a particular focal review.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprocessruninfo-11148.html#cmpprocessruninfo-11148](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpprocessruninfo-11148.html#cmpprocessruninfo-11148)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PROCESS_RUN_INFO_PK | PROCESS_RUN_INFO_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_RUN_INFO_ID | NUMBER |  | 18 | Yes | PROCESS_RUN_INFO_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| FULL_NAME | VARCHAR2 | 240 |  |  | FULL_NAME |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PROCESS_RUN_INFO_N1 | Non Unique | Default | PERSON_ID |
| CMP_PROCESS_RUN_INFO_N2 | Non Unique | Default | ASSIGNMENT_ID |
| CMP_PROCESS_RUN_INFO_PK | Unique | Default | PROCESS_RUN_INFO_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
