# HRS_GROUP_SPACE_ASSOC

This table will hold the relation between application objects like Goals, Appraisals etc with the Group Space. ObjectId will be corresponding to GoalId, AppraisalId etc and ObjectType would be Goals, Appraisal etc.

## Details

**Schema:** FUSION

**Object owner:** HRS

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsgroupspaceassoc-18735.html#hrsgroupspaceassoc-18735](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrsgroupspaceassoc-18735.html#hrsgroupspaceassoc-18735)

## Primary Key

| Name | Columns |
|------|----------|
| HRS_GROUP_SPACE_ASSOC_PK | GROUP_SPACE_ASSOC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_SPACE_ASSOC_ID | NUMBER |  | 18 | Yes | It is the primary key of this table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Application Object Id is stored as OBJECT_ID. e.g., it can be GOAL_ID |
| OBJECT_TYPE | VARCHAR2 | 80 |  | Yes | Application Object Type is stored as OBJECT_TYPE. e.g., it can be GOALS to represent Goals. |
| PRIMARY_FLAG | VARCHAR2 | 30 |  |  | It is used for visually identifying one of the group spaces related to a business object as primary. Primary group space cannot be unlinked from the business object. |
| GROUP_SPACE_NAME | VARCHAR2 | 256 |  |  | This is used for storing WebCenter Group Space name, which is  associated with OBJECT_ID and OBJECT_TYPE. |
| GROUP_SPACE_GUID | VARCHAR2 | 64 |  | Yes | This is used for storing WebCenter Group Space GUID, which is  associated with OBJECT_ID and OBJECT_TYPE. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRS_GROUP_SPACE_ASSOC_PK | Unique | FUSION_TS_TX_DATA | GROUP_SPACE_ASSOC_ID |
| HRS_GROUP_SPACE_ASSOC_UK3 | Unique | FUSION_TS_TX_DATA | GROUP_SPACE_GUID, OBJECT_ID, OBJECT_TYPE |

---

[← Back to Index](../23_Social_Connection_Tables_Index.md)
