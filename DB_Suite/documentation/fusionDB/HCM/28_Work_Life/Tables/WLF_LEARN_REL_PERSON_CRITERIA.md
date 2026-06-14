# WLF_LEARN_REL_PERSON_CRITERIA

Table to store learn organization person criteria information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelpersoncriteria-27144.html#wlflearnrelpersoncriteria-27144](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflearnrelpersoncriteria-27144.html#wlflearnrelpersoncriteria-27144)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LEARN_REL_PER_CRITERIA_PK | CRITERIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CRITERIA_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| RELATION_ID | NUMBER |  | 18 | Yes | Learn organization relation id |
| CRITERIA_SOURCE_ID | NUMBER |  | 18 | Yes | Learning organization criteria source id |
| CRITERIA_SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Learning organization criteria object type. |
| CRITERIA_SOURCE_VALUE | VARCHAR2 | 4000 |  | Yes | Learn ing organiation criteria source value |
| STATUS | VARCHAR2 | 30 |  | Yes | This column represents status of the learn relation person criteria {ACTIVE, DELETED}. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Indicates the learn relation person criteria record active date |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Indicates the learn relation person criteria record removed date |
| PROCESSED_DATE | TIMESTAMP |  |  |  | stores the last processed dat of the learning organization reconcile job |
| PREVIOUS_ELAPSED_DURATION | NUMBER |  | 18 |  | Previous elapsed duration to process destination |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the content object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CRITERIA_NAME | VARCHAR2 | 250 |  |  | Stores the name of the criteria |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LEARN_REL_PER_CRITERIA_N1 | Non Unique | Default | RELATION_ID |
| WLF_LEARN_REL_PER_CRITERIA_N2 | Non Unique | Default | CRITERIA_SOURCE_VALUE, CRITERIA_SOURCE_TYPE |
| WLF_LEARN_REL_PER_CRITERIA_U1 | Unique | Default | CRITERIA_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
