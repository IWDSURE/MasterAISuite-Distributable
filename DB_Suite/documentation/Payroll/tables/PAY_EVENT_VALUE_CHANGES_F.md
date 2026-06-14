# PAY_EVENT_VALUE_CHANGES_F

This table contains specific value changes that qualify a change and cause an event to be raised, or disqualify a change and prevent an event from being raised.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventvaluechangesf-20665.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payeventvaluechangesf-20665.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_EVENT_VALUE_CHANGES_F_PK | EVENT_VALUE_CHANGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_VALUE_CHANGE_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| PARENT_EVT_VAL_CHG_ID | NUMBER |  | 18 |  | Parent Event Value Change |
| EVENT_QUALIFIER_ID | NUMBER |  | 18 |  | Foreign Key to PAY_EVENT_QUALIFIERS_F |
| DATETRACKED_EVENT_ID | NUMBER |  | 18 |  | Foreign Key to PAY_DATETRACKED_EVENTS |
| DEFAULT_EVENT | VARCHAR2 | 30 |  |  | This denotes whether this is the default event entry |
| VALID_EVENT | VARCHAR2 | 30 |  | Yes | This value denotes whether this is a valid event to be reported. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign Key to FND_TERRITORIES |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| FROM_VALUE_OPTION | VARCHAR2 | 30 |  |  | FROM_VALUE_OPTION |
| FROM_VALUE | VARCHAR2 | 80 |  |  | The before value to be tested |
| TO_VALUE_OPTION | VARCHAR2 | 30 |  |  | TO_VALUE_OPTION |
| TO_VALUE | VARCHAR2 | 80 |  |  | The after value to be tested. |
| FORMULA_ID | NUMBER |  | 18 |  | Formula to be Used to test a value change |
| PRORATION_STYLE | VARCHAR2 | 30 |  |  | PRORATION_STYLE indicates the type of proration that should occur when this event is encountered. |
| SEQUENCE | NUMBER |  | 4 |  | Sequence of the event value changes |
| QUALIFIER_VALUE | VARCHAR2 | 2000 |  |  | QUALIFIER_VALUE contains a derived value that indicates whether the before and after value should be compared. |
| SEC_QUALIFIER_VALUE | VARCHAR2 | 2000 |  |  | SEC_QUALIFIER_VALUE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_EVENT_VALUE_CHANGES_F_PK | Unique | Default | EVENT_VALUE_CHANGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET1 |
| PAY_EVENT_VALUE_CHANGES_F_PK1 | Unique | Default | EVENT_VALUE_CHANGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORA_SEED_SET2 |
| PAY_EVT_VALUE_CHANGES_F_N1 | Non Unique | Default | PARENT_EVT_VAL_CHG_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_EVT_VALUE_CHANGES_F_N2 | Non Unique | Default | DATETRACKED_EVENT_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_EVT_VALUE_CHANGES_F_N20 | Non Unique | PAY_EVT_VALUE_CHANGES_F_N20 | SGUID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
