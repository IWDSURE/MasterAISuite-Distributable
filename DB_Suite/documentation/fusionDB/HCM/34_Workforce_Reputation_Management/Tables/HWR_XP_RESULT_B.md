# HWR_XP_RESULT_B

This is the table for the experience store results.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpresultb-4431.html#hwrxpresultb-4431](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrxpresultb-4431.html#hwrxpresultb-4431)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_XP_RESULT_B_PK | RESULT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESULT_ID | NUMBER |  | 18 | Yes | The Unique database identifier for this result. |
| IS_SUCCESS | VARCHAR2 | 1 |  |  | Indicates whether or not the attempt on the Activity was successful. |
| IS_COMPLETION | VARCHAR2 | 1 |  |  | Indicates whether or not the Activity was completed. |
| RESPONSE | VARCHAR2 | 4000 |  |  | A response appropriately formatted for the given Activity. |
| DURATION | VARCHAR2 | 100 |  |  | Period of time over which the Statement occurred. The expected format should be ISO 8601. |
| SCORE_SCALED | NUMBER |  | 10 |  | The score related to the experience as modified by scaling and/or normalization. |
| SCORE_MIN | NUMBER |  | 10 |  | The lowest possible score for the experience described by the Statement. |
| SCORE_MAX | NUMBER |  | 10 |  | The highest possible score for the experience described by the Statement. |
| SCORE_RAW | NUMBER |  | 10 |  | The score achieved by the Actor in the experience described by the Statement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_XP_RESULT_B_U1 | Unique | Default | RESULT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
