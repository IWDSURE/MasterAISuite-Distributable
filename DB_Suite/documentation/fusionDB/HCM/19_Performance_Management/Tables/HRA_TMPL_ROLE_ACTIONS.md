# HRA_TMPL_ROLE_ACTIONS

This table stores the actions that can be performed by each role

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplroleactions-9177.html#hratmplroleactions-9177](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmplroleactions-9177.html#hratmplroleactions-9177)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_ROLE_ACTIONS_PK | TMPL_ROLE_ACTION_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| TMPL_ROLE_ACTION_ID | NUMBER |  | 18 | Yes | Primary key of the Template Role Actions. |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |
| ITEM_RATINGS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | ITEM_RATINGS_REQUIRED_CODE |  |
| ITEM_COMMENTS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | ITEM_COMMENTS_REQUIRED_CODE |  |
| SECTION_RATINGS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | SECTION_RATINGS_REQUIRED_CODE |  |
| SECTION_COMMENTS_REQUIRED_CODE | VARCHAR2 | 30 |  |  | SECTION_COMMENTS_REQUIRED_CODE |  |
| TMPL_ROLE_ID | NUMBER |  | 18 | Yes | Foreign key of Template Roles |  |
| SECTION_ID | NUMBER |  | 18 | Yes | Foreign key of Template Sections. |  |
| SHARE_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will display the ratings of the specified role to the worker in the final performance document. |  |
| SHARE_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will display the comments of the specified role to the worker in the final performance document. |  |
| UPDATE_PROFILE_FLAG | VARCHAR2 | 30 |  |  | Indicates the system will publish content items from the performance document, to the person profile, when the document status changes to Completed. |  |
| PERSON_PROFILE_TYPE_ID | NUMBER |  | 18 |  | This is the profile type that will receive the published content. |  |
| QUALIFIER_SET_ID | NUMBER |  | 18 |  | This is the set for the instance qualifier object. |  |
| QUALIFIER_ID | NUMBER |  | 18 |  | This is the instance qualifier or evaluation source type for the data that will be published to the profile. |  |
| VIEW_PCPN_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant questionnaire can be viewed by the role |  |
| VIEW_PCPN_NAME_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant name can be viewed by the role |  |
| VIEW_PCPN_ROLE_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant role can be seen or not. |  |
| PCPN_ENTER_WRK_CMTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the participant role can enter the worker comments. |  |
| VIEW_MGR_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the particular role can see the manager questionnaire |  |
| VIEW_WRK_QSTNR_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the particular role can see the worker questionnaire |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| CHILD_ITEM_COMMENTS_REQ_CODE | VARCHAR2 | 30 |  |  | Indicates whether to show competency type comments to specified role or not. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| PROVIDE_ITEM_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item ratings can be provided by the role. |  |
| PROVIDE_ITEM_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether item comments can be provided by the role. |  |
| PROVIDE_SECTION_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether section ratings can be provided by the role. |  |
| PROVIDE_SECTION_COMMENTS_FLAG | VARCHAR2 | 30 |  |  | Indicates whether section comments can be provided by the role. |  |
| ALLOW_NOT_RATED_ITEM_FLAG | VARCHAR2 | 30 |  |  | Allow user role to mark the item as not rated. |  |
| VIEW_WKR_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view worker's questionnaire score. |  |
| VIEW_MGR_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view manager's questionnaire score. |  |
| VIEW_PCPN_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view participant's questionnaire score. |  |
| VIEW_OWN_QSTNR_SCORES_FLAG | VARCHAR2 | 30 |  |  | Store whether the role can view its own questionnaire score. |  |
| SHOW_ITEM_COMMENTS_AI_FLAG | VARCHAR2 | 30 |  |  | COLUMN1 |  |
| SHOW_SECTION_COMMENTS_AI_FLAG | VARCHAR2 | 30 |  |  | COLUMN1 |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_ROLE_ACTIONS_N1 | Non Unique | Default | TMPL_ROLE_ID |
| HRA_TMPL_ROLE_ACTIONS_N2 | Non Unique | Default | SECTION_ID |
| HRA_TMPL_ROLE_ACTIONS_PK | Unique | Default | TMPL_ROLE_ACTION_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
