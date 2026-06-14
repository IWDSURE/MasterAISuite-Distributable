# IRC_DA_PARTNER_NOTIF_CONFIG

This table contains the partner configuration for third party job site direct apply notification.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnernotifconfig-4289.html#ircdapartnernotifconfig-4289](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnernotifconfig-4289.html#ircdapartnernotifconfig-4289)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DA_PARTNER_NOTIF_CONF_PK | DA_NOTIF_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DA_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for the table. System generated. |
| STEP_ACTION_USAGE_ID | NUMBER |  | 18 | Yes | Foreign key IRC_LC_ACTION_USAGES_B table. (Life cycle action context) |
| DA_JA_PARTNER_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Status code of the direct apply partner reference status.  They types of status code is coming from hcm_lookups with type 'ORA_IRC_DA_JA_PARTNER_STATUS' |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DA_PARTNER_NOTIF_CONF_FK1 | Non Unique | Default | STEP_ACTION_USAGE_ID |
| IRC_DA_PARTNER_NOTIF_CONF_PK | Unique | Default | DA_NOTIF_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
