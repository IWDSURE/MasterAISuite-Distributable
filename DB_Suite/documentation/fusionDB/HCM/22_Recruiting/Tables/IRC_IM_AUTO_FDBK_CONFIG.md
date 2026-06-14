# IRC_IM_AUTO_FDBK_CONFIG

This table stores the automatic interview feedback request action configuration.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimautofdbkconfig-26708.html#ircimautofdbkconfig-26708](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircimautofdbkconfig-26708.html#ircimautofdbkconfig-26708)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IM_AUTO_FDBK_CONFIG_PK | AUTO_FDBK_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_FDBK_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table.System generated. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Stores ID of the action usage at which the automatic interview feedback request is configured. Foreign key to IRC_LC_ACTION_USAGES_B table. |
| INCLUDE_RESUME_FLAG | VARCHAR2 | 1 |  | Yes | Stores flag configuration value for resume.Default value is'N'. |
| INCLUDE_COVER_LETTER_FLAG | VARCHAR2 | 1 |  | Yes | Stores flag configuration value for cover letter.Default value is'N'. |
| INCLUDE_ATTACHMNTS_FLAG | VARCHAR2 | 1 |  | Yes | Stores flag configuration value for attachments.Default value is'N'. |
| INCLUDE_INTERNAL_FLAG | VARCHAR2 | 1 |  | Yes | Stores flag configuration value for internal documents.Default value is'N'. |
| REQUEST_RATING_FLAG | VARCHAR2 | 1 |  | Yes | Stored flag configuration value for request rating |
| EXPIRATION_DELAY | NUMBER |  | 9 |  | Stores the number of days before feedback request will expire. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| COLLABORATOR_RESP_TYPE_LIST | VARCHAR2 | 1000 |  | Yes | List of selected collaborators based on the ORA_IRC_COLLABORATOR_RESP_TYPE lookup type, stored as comma separated values. |
| CODE | VARCHAR2 | 240 |  | Yes | Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IM_AUTO_FDBK_CONFIG_FK1 | Non Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_IM_AUTO_FDBK_CONFIG_PK | Unique | Default | AUTO_FDBK_CONFIG_ID |
| IRC_IM_AUTO_FDBK_CONFIG_U1 | Unique | Default | CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
