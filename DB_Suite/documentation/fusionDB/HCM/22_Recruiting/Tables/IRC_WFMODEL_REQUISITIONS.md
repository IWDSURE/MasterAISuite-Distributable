# IRC_WFMODEL_REQUISITIONS

Table for WFModel Requisition details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwfmodelrequisitions-14530.html#ircwfmodelrequisitions-14530](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwfmodelrequisitions-14530.html#ircwfmodelrequisitions-14530)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_WFMODEL_REQUISITIONS_PK | WF_MODEL_REQUISITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| WF_MODEL_REQUISITION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| WF_MODEL_ID | NUMBER |  | 18 | Yes | Stores the ID of the WF Model from which this model one has been created. Foreign key to HMO_MODEL_PLANS_B table. |
| SOURCE_REQUISITION_ID | NUMBER |  | 18 |  | Stores the ID of the requisition from which this model one has been created. Foreign key to IRC_REQUISITIONS_B table. |
| PHASE_ID | NUMBER |  | 18 |  | Foreign key to IRC_PHASES_B table. |
| STATE_ID | NUMBER |  | 18 |  | Foreign key to IRC_STATES_B table. |
| REQUISITION_LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  |  | Unique readable number for the Requisition. |
| RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Stores the type of Recruiting as a lookup code. The corresponding lookup type is ORA_IRC_RECRUITING_TYPE. |
| HIRING_MANAGER_ID | NUMBER |  | 18 |  | Stores the PERSON_ID of the hiring manager for this Requisition. Foreign key to PER_PERSONS table. |
| MANAGER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the hiring manager's assignment for this Requisition. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| RECRUITER_ID | NUMBER |  | 18 |  | Stores the PERSON_ID of the recruiter for this Requisition. Foreign key to PER_PERSONS table. |
| RECRUITER_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the ASSIGNMENT_ID of the recruiter's assignment for this Requisition. Foreign key to PER_ALL_ASSIGNMENTS_M table. |
| JUSTIFICATION_CODE | VARCHAR2 | 30 |  |  | Stores the Justification for this Requisition as a lookup code. The corresponding lookup type is ORA_IRC_REQ_JUSTIFICATION. |
| NUMBER_TO_HIRE | NUMBER |  | 9 |  | Stores the number of people to hire for this Requisition. |
| UNLIMITED_HIRE_FLAG | VARCHAR2 | 1 |  |  | Stores whether this Requisition can hire unlimited number of people. |
| COMMENTS | CLOB |  |  |  | Stores comments about this requisition. |
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 |  | Stores the Primary Location of this Requisition. Foreign key to IRC_GEO_HIER_NODES table. |
| TITLE | VARCHAR2 | 240 |  |  | Stores the Title for this Requisition. This is the title that is published to external/internal candidates. |
| MANAGER_TITLE | VARCHAR2 | 240 |  |  | Stores the Manager Title for this Requisition. This title is only used internally by the hiring manager, it is not meant to be published to external/internal candidates. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_WFMODEL_REQUISITIONS_FK1 | Non Unique | Default | PHASE_ID |
| IRC_WFMODEL_REQUISITIONS_FK2 | Non Unique | Default | STATE_ID |
| IRC_WFMODEL_REQUISITIONS_FK3 | Non Unique | Default | SOURCE_REQUISITION_ID |
| IRC_WFMODEL_REQUISITIONS_FK4 | Non Unique | Default | GEOGRAPHY_NODE_ID |
| IRC_WFMODEL_REQUISITIONS_FK5 | Non Unique | Default | HIRING_MANAGER_ID |
| IRC_WFMODEL_REQUISITIONS_FK6 | Non Unique | Default | RECRUITER_ID |
| IRC_WFMODEL_REQUISITIONS_FK7 | Non Unique | Default | MANAGER_ASSIGNMENT_ID |
| IRC_WFMODEL_REQUISITIONS_FK8 | Non Unique | Default | RECRUITER_ASSIGNMENT_ID |
| IRC_WFMODEL_REQUISITIONS_N1 | Non Unique | Default | WF_MODEL_ID |
| IRC_WFMODEL_REQUISITIONS_PK | Unique | Default | WF_MODEL_REQUISITION_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
