# IRC_DOCUMENT_INDEXING_TRK

This table is to track the indexed candidate along with status of passed for successfully indexed candidate and status of failed for non indexed candidate while incremental indexing is being ran.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdocumentindexingtrk-24922.html#ircdocumentindexingtrk-24922](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdocumentindexingtrk-24922.html#ircdocumentindexingtrk-24922)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DOCUMENT_INDEXING_TRK_PK | TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TRACKING_ID | NUMBER |  | 18 | Yes | Primary key of the table |
| AFFECTED_ENTITY_ID | NUMBER |  | 18 | Yes | This column stores the person id of the person. |
| ENTITY_TYPE | VARCHAR2 | 32 |  | Yes | This column will store the different entity type for which the indexing tracking is happening (like CANDIDATE, REQUISITION, LOCATION). |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column will store the error message of the candidate which failed to index. |
| INDEX_STATUS | VARCHAR2 | 32 |  |  | This column will store the status of indexing (FAILED/PASSED). |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | This column stores the request id of the ESS job. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DOCUMENT_INDEXING_TRK_N1 | Non Unique | Default | AFFECTED_ENTITY_ID |
| IRC_DOCUMENT_INDEXING_TRK_PK | Unique | Default | TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
