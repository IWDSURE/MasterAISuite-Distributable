# IRC_JD_ACTIVATION_CONFIG

Stores activation configuration for job distribution partners for recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjdactivationconfig-31006.html#ircjdactivationconfig-31006](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjdactivationconfig-31006.html#ircjdactivationconfig-31006)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_JD_ACTIVATION_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CLIENT_ID | VARCHAR2 | 1024 |  |  | oAuth Client ID provided by the partner is stored in this column. |
| CLIENT_SECRET | VARCHAR2 | 1024 |  |  | oAuth Client Secret provided by the partner is stored in this column. Data stored in this column is encrypted. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_JD_ACTIVATION_CONFIG_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_JD_ACTIVATION_CONFIG_PK | Unique | Default | CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
