# BEN_LEGAL_DISCLAIMER

This table will be used to hold legal disclaimers texts.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlegaldisclaimer-3094.html#benlegaldisclaimer-3094](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benlegaldisclaimer-3094.html#benlegaldisclaimer-3094)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_LEGAL_DISCLAIMER_PK | LEGAL_DISCLAIMER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LEGAL_DISCLAIMER_ID | NUMBER |  | 18 | Yes | LEGAL_DISCLAIMER_ID |
| DESCRIPTION | VARCHAR2 | 240 |  |  | DESCRIPTION |
| PGM_ID | NUMBER |  | 18 |  | PGM_ID |
| PL_ID | NUMBER |  | 18 |  | PL_ID |
| PTIP_ID | NUMBER |  | 18 |  | PTIP_ID |
| PLIP_ID | NUMBER |  | 18 |  | PLIP_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| LER_ID | NUMBER |  | 18 |  | LER_ID |
| DISCLAIMER_TEXT | CLOB |  |  | Yes | DISCLAIMER_TEXT |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_LEGAL_DISCLAIMER_FK1 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_LEGAL_DISCLAIMER_FK2 | Non Unique | Default | PLIP_ID |
| BEN_LEGAL_DISCLAIMER_FK3 | Non Unique | Default | PTIP_ID |
| BEN_LEGAL_DISCLAIMER_FK4 | Non Unique | Default | LER_ID |
| BEN_LEGAL_DISCLAIMER_PK | Unique | Default | LEGAL_DISCLAIMER_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
