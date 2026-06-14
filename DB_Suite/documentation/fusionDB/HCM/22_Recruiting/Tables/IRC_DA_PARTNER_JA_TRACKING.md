# IRC_DA_PARTNER_JA_TRACKING

This table contains the partner tracking id provided by partners for third party job site direct apply.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnerjatracking-15404.html#ircdapartnerjatracking-15404](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircdapartnerjatracking-15404.html#ircdapartnerjatracking-15404)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_DA_PARTNER_JA_TRACKING_PK | DA_PARTNER_JA_TRACKING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DA_PARTNER_JA_TRACKING_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PARTNER_TRACKING_ID | VARCHAR2 | 255 |  |  | Tracking id provided by the partner to track direct apply submissions. |
| SUBMISSION_ID | NUMBER |  | 18 | Yes | Foreign key reference to irc_submissions. |
| PARTNER_ID | NUMBER |  | 18 | Yes | Foreign key reference to irc_tp_partners. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_DA_PARTNER_JA_TRACKING_FK1 | Non Unique | Default | SUBMISSION_ID |
| IRC_DA_PARTNER_JA_TRACKING_FK2 | Non Unique | Default | PARTNER_ID |
| IRC_DA_PARTNER_JA_TRACKING_N1 | Non Unique | Default | PARTNER_TRACKING_ID |
| IRC_DA_PARTNER_JA_TRACKING_PK | Unique | Default | DA_PARTNER_JA_TRACKING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
