# BEN_ASGN_PTNL_LER_

BEN_ASGN_PTNL_LER contains information related to person self reported life event.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benasgnptnller-3233.html#benasgnptnller-3233](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benasgnptnller-3233.html#benasgnptnller-3233)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ASGN_PTNL_LER_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASGN_PTNL_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASGN_PTNL_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PERSON_ID | NUMBER |  | 18 |  | This column holds Foreign Key to PER_PEOPLE_F. |
| LER_ID | NUMBER |  | 18 |  | This column holds Foreign Key to BEN_LER_F. |
| OCCURRED_DATE | DATE |  |  |  | This column holds life event occurred date as given by the employee. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_BENEFIT_RELATIONS_F. |
| SUBMITTED_DATE | DATE |  |  |  | This column holds the date when the self-assigned life event was submitted. |
| STATUS_CD | VARCHAR2 | 30 |  |  | This column holds life event status. |
| RESUBMITTED_DATE | DATE |  |  |  | This column holds the date when the self-assigned life event was resubmitted for approval by the employee as a response to request for more information from admin user. |
| APPROVED_DATE | DATE |  |  |  | This column holds the date when the self-assigned life event was approved by admin user. |
| REJECTED_DATE | DATE |  |  |  | This column holds the date when the self-assigned life event was rejected by admin user. |
| INFO_REQD_DATE | DATE |  |  |  | This column holds the date when the self-assigned life event was returned recently by admin to the employee seeking additional information. |
| USER_COMMENTS | VARCHAR2 | 4000 |  |  | Comments provided by employee at the time of submitting the life event and also when providing additional information requested by admin during resubmission. |
| ADMIN_COMMENTS | VARCHAR2 | 4000 |  |  | Comments provided by admin user at the time of approving, rejecting or requesting additional information from employee. |
| ACTIONED_BY | VARCHAR2 | 2000 |  |  | This column holds the name of admin user who recently actioned on the submitted life event such as approved, rejected or more info requested etc. |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | This column holds foreign Key to HR_DOCUMENT_TYPES_F. |
| SYSTEM_DOCUMENT_TYPE | VARCHAR2 | 120 |  |  | This column holds the system document type as set up in the life event approval rule for the life event submitted by employee. |
| DOR_ID | NUMBER |  | 18 |  | The ID (Foreign key) of the Document of Record uploaded as supporting document for the submitted life event. |
| PTNL_LER_FOR_PER_ID | NUMBER |  | 18 |  | This column holds foreign Key to BEN_PTNL_LER_FOR_PER. |
| SOURCE | VARCHAR2 | 30 |  |  | Whether the record was created from UI or other means. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_6 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_7 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_8 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_9 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_10 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ASGN_PTNL_LER_N1_ | Non Unique | Default | ASGN_PTNL_LER_ID, LAST_UPDATE_DATE |
| BEN_ASGN_PTNL_LER_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, ASGN_PTNL_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
