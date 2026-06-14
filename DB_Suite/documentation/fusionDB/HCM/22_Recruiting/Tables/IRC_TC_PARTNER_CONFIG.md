# IRC_TC_PARTNER_CONFIG

This table contains the partner configuration and activation data.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcpartnerconfig-17510.html#irctcpartnerconfig-17510](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcpartnerconfig-17510.html#irctcpartnerconfig-17510)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_PARTNER_CONFIG_PK | PARTNER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARTNER_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| INLINE_FLAG | VARCHAR2 | 1 |  | Yes | Stores the flag indicating whether the partner is supporting inline Tax Credits. |
| CSS_LINK_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether the WOTC link will be displayed on the candidate self service page for process triggers. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS table. |
| SHARE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether tax credits results can be shared across submissions. |
| SEND_PII_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether candidates pii data can be shared to patner. |
| VALIDITY_PERIOD | NUMBER |  | 4 |  | Previous tax credits results can be reused only if it is not older than this value. |
| CLIENT_ID | VARCHAR2 | 1024 |  |  | OAuth Client ID provided by the partner is stored in this column. |
| CLIENT_SECRET | VARCHAR2 | 1024 |  |  | OAuth Client Secret provided by the partner is stored in this column. |
| RESULTS_FLEX_CONTEXT_CODE | VARCHAR2 | 1024 |  |  | Store the Job Application EFF context code for additional Tax Credits Results |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_PARTNER_CONFIG_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_TC_PARTNER_CONFIG_PK | Unique | Default | PARTNER_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
