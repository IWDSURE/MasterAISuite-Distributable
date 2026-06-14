# IRC_CAMP_MSTEAMS_BOTS

Table to store the MS Teams BOT details. This data is also used to generate manifest file for customers.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsbots-17015.html#irccampmsteamsbots-17015](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampmsteamsbots-17015.html#irccampmsteamsbots-17015)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_MSTEAMS_BOTS_PK | CAMP_MSTEAMS_BOT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CAMP_MSTEAMS_BOT_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated |
| BOT_APP_ID | VARCHAR2 | 100 |  | Yes | Stores the Microsoft Bot’s Azure app registration ID (client ID). |
| BOT_SHORT_NAME | VARCHAR2 | 30 |  | Yes | Short display name for bot. To be used in manifest json file |
| BOT_FULL_NAME | VARCHAR2 | 255 |  | Yes | Full name (longer, for description context). To be used in manifest json file |
| BOT_SHORT_DESCRIPTION | VARCHAR2 | 80 |  | Yes | A brief description. To be used in manifest json file |
| BOT_FULL_DESCRIPTION | VARCHAR2 | 4000 |  | Yes | More detailed description. To be used in manifest json file |
| BOT_COLOR_ICON | BLOB |  |  | Yes | PNG, 192x192 pixels, for app display. To be used in manifest json file |
| BOT_OUTLINE_ICON | BLOB |  |  | Yes | PNG, 32x32 pixels, for Teams channels and lists. To be used in manifest json file |
| TENANT_ID | VARCHAR2 | 100 |  | Yes | Stores customer tenant guid of Microsoft azure |
| BOT_AUTHENTICATION_TYPE | VARCHAR2 | 30 |  | Yes | Whether it is certificate or client secrete (ORA_CLIENT_SECRET or ORA_CLIENT_CERTIFICATE) |
| BOT_CREDENTIAL_REF | VARCHAR2 | 255 |  | Yes | Reference to credential in Recruiting credential store |
| BOT_MANIFEST_UUID | VARCHAR2 | 100 |  | Yes | This will generate while saving the bot first time. To be used in manifest json file |
| BOT_STATUS | VARCHAR2 | 30 |  | Yes | Indicate the BOT deleted from FSM. Either ORA_ACTIVE or ORA_DELETE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_MSTEAMS_BOTS_PK | Unique | Default | CAMP_MSTEAMS_BOT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
