# IRC_DA_PARTNER_CONFIG

This table contains the partner configuration and activation data for third party job site direct apply.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnerconfig-31223.html#ircdapartnerconfig-31223](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnerconfig-31223.html#ircdapartnerconfig-31223)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DA_PARTNER_CONFIG_PK | PARTNER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARTNER_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PARTNER_TYPE | VARCHAR2 | 255 |  | Yes | Partner type can be DIRECT_APPLY / TALENT_NETWORK / LINKEDIN |
| CLIENT_ID | VARCHAR2 | 1024 |  |  | oAuth Client ID provided by the partner is stored in this column. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key reference to irc_tp_partner_provisngs |
| DISPLAY_FLAG | VARCHAR2 | 1 |  | Yes | This flag value determines that the partner needs to be displayed in the FSM UI |
| SOURCE_MEDIUM_CODE | VARCHAR2 | 255 |  | Yes | Source Medium Code used as a reference.  The corresponding lookup type is ORA_IRC_SOURCE_TRACKING_MEDIUM. |
| SOURCE_NAME | VARCHAR2 | 255 |  | Yes | Source Name used as a reference |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DA_PARTNER_CONFIG_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_DA_PARTNER_CONFIG_PK | Unique | Default | PARTNER_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
