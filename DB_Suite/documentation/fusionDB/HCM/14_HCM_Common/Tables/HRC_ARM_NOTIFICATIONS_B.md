# HRC_ARM_NOTIFICATIONS_B

Approval model Table: This holds notification details like mode of delivery, recipient to receive the notification pertaining to a specific process.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmnotificationsb-18544.html#hrcarmnotificationsb-18544](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcarmnotificationsb-18544.html#hrcarmnotificationsb-18544)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_ARM_NOTIFICATIONS_B_PK | NOTIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| NOTIFICATION_ID | NUMBER |  | 18 | Yes | Primary Key and unique identifier |
| PROCESS_ID | NUMBER |  | 18 | Yes | Identify the process  to which the Notification belongs.  Foreign key to PER_APPROVAL_PROCESS |
| TASK_STATUS | VARCHAR2 | 32 |  | Yes | The status of task at which notification has to be sent |
| RECIPIENT_TYPE | VARCHAR2 | 64 |  | Yes | The recipient to be notified |
| USER_NAME | VARCHAR2 | 80 |  |  | The user name if recipient type is USER |
| ENABLED | VARCHAR2 | 4 |  |  | Flag to check if the notification is enabled |
| DELIVERY_MODE | VARCHAR2 | 32 |  |  | The mode of delivery for the notification |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identify the ENTERPRISE  to which the composite belongs.  
Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_ARM_NOTIFICATIONS_B_N1 | Non Unique | Default | LAST_UPDATE_DATE |
| HRC_ARM_NOTIFICATIONS_B_PK | Unique | Default | NOTIFICATION_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
