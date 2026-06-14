# IRC_RAC_RULE_ACTIONS

This table is used to store the actions defined for a given rule.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracruleactions-16092.html#ircracruleactions-16092](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracruleactions-16092.html#ircracruleactions-16092)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RAC_RULE_ACTIONS_PK | SUBSCRIBER_RULE_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SUBSCRIBER_RULE_ACTION_ID | NUMBER |  | 18 | Yes | This column will be used to store the primary key of this table. Auto Generated Key. |
| SUBSCRIBER_RULE_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_RAC_SUBSCR_RULES_B |
| SUBSCRIBER_RULE_CODE | VARCHAR2 | 256 |  | Yes | This column stores the subscriber rule code of the action. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This column determines whether the actions for a given rule is enabled or not. |
| DEFAULT_FLAG | VARCHAR2 | 1 |  | Yes | Indicates whether the action is a "default action" for the rule. |
| ACTION_CODE | VARCHAR2 | 30 |  | Yes | This stores the lookup code for the given action for lookup ORA_IRC_RAC_RULE_ACTION_CODE. |
| DEEPLINK | VARCHAR2 | 512 |  |  | This column is needed to store the deep link information for the actions which are needed to be executed on the ADF side. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RAC_RULE_ACTIONS_FK1 | Non Unique | FUSION_TS_SEED | SUBSCRIBER_RULE_ID |
| IRC_RAC_RULE_ACTIONS_PK | Unique | FUSION_TS_SEED | SUBSCRIBER_RULE_ACTION_ID, ORA_SEED_SET1 |
| IRC_RAC_RULE_ACTIONS_PK1 | Unique | FUSION_TS_SEED | SUBSCRIBER_RULE_ACTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
