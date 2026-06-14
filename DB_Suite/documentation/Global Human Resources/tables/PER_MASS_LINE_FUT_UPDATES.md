# PER_MASS_LINE_FUT_UPDATES

Stores summary of changed attribute values of different entities.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permasslinefutupdates-7587.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permasslinefutupdates-7587.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_MASS_LINE_FUT_UPDATES_PK | MASS_ACTION_FUT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_ACTION_FUT_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MASS_ACTION_LINE_ID | NUMBER |  | 18 | Yes | The mass action line id associated to the surrogate key id. |
| MASS_ACTION_HEADER_ID | NUMBER |  | 18 | Yes | The mass action header id associated to one or more surrogate keys. |
| PERSON_ID | NUMBER |  | 18 | Yes | The PersonId of the person whose attribute changes are stored. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | The enterprise id of the person. |
| SURROGATE_KEY_ID | NUMBER |  | 18 | Yes | Surrogate key of the entity whose attribute changes are stored. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| SURROGATE_KEY_NAME | VARCHAR2 | 200 |  | Yes | Surrogate key name of the entity whose attribute changes are stored. |
| ENTITY_NAME | VARCHAR2 | 400 |  | Yes | Name of the entity whose attribute changes are stored.. |
| ATTRIBUTE | VARCHAR2 | 200 |  | Yes | The name of the attribute whose changed are stored. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | The ActionOccurrenceId of the entity row whose attribute changes are stored. |
| EFFECTIVE_SEQUENCE | NUMBER |  | 4 |  | Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day. |
| OLD_VALUE | VARCHAR2 | 4000 |  |  | The old value of the attribute that has changes in the source entity row. |
| NEW_VALUE | VARCHAR2 | 4000 |  |  | The new value of the attribute that has changes in the source entity row. |
| COPY_STATUS | VARCHAR2 | 30 |  |  | This indicates whether the copy of the update is done or not done. |
| DESTINATION_SURROGATE_KEY_ID | NUMBER |  | 18 |  | Surrogate key of the entity into which the attribute change has to be copied. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_MASS_LINE_FUT_UPDATES_N1 | Non Unique | Default | SURROGATE_KEY_ID |
| PER_MASS_LINE_FUT_UPDATES_N2 | Non Unique | Default | MASS_ACTION_LINE_ID |
| PER_MASS_LINE_FUT_UPDATES_N3 | Non Unique | Default | EFFECTIVE_START_DATE, SURROGATE_KEY_ID |
| PER_MASS_LINE_FUT_UPDATES_PK | Unique | Default | MASS_ACTION_FUT_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
