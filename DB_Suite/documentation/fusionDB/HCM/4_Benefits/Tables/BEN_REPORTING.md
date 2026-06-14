# BEN_REPORTING

BEN_REPORTING contains information, such as the person or life event and error text, about all the errors that occurred as a result of running a benefits process through the concurrent manager.  It also stores all informational messages, such as person was eligible for plan X, electable choice created for option Y.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benreporting-12909.html#benreporting-12909](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benreporting-12909.html#benreporting-12909)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_REPORTING_PK | REPORTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REPORTING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BENEFIT_ACTION_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_BENEFIT_ACTION. |
| THREAD_ID | NUMBER |  | 30 | Yes | Thread  that saved the reporting line. |
| SEQUENCE | NUMBER |  | 38 | Yes | Sequence. |
| TEXT | VARCHAR2 | 2000 |  |  | Text. |
| REP_TYP_CD | VARCHAR2 | 30 |  |  | Report type. |
| ERROR_MESSAGE_CODE | VARCHAR2 | 90 |  |  | Error message code. |
| RELATED_PERSON_LER_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| TEMPORAL_LER_ID | NUMBER |  | 18 |  | Foreign key to BEN_LER_F. |
| LER_ID | NUMBER |  | 18 |  | Foreign Key to BEN_LER_F. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_PEOPLE_F. |
| PGM_ID | NUMBER |  | 18 |  | Foreign key to BEN_PGM_F. |
| PL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_PL_F. |
| RELATED_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_PEOPLE_F. |
| OIPL_ID | NUMBER |  | 18 |  | Foreign Key to BEN_OIPL_F. |
| PL_TYP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_TYP_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| ACTL_PREM_ID | NUMBER |  | 18 |  | Foreign Key to BEN_ACTL_PREM_F. |
| VAL | NUMBER |  |  |  | Value. |
| MO_NUM | NUMBER |  | 18 |  | Month number. |
| YR_NUM | NUMBER |  | 18 |  | Year . |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | Benefit Relation ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal Entity Id |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_REPORTING_FK3 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_REPORTING_N1 | Non Unique | Default | REP_TYP_CD, BENEFIT_ACTION_ID |
| BEN_REPORTING_PK | Unique | Default | REPORTING_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
