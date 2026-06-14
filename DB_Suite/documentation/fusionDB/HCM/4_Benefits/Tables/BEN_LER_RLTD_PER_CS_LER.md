# BEN_LER_RLTD_PER_CS_LER

BEN_LER_RLTD_PER_CS_LER_F  identifies what life event reasons, when they occur for one person, signal the need to generate another life event for a person related to that individual.  . For example, the life event reason of death of a participant means that persons related to that person may have a life event reason of death of participant which provided coverage.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerrltdpercsler-11242.html#benlerrltdpercsler-11242](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlerrltdpercsler-11242.html#benlerrltdpercsler-11242)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LER_RLTD_PER_CS_LER_PK | LER_RLTD_PER_CS_LER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| LER_RLTD_PER_CS_LER_ID | NUMBER |  | 18 | Yes | System generated primary key column. | Active |
| LER_RLTD_PER_CS_CHG_RL | NUMBER |  | 18 |  | Foreign key to FF_FORMULAS_F. | Active |
| LER_ID | NUMBER |  | 18 | Yes | Foreign Key to BEN_LER_F. | Active |
| RLTD_PER_CHG_CS_LER_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_RLTD_PER_CHG_CS_LER_F. | Active |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| CHG_MANDATORY_CD | VARCHAR2 | 30 |  |  | Mandatory Code Y or N | Active |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LER_RLTD_PER_CS_LER_N2 | Non Unique |  | LER_ID |
| BEN_LER_RLTD_PER_CS_LER_N3 | Non Unique |  | RLTD_PER_CHG_CS_LER_ID |
| BEN_LER_RLTD_PER_CS_LER_PK | Unique | Default | LER_RLTD_PER_CS_LER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
