# IRC_ASMT_PARTNER_CONFIG

This table contains the partner configuration and activation data.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtpartnerconfig-14128.html#ircasmtpartnerconfig-14128](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircasmtpartnerconfig-14128.html#ircasmtpartnerconfig-14128)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_ASMT_PARTNER_CONFIG_PK | PARTNER_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PARTNER_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS table. |
| SHARE_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether assessment results can be shared across submissions. |
| VALIDITY_PERIOD | NUMBER |  | 4 |  | Previous assessment results can be reused only if it is not older than this value. |
| MULTI_PHASE_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if the partner is supporting multi-phase assessments. |
| INLINE_FLAG | VARCHAR2 | 1 |  |  | Stores whether the partner supports inline assesments. |
| CSS_LINK_FLAG | VARCHAR2 | 1 |  |  | Stores the flag indicating whether the assessment link will be displayed on the candidate self service page for process triggers. |
| PHASE_COUNT | NUMBER |  | 4 |  | Number of phases supported by the partner. |
| CLIENT_ID | VARCHAR2 | 1024 |  |  | oAuth Client ID provided by the partner is stored in this column. |
| CLIENT_SECRET | VARCHAR2 | 1024 |  |  | oAuth Client Secret provided by the partner is stored in this column. |
| RESULTS_FLEX_CONTEXT_CODE | VARCHAR2 | 1024 |  |  | Store the Job Application EFF context code for additional Assessment Results |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_ASMT_PARTNER_CONFIG_FK1 | Non Unique | Default | PROVISIONING_ID |
| IRC_ASMT_PARTNER_CONFIG_PK | Unique | Default | PARTNER_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
