# HRC_MESSAGE_ACTIONS_B

This table holds the actions which will be supported by each process in communication model

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageactionsb-29800.html#hrcmessageactionsb-29800](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcmessageactionsb-29800.html#hrcmessageactionsb-29800)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_MESSAGE_ACTIONS_B_PK | ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | Unique identifier for the action deifined to be included in communication. |
| CONFIG_ID | NUMBER |  | 18 | Yes | Id for the communication configuration enty for which action is to be used |
| IS_AFFIRMATIVE_ACTION | VARCHAR2 | 20 |  |  | This value will confirm that the approval will be routed to the next level or not. This will have the value of yes or no. |
| ACTION_CODE | VARCHAR2 | 50 |  |  | Code of the action which will be included in the communication. This will be used in the application. |
| IS_ACTIVE | VARCHAR2 | 20 |  |  | This value indicates whether the action is active or not. If an action is defined as inactive it will no longer will be available. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | The identifier of the enterprise.This is used to filter out the items based on enterprise. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_MESSAGE_ACTIONS_B_PK | Unique | Default | ACTION_ID, ORA_SEED_SET1 |
| HRC_MESSAGE_ACTIONS_B_PK1 | Unique | Default | ACTION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
