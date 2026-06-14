# HWR_XP_VERB_B

This is the table for the experience store verbs.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpverbb-16692.html#hwrxpverbb-16692](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpverbb-16692.html#hwrxpverbb-16692)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_VERB_B_PK | VERB_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VERB_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this verb. |
| ID_IRI | VARCHAR2 | 2000 |  | Yes | Corresponds to a Verb definition. Each Verb definition corresponds to the meaning of a Verb, not the word. The ID should follow the IRI sandard. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_VERB_B_U1 | Unique | Default | VERB_ID |
| HWR_XP_VERB_B_U2 | Unique | Default | ID_IRI |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
