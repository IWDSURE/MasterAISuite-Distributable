# BEN_PER_ACTY_LOG

BEN_PER_ACTY_LOG contains information related to person activity on self service enrollment page.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperactylog-10465.html#benperactylog-10465](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperactylog-10465.html#benperactylog-10465)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ACTY_LOG_ID | NUMBER |  |  | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  |  | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| PERSON_ID | NUMBER |  |  | Yes | This column holds Foreign Key to PER_PEOPLE_F. |
| ACTY_DATE_TIME | TIMESTAMP |  |  | Yes | This column holds date and time on which activity is performed |
| ACTY_TYPE | VARCHAR2 | 64 |  |  | This column holds the type of activity performed |
| ACTY_FLOW | VARCHAR2 | 240 |  | Yes | This column holds the flow or page or ess job name where the activity is performed |
| ACTY_REGION | VARCHAR2 | 240 |  | Yes | This column holds the region name in a page where the activity is performed |
| OBJ_NAME | VARCHAR2 | 240 |  |  | This column holds the name of the object on which activity is performed |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| OBJ_ID | NUMBER |  |  |  | This column holds the key of the object on which activity is performed |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_ACTY_LOG_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID, ACTY_FLOW |
| BEN_PER_ACTY_LOG_PK | Unique | FUSION_TS_TX_DATA | PER_ACTY_LOG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
