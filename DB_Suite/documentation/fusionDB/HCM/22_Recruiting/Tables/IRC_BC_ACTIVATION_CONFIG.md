# IRC_BC_ACTIVATION_CONFIG

Stores activation configuration for background check partners for recruiting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcactivationconfig-12462.html#ircbcactivationconfig-12462](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbcactivationconfig-12462.html#ircbcactivationconfig-12462)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BC_ACTIVATION_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| SHARE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether BC results can be shared across submissions |
| VALIDITY_PERIOD | NUMBER |  | 4 |  | Previous BC result can be reused only if it is not older than this value. |
| CAPTURE_PII_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether partner can be post  pii data  for submissions |
| SEND_PII_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether candidate pii data can be shared to patner. |
| PACKAGE_SELECTION_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether background check package selection allowed or not. |
| MULTIPLE_REQUEST_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether background check will be enabled for multiple requests |
| CSS_LINK_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether the backgroundCheck link will be displayed on the candidate self service page for process triggers. |
| OVERDUE_ALERT | NUMBER |  | 4 |  | Stores the number of days past request date when the BC results are due |
| CLIENT_ID | VARCHAR2 | 1000 |  |  | oAuth Client ID provided by the partner is stored in this column. |
| CLIENT_SECRET | VARCHAR2 | 1000 |  |  | oAuth Client Secret provided by the partner is stored in this column. |
| RESULTS_FLEX_CONTEXT_CODE | VARCHAR2 | 1024 |  |  | Store the Job Application EFF context code for additional Background check Results |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BC_ACTIVATION_CONFIG_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_BC_ACTIVATION_CONFIG_PK | Unique | Default | CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
