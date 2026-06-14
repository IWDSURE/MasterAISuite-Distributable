# BEN_BATCH_RANGES

BEN_BATCH_RANGES contains ranges of people that are going to be processedby multi-threaded programs. The number of people in a range is set by the chunk size for that particular concurrent program. The threads within a concurrent program attempt to process ranges of people until all ranges have been exhausted. The total number of ranges will be the number of people to be processed divided by the chunk size.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchranges-23710.html#benbatchranges-23710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbatchranges-23710.html#benbatchranges-23710)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BATCH_RANGES_PK | RANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RANGE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Foreign Key to BEN_BENEFIT_RELATIONS_F |
| RANGE_STATUS_CD | VARCHAR2 | 30 |  | Yes | Range status. |
| STARTING_PERSON_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PERSON_ACTIONS. |
| ENDING_PERSON_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PEOPLE_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_BATCH_RANGES_FK1 | Non Unique | Default | BENEFIT_RELATION_ID |  |
| BEN_BATCH_RANGES_FK4 | Non Unique | Default | BENEFIT_ACTION_ID | Obsolete |
| BEN_BATCH_RANGES_N1 | Non Unique | Default | BENEFIT_ACTION_ID, RANGE_STATUS_CD |  |
| BEN_BATCH_RANGES_N2 | Non Unique | Default | ENDING_PERSON_ACTION_ID |  |
| BEN_BATCH_RANGES_N3 | Non Unique | Default | STARTING_PERSON_ACTION_ID |  |
| BEN_BATCH_RANGES_PK1 | Unique | Default | RANGE_ID |  |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
