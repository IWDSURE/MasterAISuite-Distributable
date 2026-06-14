# HWR_ASSIGNMENT_B

The assignment table stores the assignments of tasks to resources.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrassignmentb-31154.html#hwrassignmentb-31154](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrassignmentb-31154.html#hwrassignmentb-31154)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ASSIGNMENT_B_PK | ASSIGNMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | This stores the unique assignment ID. |  |
| PROJECT_KEY | VARCHAR2 | 500 |  | Yes | This is the unique key of the project that contains the assignment. |  |
| ASSIGNMENT_KEY | VARCHAR2 | 500 |  | Yes | This is the unique key of the assignment within the project. |  |
| TASK_ID | NUMBER |  | 18 | Yes | This refers to the TASK_ID in HWR_TASK_B. |  |
| RESOURCE_ID | NUMBER |  | 18 |  | This refers to RESOURCE_ID in HWR_RESOURCE_B. |  |
| RESOURCE_KEY | VARCHAR2 | 500 |  |  | This refers to RESOURCE_KEY in HWR_RESOURCE_B. |  |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | This is the profile Id of the assigned user. | Obsolete |
| HOURS_OF_WORK | NUMBER |  |  |  | This stores the number of hours on the assignment. |  |
| RESOURCE_PERCENT | NUMBER |  |  |  | This stores the percent of resources used for the assignment. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWR_ASSIGNMENT_B_U1 | Unique | FUSION_TS_TX_DATA | ASSIGNMENT_ID |  |
| HWR_ASSIGNMENT_B_U2 | Unique | FUSION_TS_TX_DATA | PROJECT_KEY, ASSIGNMENT_KEY |  |
| HWR_ASSIGNMENT_B_U3 | Unique | FUSION_TS_TX_DATA | TASK_ID, PRFL_ID | Obsolete |
| HWR_ASSIGNMENT_B_U4 | Unique | FUSION_TS_TX_DATA | TASK_ID, RESOURCE_ID |  |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
