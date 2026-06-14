# IRC_LI_REQUISITION_MAPPING

Stores the requisition mapping between ORC and LinkedIn

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirequisitionmapping-8991.html#irclirequisitionmapping-8991](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclirequisitionmapping-8991.html#irclirequisitionmapping-8991)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_REQUISITION_MAPPING_PK | REQUISITION_ID, LI_JOB_POSTING_TASK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUISITION_ID | NUMBER |  | 18 | Yes | Primary Key of the table and also foreign key to IRC_REQUISITIONS_B |
| LI_JOB_POSTING_TASK_ID | VARCHAR2 | 255 |  | Yes | Job Posting Task Identifier from LinkedIn |
| LI_JOB_POSTING_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the posting status of ORC job in LinkedIn. The corresponding lookup type is ORA_LI_RSC_JOB_POSTING_STATUS |
| ADDITIONAL_INFO1 | VARCHAR2 | 2000 |  |  | To store additional info for the requisition |
| LI_JOB_POSTING_URN | VARCHAR2 | 255 |  |  | Job Posting Identifier from LinkedIn |
| LOCATION | VARCHAR2 | 360 |  |  | Location details of the requisition |
| HTTP_CODE | VARCHAR2 | 20 |  |  | The HTTP status code received from LI |
| ACTIVE_FLAG | VARCHAR2 | 1 |  |  | If the location of this row is the current location for the requisition |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUISITION_ACTION_CODE | VARCHAR2 | 20 |  |  | Represents the action code of Requisition synchronization |
| REQUISITION_SYNC_STATUS | VARCHAR2 | 20 |  |  | Represents the status code of Requisition synchronization |
| REQUISITION_SYNC_ERROR | VARCHAR2 | 1000 |  |  | Synchronization error of Requisition, if any such error happened |
| REQUISITION_SYNC_INFO | VARCHAR2 | 2000 |  |  | Additional Information from requisition synchronization |
| REQUISITION_SYNC_DATE | TIMESTAMP |  |  |  | Requsisition Last synchronization Date |
| CALL_TYPE | VARCHAR2 | 30 |  |  | Represents the source of this record, requisition and requisition status |
| REQUISITION_PAYLOAD | VARCHAR2 | 1000 |  |  | This is the column to store OAC(Onsite Apply Configuration) data for Requisition |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LI_REQUISITION_MAPPING_N1 | Non Unique | Default | LI_JOB_POSTING_URN |
| IRC_LI_REQUISITION_MAPPING_PK | Unique | Default | REQUISITION_ID, LI_JOB_POSTING_TASK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
