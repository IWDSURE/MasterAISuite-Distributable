# PER_PORTRAIT_MESSAGES_B

This table stores administrator messages that should appear on the  Portrait Pages.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitmessagesb-25543.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitmessagesb-25543.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PORTRAIT_MESSAGES_B_PK | PORTRAIT_MESSAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PORTRAIT_MESSAGE_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SHOW_CAL_EVT_CATEGORY | VARCHAR2 | 30 |  |  | Calendar Event Category which should be included in portrait messages. |
| PRIORITY | NUMBER |  | 18 |  | Priority of the portrait message. |
| MESSAGE_TYPE | VARCHAR2 | 30 |  |  | Type of the portrait message like STATUS , BROADCAST etc. |
| TIME_FROM | TIMESTAMP |  |  |  | Date and Time on Server that message will start being shown |
| TIME_TO | TIMESTAMP |  |  |  | Date and Time on server that message will stop being shown |
| TARGET_PERSON_ID | NUMBER |  | 18 |  | Optionally specify a Person, such that the message appears when the user views the portrait of a person. |
| TARGET_DEPARTMENT_ID | NUMBER |  | 18 |  | Optionally specify a Department, such that the message appears when the user views the portrait of a person who is a member of that Department. |
| TARGET_LOCATION_ID | NUMBER |  | 18 |  | Optionally specify a Location, such that the message appears when the user views the portrait of a person who is a member of that Location. |
| TARGET_ORGANIZATION_TREE_CODE | VARCHAR2 | 32 |  |  | Optionally specify an Organization Hierarchy , such that the message appears when the user views the portrait of a person who is a member of that Organization Hierarchy. |
| TARGET_ORGANIZATION_TOP_NODE | NUMBER |  | 18 |  | Optionally specify the Organization in the Organization hierarchy that is to be considered the top for the message. Portraits of people in organizations above this do not show this message. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PORTRAIT_MESSAGES_B_N1 | Non Unique | Default | TARGET_PERSON_ID |
| PER_PORTRAIT_MESSAGES_B_PK | Unique | Default | PORTRAIT_MESSAGE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
