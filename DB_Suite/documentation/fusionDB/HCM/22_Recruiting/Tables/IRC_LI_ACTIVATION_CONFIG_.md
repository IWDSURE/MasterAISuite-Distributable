# IRC_LI_ACTIVATION_CONFIG_

Stores the activation details of LinkedIn integration in Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircliactivationconfig-5784.html#ircliactivationconfig-5784](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircliactivationconfig-5784.html#ircliactivationconfig-5784)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LI_ACTIVATION_CONFIG_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. | Active |
| PROVISIONING_ID | NUMBER |  | 18 |  | Foreign key to IRC_TP_PARTNER_PROVISNGS | Active |
| APP_ID | VARCHAR2 | 64 |  |  | Unique ID that represents the provisioning application created for the integration | Active |
| APP_URN | VARCHAR2 | 300 |  |  | URN representing the provisioning application created for the integration | Active |
| APP_NAME | VARCHAR2 | 300 |  |  | Name of the provisioning application created for the integration | Active |
| APP_DESC | VARCHAR2 | 1000 |  |  | Brief description of the provisioning application created for the integration | Active |
| VALID_DOMAINS | VARCHAR2 | 2000 |  |  | List of fully qualified domain names allowed by the partner for the integration | Active |
| INTEGRATION_CONTEXT | VARCHAR2 | 300 |  |  | URN representing the data-integration-context for the integration | Active |
| INTEGRATION_NAME | VARCHAR2 | 300 |  |  | Customer facing name for the integration | Active |
| INTEGRATION_TYPE | VARCHAR2 | 300 |  |  | Type of integration supported by partner | Active |
| TENANT_TYPE | VARCHAR2 | 300 |  |  | Role type needed for the integration | Active |
| ONBOARDING_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the onboarding status of the integration. The corresponding lookup type is ORA_IRC_LI_ONBOARDING_STATUS | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CONTRACT_ID | NUMBER |  | 18 |  | Foreign key to IRC_LI_CONTRACTS. |  |
| INTEGRATION_STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the status of the integration in ORC. The corresponding lookup type is ORA_IRC_LI_INTEGRATION_STATUS |  |
| LAST_ACTIVATED_BY | VARCHAR2 | 64 |  |  | Indicates the user who last activated the integration. |  |
| LAST_ACTIVE_DATE | TIMESTAMP |  |  |  | Indicates the date and time the integration was last activated. |  |
| LAST_INACTIVATED_BY | VARCHAR2 | 64 |  |  | Indicates the user who last inactivated the integration. |  |
| LAST_INACTIVE_DATE | TIMESTAMP |  |  |  | Indicates the date and time the integration was last inactivated. |  |
| USER_NAME | VARCHAR2 | 250 |  |  | To store user name sent to the third party (based on integration type column) |  |
| ADDL_INFO1_LAST_SENT_DATE | TIMESTAMP |  |  |  | Store the last time additional information is sent to the third party |  |
| COMPANY_URL | VARCHAR2 | 2000 |  |  | To store company URL to be sent to the third party (based on integration type column) |  |
| NOTIFICATION_STATUS_CODE | VARCHAR2 | 30 |  |  | To store integration partner notification status if available for a given integration type. ORA_ENABLED or ORA_DISABLED |  |
| EASY_APPLY_STATUS_CODE | VARCHAR2 | 30 |  |  | To store Easy apply status.
Default: ORA_ENABLED. ORA_ENABLED or ORA_DISABLED |  |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |  |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |  |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_LI_ACTIVATION_CONFIGN1_ | Non Unique | Default | CONFIG_ID |  |
| IRC_LI_ACTIVATION_CONFIG_PK_ | Unique | FUSION_TS_TX_IDX | LAST_UPDATE_DATE, LAST_UPDATED_BY, CONFIG_ID | Active |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
