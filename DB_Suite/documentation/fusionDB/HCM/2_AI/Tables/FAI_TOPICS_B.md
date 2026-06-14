# FAI_TOPICS_B

This table stores information about topics.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitopicsb-14886.html#faitopicsb-14886](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faitopicsb-14886.html#faitopicsb-14886)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_TOPICS_B_PK | TOPIC_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOPIC_ID | NUMBER |  | 18 | Yes | Primary key. Uniquely identifies topics. |
| TOPIC_CODE | VARCHAR2 | 200 |  | Yes | Topic name. Uniquely identifies topics. |
| INTERNAL_NAME | VARCHAR2 | 200 |  |  | This column represents the system name of the Topic. |
| INTERNAL_DESCRIPTION | VARCHAR2 | 2000 |  |  | This column represents the system description of the Topic. |
| SEEDED_FLAG | VARCHAR2 | 1 |  | Yes | This column differentiates seeded data from customer created. |
| STATUS | VARCHAR2 | 32 |  | Yes | This column provides topic status. |
| OWNER_ID | NUMBER |  | 18 |  | ID of the owner who created the Gen AI Topic. |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Name of the owner who created the topic. |
| FAMILY | VARCHAR2 | 80 |  |  | Product family of the supported business object. |
| PRODUCT | VARCHAR2 | 100 |  |  | Product of the supported business object. |
| TOPIC_CREATED_DATE | DATE |  |  |  | The date when the topic was created. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_TOPICS_B_U1 | Unique | Default | TOPIC_ID, ORA_SEED_SET1 |
| FAI_TOPICS_B_U11 | Unique | Default | TOPIC_ID, ORA_SEED_SET2 |
| FAI_TOPICS_B_U2 | Unique | Default | TOPIC_CODE, ORA_SEED_SET1 |
| FAI_TOPICS_B_U21 | Unique | Default | TOPIC_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../2_AI_Tables_Index.md)
