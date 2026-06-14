# HRA_TMPL_DEFNS_B

This table stores the structure and process for creating performance evaluations that contains the rules and configuration for the various business processes and participants that will be be part of the evaluation e.g. Annual Review.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmpldefnsb-7368.html#hratmpldefnsb-7368](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hratmpldefnsb-7368.html#hratmpldefnsb-7368)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_TMPL_DEFNS_B_PK | TEMPLATE_DEFN_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Flexfield-mapping | Status |
|---|---|---|---|---|---|---|---|
| TEMPLATE_DEFN_ID | NUMBER |  | 18 | Yes | Primary key of Template Definition. |  |  |
| TEMPLATE_TYPE_CODE | VARCHAR2 | 30 |  |  | Identifies template type of the performance document. |  |  |
| USE_CALC_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates if section rating needs to be set based on calculated value. |  |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS |  |  |
| SET_ID | NUMBER |  | 18 | Yes | Identifies a set of reference data shared across business units and other entities. Also known as Reference Data Sets, they are used to filter reference data in transactional UIs. |  |  |
| DOC_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key of Document Type. |  |  |
| PROCESS_FLOW_ID | NUMBER |  | 18 |  | Indicates the Process Flow definiton that is used in this template definiton. |  |  |
| DATE_FROM | DATE |  |  | Yes | This is the date when the performance template is valid from. |  |  |
| DATE_TO | DATE |  |  |  | This is the last day that the performance template is valid. |  |  |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Status of the Performance Template. |  |  |
| CALCULATE_RATINGS_FLAG | VARCHAR2 | 30 |  |  | Indicates that the system should calculate the ratings for a section or a document. |  |  |
| ROUNDING_RULE_CODE | VARCHAR2 | 30 |  |  | Indicates the rounding rule that will be used for ratings that are calculated by the system. Valid values are Standard, Up and Down. |  |  |
| DECIMAL_PLACES | NUMBER |  | 18 |  | Indicates the number of decimal places for calculated ratings. |  |  |
| MAPPING_METHOD_CODE | VARCHAR2 | 30 |  |  | This applies to the Overall Rating section, where the system must choose an overall rating from the rating model, based on a calculated rating. |  |  |
| SHOW_PARTICIPANT_NAMES | VARCHAR2 | 30 |  |  | Indicates whether to display participant names to worker. |  |  |
| SELECT_MGR_ALLOWED_FLAG | VARCHAR2 | 30 |  |  | Indicates whether worker can select manager when generating document. |  |  |
| STAR_RATING_ENABLED_FLAG | VARCHAR2 | 30 |  | Yes | Indicates whether to use star rating model or not. |  |  |
| SET_ROLE_MINIMUMS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to set the minimum number for each role and also the total number for the evaluation. |  |  |
| SET_ROLE_MAXIMUMS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to set the maximum number for each role and also the total number for the evaluation. |  |  |
| TOTAL_MIN_PARTICIPANTS | NUMBER |  | 18 |  | Stores the total minimum number of participants required in the document |  |  |
| TOTAL_MAX_PARTICIPANTS | NUMBER |  | 18 |  | Stores the total maximum number of participants required in the document |  |  |
| ENFORCE_MIN_PCPNS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to enforce minimum number of participants allowed in the document. |  |  |
| USE_WRK_CONNECTIONS_FLAG | VARCHAR2 | 30 |  |  | Stores whether to show  the search by workers' network connections in the social product when adding participants |  |  |
| WRK_SEE_MGR_PCPN_FLAG | VARCHAR2 | 30 |  |  | Stores whether worker can see the participants added by manager |  |  |
| PCPN_FEEDBACK_REQ_FLAG | VARCHAR2 | 30 |  |  | Stores whether the participant feedback is required |  |  |
| PCPN_DECLINE_OPTION_FLAG | VARCHAR2 | 30 |  |  | Stores whether to give the participant the option whether to Accept/Decline the feedback request |  |  |
| AUTO_POPULATE_MM_FLAG | VARCHAR2 | 30 |  |  | Indicate matrix managers are automatically populated as participants when performance document is created. |  |  |
| SEND_REQUEST_TO_MM_FLAG | VARCHAR2 | 30 |  |  | Indicates request will be sent to matrix manager particpants when performance document is created, which automatically gives them access to the document. |  |  |
| DEFAULT_MATRIX_PCPN_ROLE_ID | NUMBER |  | 18 |  | Indicates default matrix role to use when automatically populating matrix managers as participants. |  |  |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| ATTRIBUTE_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. | Performance Template Definition (HRA_TMPL_DEFNS_B) |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |  |
| DIGITAL_SIGNATURE_FLAG | VARCHAR2 | 30 |  |  | Display digital signature flag. |  |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |  |
| KUDOS_REGION_FLAG | VARCHAR2 | 30 |  |  | Display kudos region flag. |  |  |
| SHOW_WKR_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Calculated Ratings should be visible to Worker. |  |  |
| SHOW_MGR_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether the Calculated Ratings should be visible to Manager. |  |  |
| SHOW_MM_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether calculated ratings should be visible to matrix managers. |  |  |
| SHOW_PCPN_CALC_RATING_FLAG | VARCHAR2 | 30 |  |  | Indicates whether calculated ratings should be visible to participants. |  |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  | Obsolete |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | Stores request id of the last ESS job submitted for this performance template |  |  |
| ESS_REQUEST_STATUS | VARCHAR2 | 30 |  |  | Stores request status of the last ESS job submitted for this performance template |  |  |
| SHOW_CHECK_IN_REGION_FLAG | VARCHAR2 | 30 |  |  | Indicates if the CheckIn region should display in performance document. |  |  |
| SHOW_FEEDBACK_REQ_REGION_FLAG | VARCHAR2 | 30 |  |  | indicates if the feedback request region should display in the performance document. |  |  |
| ENABLE_SYNC_FLAG | VARCHAR2 | 30 |  |  | Indicates if the performance template is configured to use synchronized goals |  |  |
| ALLOW_WKR_SELECT_MM_ROLE_FLAG | VARCHAR2 | 30 |  |  | Allow worker to select matrix manager role. |  |  |
| ALLOW_MGR_SELECT_MM_ROLE_FLAG | VARCHAR2 | 30 |  |  | Allow manager to select matrix manager role. |  |  |
| ALL_MM_MGR_TYPE_FLAG | VARCHAR2 | 30 |  |  | Specify all manager types for auto population as participants. |  |  |
| MM_MANAGER_TYPES | VARCHAR2 | 4000 |  |  | Specify manager types for auto population as participants. |  |  |
| MIN_LENGTH_COMMENTS | NUMBER |  |  |  | Minimum Length of comments |  |  |
| MAX_LENGTH_COMMENTS | NUMBER |  |  |  | Maximum Length of comments |  |  |
| SHOW_CHECK_IN_SUMMARY_FLAG | VARCHAR2 | 30 |  |  | Indicates if the CheckIn summary should display in performance document. |  |  |
| SHOW_FEEDBACK_REQ_SUMMARY_FLAG | VARCHAR2 | 30 |  |  | Indicates if the feedback request summary should display in the performance document. |  |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_TMPL_DEFNS_B_N1 | Non Unique | Default | SET_ID |
| HRA_TMPL_DEFNS_B_N2 | Non Unique | Default | DOC_TYPE_ID |
| HRA_TMPL_DEFNS_B_N3 | Non Unique | Default | PROCESS_FLOW_ID |
| HRA_TMPL_DEFNS_B_N4 | Non Unique | Default | LAST_UPDATE_DATE |
| HRA_TMPL_DEFNS_B_PK | Unique | Default | TEMPLATE_DEFN_ID, BUSINESS_GROUP_ID |
| HRA_TMPL_DEFNS_B_UK1 | Unique | Default | TEMPLATE_DEFN_ID, SET_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
