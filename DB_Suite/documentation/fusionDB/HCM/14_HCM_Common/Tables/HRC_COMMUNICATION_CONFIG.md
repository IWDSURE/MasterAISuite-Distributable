# HRC_COMMUNICATION_CONFIG

This table stores the configuration information for HCM Communications

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationconfig-5515.html#hrccommunicationconfig-5515](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccommunicationconfig-5515.html#hrccommunicationconfig-5515)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_COMMUNICATION_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Unique Identifier to identify the configuration record |
| PROCESS_ID | NUMBER |  | 18 | Yes | Unique Identifier of the process to which the configuration belong to |
| TWO_WAY_COMM_SUPPORTED | VARCHAR2 | 20 |  |  | Parameter to indicate whether two way communication is supported or not |
| IS_BIP_CONTENT_SUPPORTED | VARCHAR2 | 20 |  |  | Indicate whether the BIP content is supported or not |
| BIP_TEMPLATE | VARCHAR2 | 500 |  |  | Details or the path of the BIP Template which is defined to show the report content. |
| IS_CUSTOM_ACTIONS_ALLOWED | VARCHAR2 | 20 |  |  | Indicates whether the custom actions are supported by the communication or not. |
| APPROVAL_CONFIGURATION_JSON | CLOB |  |  |  | Json Configuration record, which will indicate the different levels of approval and rules on each level. |
| IS_SMS_SUPPORTED | VARCHAR2 | 1 |  |  | indicates whether sms mode is supported by the communication or not |
| IS_EMAIL_SUPPORTED | VARCHAR2 | 1 |  |  | indicates whether email mode is supported by the communication or not |
| IS_PUSH_SUPPORTED | VARCHAR2 | 1 |  |  | indicates whether push mode is supported by the communication or not |
| DELEGATION_CATEGORY | VARCHAR2 | 120 |  |  | value of the category corresponding to which this process will be mapped for approval delegations |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Unique Identifier of the enterprise to filter out the records which does not belong to. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| PURGE_PERIOD | VARCHAR2 | 64 |  |  | Indicates purge period for a communication process |
| SHOW_IN_CONFIG_UI | VARCHAR2 | 1 |  |  | Indicates whether to show the configuration entry in message configuration ui or not. |
| DISABLE_COMMUNICATION | VARCHAR2 | 1 |  |  | Indicates whether to enable the communication for the process or not. If this is false it will result into error. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMMUNICATION_CONFIG_PK | Unique | Default | CONFIG_ID, ORA_SEED_SET1 |
| HRC_COMMUNICATION_CONFIG_PK1 | Unique | Default | CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
