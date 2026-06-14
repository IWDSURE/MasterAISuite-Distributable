# PER_CHECKLIST_ACTIONS

PER_CHECKLIST_ACTIONS : Stores the event for a checklist

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistactions-10641.html#perchecklistactions-10641](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistactions-10641.html#perchecklistactions-10641)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| CHECKLIST_ACTION_ID | NUMBER |  | 18 | Yes | Primary Key |  |
| EVALUATION_MODE | VARCHAR2 | 10 |  |  | Evaluation Mode. |  |
| CONDITION_TEXT1 | VARCHAR2 | 4000 |  |  | Stores the checklist action trigger condition |  |
| CONDITION_TEXT2 | VARCHAR2 | 4000 |  |  | Stores the checklist action trigger condition |  |
| CONDITION_TEXT3 | VARCHAR2 | 4000 |  |  | Stores the checklist action trigger condition |  |
| CONDITION_TEXT4 | VARCHAR2 | 4000 |  |  | Stores the checklist action trigger condition |  |
| CONDITION_TEXT5 | VARCHAR2 | 4000 |  |  | Stores the checklist action trigger condition |  |
| CHECKLIST_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_CHECKLISTS_B.CHECKLIST_ID |  |
| CHECKLIST_ACTION_CODE | VARCHAR2 | 250 |  | Yes | Unique for each checklist |  |
| ACTION_TYPE | VARCHAR2 | 80 |  | Yes | The type of event. Valid values are

ORA_ACTION_AND_REASON - Action / Action reason

ORA_PERSON_DATA_CHANGE - Person data change |  |
| EVENT_CODE | VARCHAR2 | 270 |  |  | Mandatory for ACTION_TYPE= ORA_PERSON_DATA_CHANGE

The event code |  |
| OLD_VALUE | VARCHAR2 | 30 |  |  | Mandatory for ACTION_TYPE= ORA_PERSON_DATA_CHANGE

The old value of the column.

Valid values are

ORA_NO_VALUE - No Value

ORA_ANY_VALUE - Any Value

ORA_SPECIFIC_VALUE - Specific Value |  |
| OLD_VALUE_SPECIFIC | VARCHAR2 | 240 |  |  | Mandatory for ACTION_TYPE= ORA_PERSON_DATA_CHANGE and OLD_VALUE = ORA_SPECIFIC_VALUE |  |
| NEW_VALUE | VARCHAR2 | 30 |  |  | Mandatory for ACTION_TYPE= ORA_PERSON_DATA_CHANGE

The new value of the column.

Valid values are

ORA_NO_VALUE - No Value

ORA_ANY_VALUE - Any Value

ORA_SPECIFIC_VALUE - Specific Value |  |
| NEW_VALUE_SPECIFIC | VARCHAR2 | 240 |  |  | Mandatory for ACTION_TYPE= ORA_PERSON_DATA_CHANGE and NEW_VALUE = ORA_SPECIFIC_VALUE |  |
| ACTION_ID | NUMBER |  | 18 |  | Mandatory for ACTION_TYPE= ORA_ACTION_AND_REASON

Foreign Key to PER_ACTIONS_B.ACTION_ID |  |
| ACTION_REASON_ID | NUMBER |  | 18 |  | Valid only for ACTION_TYPE= ORA_ACTION_AND_REASON

Foreign Key to PER_ACTION_REASONS_B.ACTION_REASON_ID |  |
| ENABLED_FLAG | VARCHAR2 | 4 |  |  | Indicates whether the action is active or not. |  |
| OBSOLETE_FLAG | VARCHAR2 | 4 |  |  | Indicates whether the action is obsolete or not. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |
| RULE_ID | NUMBER |  | 18 |  | RULE_ID |  |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLIST_ACTIONS_N1 | Non Unique | Default | CHECKLIST_ID |
| PER_CHECKLIST_ACTIONS_N2 | Non Unique | Default | ACTION_ID, ACTION_REASON_ID |
| PER_CHECKLIST_ACTIONS_N3 | Non Unique | Default | EVENT_CODE |
| PER_CHECKLIST_ACTIONS_PK | Unique | Default | CHECKLIST_ACTION_ID, CHECKLIST_ACTION_CODE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
