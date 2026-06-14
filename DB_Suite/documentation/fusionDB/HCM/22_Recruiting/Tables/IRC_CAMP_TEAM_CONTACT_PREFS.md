# IRC_CAMP_TEAM_CONTACT_PREFS

Stores the contact order preferences in Communication Teams.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamcontactprefs-16166.html#irccampteamcontactprefs-16166](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampteamcontactprefs-16166.html#irccampteamcontactprefs-16166)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_TEAM_CONTACT_PREF_PK | CONTACT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTACT_PREFERENCE_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| TEAM_ID | NUMBER |  | 18 | Yes | Stores the ID of communication Team for which the contact order preference is added.Foreign Key to irc_camp_comm_teams_b table |
| CONTACT_PREFERENCE_TYPE_CODE | VARCHAR2 | 40 |  | Yes | Stores the Lookup code from Lookup Type "Email_Type/Phone_Type", added to the contact order preference list to figure out which type of contact is stored, ex: W1 or H1. |
| CONTACT_PREFERENCE_ORDER | NUMBER |  | 9 | Yes | Stores the priority of the CONTACT_PREFERENCE_TYPE_CODE added to the contact order preference list. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the lookupCode (ORA_EMAIL/ORA_SMS) from lookupType "ORA_HCO_CHANNEL_TYPE" to determine which channel is selected in contact order preference list. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_TEAM_CONTACT_PREF_FK1 | Non Unique | Default | TEAM_ID |
| IRC_CAMP_TEAM_CONTACT_PREF_PK | Unique | Default | CONTACT_PREFERENCE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
