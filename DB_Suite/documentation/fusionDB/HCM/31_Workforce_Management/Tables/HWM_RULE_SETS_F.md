# HWM_RULE_SETS_F

Contains the rule sets created for OTL Time Calculation, Time Entry, Time device, and Time Audit rules.

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetsf-25977.html#hwmrulesetsf-25977](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmrulesetsf-25977.html#hwmrulesetsf-25977)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_RULE_SETS_F_PK | RULE_SET_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| RULE_SET_ID | NUMBER |  | 18 | Yes | Primary Key column containing a random generated number.  This column is not updateable. | Active |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |  |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| RULE_SET_UNQ_ID | NUMBER |  | 18 | Yes | RULE_SET_UNQ_ID |  |
| RULE_SET_NAME | VARCHAR2 | 80 |  | Yes | Name of Rule set |  |
| RULE_TYPE | VARCHAR2 | 30 |  | Yes | RULE_TYPE |  |
| ACTIVE_START_DATE | DATE |  |  |  | Active Start Date |  |
| ACTIVE_END_DATE | DATE |  |  |  | Active End Date |  |
| SOURCE | VARCHAR2 | 30 |  |  | SOURCE |  |
| SORT_ENTRY_TYPE | VARCHAR2 | 30 |  |  | SORT_ENTRY_TYPE |  |
| SORT_DURATION | VARCHAR2 | 30 |  |  | SORT_DURATION |  |
| SORT_ATTRIBUTE1 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE1 |  |
| SORT_ATTRIBUTE2 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE2 |  |
| SORT_ATTRIBUTE3 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE3 |  |
| SORT_ATTRIBUTE4 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE4 |  |
| SORT_ATTRIBUTE5 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE5 |  |
| SORT_ATTRIBUTE6 | VARCHAR2 | 30 |  |  | SORT_ATTRIBUTE6 |  |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the Rule Set (Optional) | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |  |
| XJDB_VERSION | VARCHAR2 | 30 |  |  | XJDB_VERSION |  |
| XJDB_CACHE | CLOB |  |  |  | XJDB_CACHE |  |
| IS_DRAFT | VARCHAR2 | 1 |  |  | Indicates whether a rule set is still in draft mode and has not been fully validated. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HWM_RULE_SETS_F_PK | Unique | FUSION_TS_TX_DATA | RULE_SET_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE | Active |
| HWM_RULE_SETS_F_U1 | Unique | FUSION_TS_TX_DATA | RULE_SET_NAME, EFFECTIVE_START_DATE |  |
| HWM_RULE_SETS_F_U2 | Unique | FUSION_TS_TX_DATA | RULE_SET_UNQ_ID |  |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
