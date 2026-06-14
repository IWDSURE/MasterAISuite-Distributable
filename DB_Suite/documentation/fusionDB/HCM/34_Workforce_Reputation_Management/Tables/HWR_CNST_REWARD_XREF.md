# HWR_CNST_REWARD_XREF

This table is a corss referece table that connects contests and rewards.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstrewardxref-6514.html#hwrcnstrewardxref-6514](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcnstrewardxref-6514.html#hwrcnstrewardxref-6514)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CNST_REWARD_XREF_PK | CONTEST_ID, REWARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEST_ID | NUMBER |  | 18 | Yes | This column is a foreign key to HWR_CNST_B table. |
| REWARD_ID | NUMBER |  | 18 | Yes | This column is a foreign key to HWR_REWARD_B table |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CNST_REWARD_XREF_N1 | Non Unique | FUSION_TS_TX_DATA | REWARD_ID |
| HWR_CNST_REWARD_XREF_U1 | Unique | FUSION_TS_TX_DATA | CONTEST_ID, REWARD_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
