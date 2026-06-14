# PAY_EVENT_ACTIONS_F

This table contains the Action Definitions to be used by Events.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventactionsf-27891.html#payeventactionsf-27891](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventactionsf-27891.html#payeventactionsf-27891)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_ACTION_PK | EVENT_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| EVENT_ACTION_TYPE_ID | NUMBER |  | 18 | Yes | Foreign key to PAY_EVENT_ACTION_TYPE |
| BASE_NAME | VARCHAR2 | 80 |  | Yes | Name of the Action |
| REPORT_TYPE | VARCHAR2 | 30 |  |  | The Report Type of a HCM Extract |
| ACTION_SUBMISSION | VARCHAR2 | 30 |  | Yes | The method for the action to be performed (Sync/Async) |
| LOOKBACK_TIME_DEF_ID | NUMBER |  | 18 |  | Foreign key to the PAY_TIME_DEFINITIONS table |
| ACTION_PARAM_GROUP_ID | NUMBER |  | 18 |  | Foreign Key to the Action Parameter Group Id to be used with this Action. |
| ALERT_ID | NUMBER |  | 18 |  | Foreign key to Alerts |
| ALERT_TEMPLATE_ID | NUMBER |  | 18 |  | Template for Alert. |
| INFORMATION_CHAR1 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR2 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR3 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR4 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR5 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR6 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR7 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR8 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR9 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR10 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR11 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR12 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR13 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR14 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR15 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR16 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR17 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR18 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR19 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR20 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR21 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR22 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR23 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR24 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR25 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR26 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR27 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR28 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR29 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_CHAR30 | VARCHAR2 | 150 |  |  | Flexfield Char |
| INFORMATION_NUMBER1 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER2 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER3 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER4 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER5 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER6 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER7 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER8 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER9 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER10 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER11 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER12 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER13 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER14 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER15 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER16 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER17 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER18 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER19 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_NUMBER20 | NUMBER |  |  |  | Flexfield Number |
| INFORMATION_DATE1 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE2 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE3 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE4 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE5 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE6 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE7 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE8 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE9 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE10 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE11 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE12 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE13 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE14 | DATE |  |  |  | Flexfield Date |
| INFORMATION_DATE15 | DATE |  |  |  | Flexfield Date |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | LEGISLATION_CODE |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | LEGISLATIVE_DATA_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| INFORMATION_CATEGORY | VARCHAR2 | 120 |  |  | Developer Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_EVENT_ACTIONS_F_N1 | Non Unique | Default | EVENT_ACTION_TYPE_ID |
| PAY_EVENT_ACTIONS_F_N2 | Non Unique | Default | BASE_NAME |
| PAY_EVENT_ACTIONS_F_PK | Unique | Default | EVENT_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_EVENT_ACTIONS_F_PK1 | Unique | Default | EVENT_ACTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_EVENT_ACTIONS_F_SGUID_N20 | Non Unique | Default | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
