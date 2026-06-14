# IRC_CAMP_VANITY_CONFIG

Stores the vanity configuration details which is used for a campaign

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampvanityconfig-16174.html#irccampvanityconfig-16174](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampvanityconfig-16174.html#irccampvanityconfig-16174)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_VANITY_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| CONFIG_NAME | VARCHAR2 | 240 |  | Yes | Stores the sender information value. |
| SENDER_DISPLAY_NAME | VARCHAR2 | 240 |  | Yes | Stores the sender display name value. |
| SENDER_EMAIL | VARCHAR2 | 240 |  | Yes | Stores the sender email address value. |
| REPLY_TO_DISPLAY_NAME | VARCHAR2 | 240 |  |  | Stores the reply-to display name value. |
| REPLY_TO_EMAIL | VARCHAR2 | 240 |  |  | Stores the reply-to email address value. |
| OBJECT_STATUS | VARCHAR2 | 40 |  | Yes | Indicates the status of the object. (ORA_ACTIVE/ORA_DELETED) |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_VANITY_CONFIG_PK | Unique | Default | CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
