# WLF_MESSAGES

This table will be used to store all error and warning messages that are thrown during validation of the state of the learning item.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** wlf_messages

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmessages-14733.html#wlfmessages-14733](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfmessages-14733.html#wlfmessages-14733)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_MESSAGES_PK | MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MESSAGE_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| MESSAGE_CODE | VARCHAR2 | 400 |  | Yes | The fusion message name/key which can be used to lookup the appropriate translated value of the message |
| MESSAGE_CATEGORY | VARCHAR2 | 30 |  | Yes | Category of the message such as whether it is related to validation, transcoding, integration, etc. |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | The unique id of the source object to which this message applies |
| SOURCE_OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | The type of the source object that this message is applicable to |
| VALIDATION_STATUS | VARCHAR2 | 30 |  |  | The status of the validation - ORA_ACTIVE / ORA_RESOLVED / ORA_IGNORE |
| SEVERITY | VARCHAR2 | 30 |  |  | The severity of the message - 1 for Error, 2 for Warning, 3 for Info |
| VISIBILITY | VARCHAR2 | 30 |  |  | The visibility of the message - ORA_SHOW / ORA_HIDE |
| TRACE_ID | VARCHAR2 | 400 |  |  | An internal identifier that can be used by Support/Dev team to trace the source/cause of the error |
| LOG | CLOB |  |  |  | Text to provide more information about the error |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_MESSAGES_N1 | Non Unique | Default | SOURCE_OBJECT_ID, SOURCE_OBJECT_TYPE |
| WLF_MESSAGES_U1 | Unique | Default | MESSAGE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
