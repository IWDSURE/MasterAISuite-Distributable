# FAI_TOPICS_B_

This table stores information about topics.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitopicsb-8291.html#faitopicsb-8291](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitopicsb-8291.html#faitopicsb-8291)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_TOPICS_B_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies topics. |
| TOPIC_CODE | VARCHAR2 | 200 |  |  | Topic name. Uniquely identifies topics. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the Topic. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Topic. |
| SEEDED_FLAG | VARCHAR2 | 1 |  |  | This column differentiates seeded data from customer created. |
| STATUS | VARCHAR2 | 32 |  |  | This column provides topic status. |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Topic. |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the topic. |
| FAMILY | VARCHAR2 | 80 |  |  | Product family of the supported business object. |
| PRODUCT | VARCHAR2 | 100 |  |  | Product of the supported business object. |
| TOPIC_CREATED_DATE | DATE |  |  |  | The date when the topic was created. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_TOPICS_BN1_ | Non Unique | Default | TOPIC_ID |
| FAI_TOPICS_BU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, TOPIC_ID |

---

[← Back to Index](../2_AI_Tables_Index.md)
