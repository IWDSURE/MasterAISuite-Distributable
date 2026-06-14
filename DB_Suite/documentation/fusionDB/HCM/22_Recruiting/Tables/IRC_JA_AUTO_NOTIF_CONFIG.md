# IRC_JA_AUTO_NOTIF_CONFIG

This table is used to store the automated hiring team notifications , agents and collaborators template.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjaautonotifconfig-6933.html#ircjaautonotifconfig-6933](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjaautonotifconfig-6933.html#ircjaautonotifconfig-6933)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JA_AUTO_NOTIF_CONFIG_PK | JA_AUTO_NOTIF_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JA_AUTO_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | Primary Key for the Table. System generated. |
| JA_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | Foreign key IRC_JA_NOTIF_CONFIG table. |
| RECEIVER_TYPE | VARCHAR2 | 64 |  | Yes | This captures the information whether the receiver is HM type / Recruiter / Collaborator or Agent type. |
| RECEIVER_CODE | VARCHAR2 | 64 |  |  | Captures any code of the receiver if exists. For eg - when we select collaborator and its template , we would have to store the collaborator code. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Email template that is to be used for sending notifications for particular receiver. Foreign key IRC_DESCRIPTIONS_B.DESCRIPTION_ID |
| RECEIVER_NOTIF_DELAY | NUMBER |  | 18 |  | Stores the delay time in hours before sending notification to the receiver. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JA_AUTO_NOTIF_CONFIG_FK1 | Non Unique | Default | JA_NOTIF_CONFIG_ID |
| IRC_JA_AUTO_NOTIF_CONFIG_FK2 | Non Unique | Default | TEMPLATE_ID |
| IRC_JA_AUTO_NOTIF_CONFIG_PK | Unique | Default | JA_AUTO_NOTIF_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
