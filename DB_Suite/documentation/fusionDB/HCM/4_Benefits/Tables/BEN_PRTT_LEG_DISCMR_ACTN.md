# BEN_PRTT_LEG_DISCMR_ACTN

BEN_PRTT_LEG_DISCMR_ACTN contains the status of the action taken by the self-service user against a legal disclaimer. The status can be either Accept/Decline.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttlegdiscmractn-16617.html#benprttlegdiscmractn-16617](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benprttlegdiscmractn-16617.html#benprttlegdiscmractn-16617)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PRTT_LEG_DISCMR_ACTN_PK | PRTT_LEG_DISCMR_ACTN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PRTT_LEG_DISCMR_ACTN_ID | NUMBER |  | 18 | Yes | System generated primary key PRTT_LEG_DISCMR_ACTN_ID |
| PL_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_PL_F |
| PTIP_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_PTIP_F |
| PGM_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_PGM_F |
| PLIP_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_PL_F |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | This column holds LEGAL_ENTITY_ID |
| LER_ID | NUMBER |  | 18 |  | This column holds foreign key to BEN_LER_F |
| PER_IN_LER_ID | NUMBER |  | 18 |  | This column holds PER_IN_LER_ID |
| BENEFIT_RELATION_ID | NUMBER |  | 18 |  | This column holds BENEFIT_RELATION_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | This column holds PERSON_ID value |
| LEGAL_DISCLAIMER_ID | NUMBER |  | 18 |  | This column holds LEGAL_DISCLAIMER_ID |
| STATUS | VARCHAR2 | 30 |  | Yes | This column holds STATUS value. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| ACTION_TIME | TIMESTAMP |  |  |  | This column holds ACTION_TIME value |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PRTT_LEG_DIS_ACTN_FK2 | Non Unique | Default | BENEFIT_RELATION_ID |
| BEN_PRTT_LEG_DIS_ACTN_N1 | Non Unique | Default | PERSON_ID, PER_IN_LER_ID |
| BEN_PRTT_LEG_DIS_ACTN_N2 | Non Unique | Default | PER_IN_LER_ID |
| BEN_PRTT_LEG_DIS_ACTN_PK | Unique | Default | PRTT_LEG_DISCMR_ACTN_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
