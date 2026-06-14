# BEN_PERSON_ACTIONS

BEN_PERSON_ACTIONS identifies persons
                                         being processed in a benefits
                                         concurrent manager process.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpersonactions-7078.html#benpersonactions-7078](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benpersonactions-7078.html#benpersonactions-7078)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PERSON_ACTIONS_PK | PERSON_ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| PERSON_ACTION_ID | NUMBER |  | 18 | Yes | System generated primary key
                                               column. | Active |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_PEOPLE_F. | Active |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. | Active |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. | Active |
| ACTION_STATUS_CD | VARCHAR2 | 30 |  | Yes | Action status. | Active |
| CHUNK_NUMBER | NUMBER |  | 18 |  | Number of chunks for concurrent
                                               process. | Active |
| NON_PERSON_CD | VARCHAR2 | 30 |  |  | Non-person code. | Active |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID | Active |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | BENEFIT_RELATION_ID | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| BEN_PERSON_ACTIONS_FK2 | Non Unique | Default | BENEFIT_RELATION_ID |  |
| BEN_PERSON_ACTIONS_FK3 | Non Unique | FUSION_TS_TX_DATA | BENEFIT_ACTION_ID | Active |
| BEN_PERSON_ACTIONS_N1 | Non Unique | FUSION_TS_TX_DATA | PERSON_ID | Active |
| BEN_PERSON_ACTIONS_N2 | Non Unique | FUSION_TS_TX_DATA | LER_ID | Active |
| BEN_PERSON_ACTIONS_PK | Unique | FUSION_TS_TX_DATA | PERSON_ACTION_ID | Active |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
