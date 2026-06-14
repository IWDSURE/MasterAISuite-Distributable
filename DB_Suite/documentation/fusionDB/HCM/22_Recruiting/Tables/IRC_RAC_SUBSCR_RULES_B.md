# IRC_RAC_SUBSCR_RULES_B

This table contains the rules defined for a given subscriber.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracsubscrrulesb-19503.html#ircracsubscrrulesb-19503](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracsubscrrulesb-19503.html#ircracsubscrrulesb-19503)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RAC_SUBSCR_RULES_B_PK | SUBSCRIBER_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SUBSCRIBER_RULE_ID | NUMBER |  | 18 | Yes | This column will be used to store the primary key of this table. Auto Generated Key. |  |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | This a foreign key to IRC_RAC_SUBSCRIBERS table. | Obsolete |
| SUBSCRIBER_ID#01 | NUMBER |  | 18 | Yes | This a foreign key to IRC_RAC_SUBSCRIBERS table. |  |
| SUBSCRIBER_RULE_CODE | VARCHAR2 | 256 |  | Yes | This column stores the code for the rules. |  |
| RULE_PRIORITY_CODE | VARCHAR2 | 30 |  |  | Priority Code of each subscriber rule.Lookup used - ORA_IRC_RAC_RULE_PRIORITY |  |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This column indicates whether the rule is enabled or not. |  |
| ESS_RULE_FLAG | VARCHAR2 | 1 |  |  | Indicates if rule gets evaluated in ESS. ESS will skip other rules unless in "full refresh" mode. |  |
| MESSAGE | VARCHAR2 | 64 |  |  | Reference to message bundle for message for this rule. |  |
| APPLY_AFTER_AGE | NUMBER |  | 3 |  | Generate Action Item once this has been extended. It may measure length of inactivity , time in some status etc depending on the rule. |  |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |  |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RAC_SUBSCR_RULES_B_PK | Unique | FUSION_TS_SEED | SUBSCRIBER_RULE_ID, ORA_SEED_SET1 |
| IRC_RAC_SUBSCR_RULES_B_PK1 | Unique | FUSION_TS_SEED | SUBSCRIBER_RULE_ID, ORA_SEED_SET2 |
| IRC_RAC_SUBSCR_RULES_B_U1 | Unique | FUSION_TS_SEED | SUBSCRIBER_ID#01, SUBSCRIBER_RULE_CODE, ORA_SEED_SET1 |
| IRC_RAC_SUBSCR_RULES_B_U11 | Unique | FUSION_TS_SEED | SUBSCRIBER_ID#01, SUBSCRIBER_RULE_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
