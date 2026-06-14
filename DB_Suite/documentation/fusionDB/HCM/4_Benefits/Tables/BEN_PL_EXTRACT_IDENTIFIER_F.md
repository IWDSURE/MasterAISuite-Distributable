# BEN_PL_EXTRACT_IDENTIFIER_F

The ANSI 834 extract delivered by Oracle allows customers to send their enrollment changes to their Plan providers. Some plan providers allocate different plan identifiers for the same plans and options depending on the indicative data of the employee who is enrolled. This table identifies multiple identifiers for the same plan or option in plan, based on the Indicative data stored on their employee assignment and address.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplextractidentifierf-18970.html#benplextractidentifierf-18970](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benplextractidentifierf-18970.html#benplextractidentifierf-18970)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PL_EXTRACT_IDENTIFIER_PK | PL_EXTRACT_IDENTIFIER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PL_EXTRACT_IDENTIFIER_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| PL_ID | NUMBER |  | 18 |  | Foreign key to BEN_PL_F. |
| PLIP_ID | NUMBER |  | 18 |  | Foreign key to BEN_PLIP_F |
| OIPL_ID | NUMBER |  | 18 |  | Foreign key to BEN_OIPL_F |
| THIRD_PARTY_IDENTIFIER | VARCHAR2 | 10 |  |  | Plan Third Party Identifier |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Foreign key to HR_ORGANIZATION_UNITS |
| JOB_ID | NUMBER |  | 18 |  | Foreign key to PER_JOBS |
| POSITION_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_POSITIONS. |
| PEOPLE_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PAY_PEOPLE_GROUPS. |
| GRADE_ID | NUMBER |  | 18 |  | Foreign key to PER_GRADES |
| PAYROLL_ID | NUMBER |  | 18 |  | Foreign key to PAY_PAYROLLS. |
| HOME_STATE | VARCHAR2 | 30 |  |  | Home State |
| HOME_ZIP | VARCHAR2 | 30 |  |  | Zip Range |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PL_EXT_IDENTIFIER_F_FK2 | Non Unique |  | PL_ID |
| BEN_PL_EXT_IDENTIFIER_F_FK3 | Non Unique |  | PLIP_ID |
| BEN_PL_EXT_IDENTIFIER_F_FK4 | Non Unique |  | OIPL_ID |
| BEN_PL_EXT_IDENTIFIER_F_PK | Unique | Default | PL_EXTRACT_IDENTIFIER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
