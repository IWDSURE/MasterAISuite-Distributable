# CEL_PROGRAM_CARDS_B

MLS base table to hold quick recognition card details.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramcardsb-9095.html#celprogramcardsb-9095](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celprogramcardsb-9095.html#celprogramcardsb-9095)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_PROGRAM_CARDS_B_PK | CARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CARD_ID | NUMBER |  | 18 | Yes | Quick recognition card identifier |
| PROGRAM_ID | NUMBER |  | 18 | Yes | Program identifier |
| ILLUSTRATION_ID | NUMBER |  | 18 |  | Quick recognition illistration identifier |
| VALUE_ID | NUMBER |  | 18 |  | Quick recognition value identifier |
| POINTS | NUMBER |  |  |  | Quick recognition reward points |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_PROGRAM_CARDS_B_N1 | Non Unique | Default | PROGRAM_ID |
| CEL_PROGRAM_CARDS_B_PK | Unique | Default | CARD_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
