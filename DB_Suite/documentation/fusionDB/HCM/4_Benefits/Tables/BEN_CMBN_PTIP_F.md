# BEN_CMBN_PTIP_F

BEN_CMBN_PTIP_F  is a collection of plan types ina program that may provide credits to a participant for enrolling in one or more plans of the specified plan types in the program. For example, the combination plan type in program of "Health Benefit" may be  comprised of Medical, Dental, and Vision Plan Types.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnptipf-13949.html#bencmbnptipf-13949](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencmbnptipf-13949.html#bencmbnptipf-13949)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CMBN_PTIP_F_PK | CMBN_PTIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CMBN_PTIP_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the combination plan type in program. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| PGM_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_PGM_F. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CMBN_PTIP_F_N1 | Non Unique |  | NAME |
| BEN_CMBN_PTIP_F_PK | Unique | Default | CMBN_PTIP_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
