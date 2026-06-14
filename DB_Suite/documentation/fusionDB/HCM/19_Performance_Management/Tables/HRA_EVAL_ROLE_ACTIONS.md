# HRA_EVAL_ROLE_ACTIONS

This table stores the roles and the actions each role can perform on a performance document.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalroleactions-21741.html#hraevalroleactions-21741](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraevalroleactions-21741.html#hraevalroleactions-21741)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_EVAL_ROLE_ACTIONS_PK | EVAL_ROLE_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVAL_ROLE_ACTION_ID | NUMBER |  | 18 | Yes | Primark key of the Evaluation Role Actions. |
| ITEM_RATINGS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | ITEM_RATINGS_REQUIRED_CODE |
| ITEM_COMMENTS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | ITEM_COMMENTS_REQUIRED_CODE |
| SECTION_RATINGS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | SECTION_RATINGS_REQUIRED_CODE |
| SECTION_COMMENTS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | SECTION_COMMENTS_REQUIRED_CODE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |
| EVALUATION_ID | NUMBER |  | 18 |  | Primary key of Evaluation. |
| EVAL_ROLE_ID | NUMBER |  | 18 |  | Foreign key to HRA_EVAL_ROLES |
| EVAL_SECTION_ID | NUMBER |  | 18 |  | The identifier for the section (not shown in the UI) |
| SHARE_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will display the ratings of the specified role to the worker in the final performance document. |
| SHARE_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will display the comments of the specified role to the worker in the final performance document. |
| UPDATE_PROFILE_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will publish content items from the performance document, to the person profile, when the document status changes to Completed. |
| PERSON_PROFILE_TYPE_ID | NUMBER |  | 18 |  | Indicates the type of person profile in Profile Management |
| QUALIFIER_ID | NUMBER |  | 18 |  | Indicates the qualifier ID for the person profile in Profile Management |
| VIEW_PCPN_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant questionnaire can be viewed by the role |
| VIEW_PCPN_NAME_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant name can be viewed by the role |
| VIEW_PCPN_ROLE_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant role name can be seen or not by the selected role. |
| PCPN_ENTER_WRK_CMTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the participant role can enter the comments for the worker. |
| VIEW_MGR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the particular role can see the manager questionnaire |
| VIEW_WRK_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the particular role can see the worker questionnaire |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CHILD_ITEM_COMMENTS_REQ_CODE | VARCHAR2 | 30 |  |  | Indicates whether to show competency type comments to specified role or not. |
| PROVIDE_ITEM_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item ratings can be provided by the role. |
| PROVIDE_ITEM_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item comments can be provided by the role. |
| PROVIDE_SECTION_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether section ratings can be provided by the role. |
| PROVIDE_SECTION_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether section comments can be provided by the role. |
| VIEW_WKR_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view worker's questionnaire score. |
| VIEW_MGR_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view manager's questionnaire score. |
| VIEW_PCPN_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view participant's questionnaire score. |
| VIEW_OWN_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view its own questionnaire score. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_EVAL_ROLE_ACTIONS_N1 | Non Unique | Default | EVALUATION_ID |
| HRA_EVAL_ROLE_ACTIONS_N2 | Non Unique | Default | EVAL_ROLE_ID |
| HRA_EVAL_ROLE_ACTIONS_N3 | Non Unique | Default | EVAL_SECTION_ID |
| HRA_EVAL_ROLE_ACTIONS_PK | Unique | Default | EVAL_ROLE_ACTION_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
