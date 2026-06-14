# HMO_MODEL_PLANS_B

The main table to store the model plan.

## Details

**Schema:** FUSION

**Object owner:** HMO

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplansb-20203.html#hmomodelplansb-20203](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hmomodelplansb-20203.html#hmomodelplansb-20203)

## Primary Key

| Name | Columns |
|------|----------|
| HMO_MODEL_PLANS_B_PK | MODEL_PLAN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_PLAN_ID | NUMBER |  | 18 | Yes | Model Plan Id . This is the primary ley |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Enterprise Id of the system.This is the foreign key to PER_ENTERPRISES. |
| EFFECTIVE_DATE | DATE |  |  | Yes | Effective Date of the model plan. |
| MODEL_PLAN_STATUS | VARCHAR2 | 30 |  | Yes | Status of the  model plan . The valid values are  DRAFT,PENDING, APPROVED, REJECTED. |
| MODEL_PLAN_TYPE | VARCHAR2 | 30 |  | Yes | Type of the Model Plan Top Manager like Position or Line Manager |
| ACTION_ID | NUMBER |  | 18 |  | Action Id. This is the foreign key to PER_ACTIONS_VL. |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Action Reason Id. This is the foreign key to PER_ACTION_REASONS_VL |
| AUTHOR_PERSON_ID | NUMBER |  | 18 | Yes | Author's Person Id of the model plan. |
| TOP_MANAGER_ID | NUMBER |  | 18 | Yes | Top Manager Person Id  whose hierarchy is being modeled. |
| TOP_MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 | Yes | Top Manager  Assignment Id  whose hierarchy is being displayed. |
| TOP_MANAGER_TYPE | VARCHAR2 | 30 |  | Yes | Type of the Manager i.e LINE_MANAGER , RESOURCE_MANAGER , PROJECT_MANAGER |
| ACCESS_TO_TOP_MANAGER | VARCHAR2 | 30 |  | Yes | The flag indicates whether the top manager can access the model. The valid values are Y/N and the default value is 'Y'. |
| MODEL_LOADER_BATCH_ID | NUMBER |  | 18 |  | Primary key of the Batch loader process |
| LAST_SYNC_DATE | TIMESTAMP |  |  |  | Last Sync Date indicates the date of last synchronization to the Fusion System source |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HMO_MODEL_PLANS_B_N1 | Non Unique | Default | ENTERPRISE_ID, AUTHOR_PERSON_ID |
| HMO_MODEL_PLANS_B_PK | Unique | Default | MODEL_PLAN_ID |

---

[← Back to Index](../32_Workforce_Modeling_Tables_Index.md)
