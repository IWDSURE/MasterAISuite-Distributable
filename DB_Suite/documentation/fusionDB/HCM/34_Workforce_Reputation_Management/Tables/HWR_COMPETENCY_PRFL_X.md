# HWR_COMPETENCY_PRFL_X

This cross reference (xref) table stores relationship between profile and competency.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcompetencyprflx-16903.html#hwrcompetencyprflx-16903](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcompetencyprflx-16903.html#hwrcompetencyprflx-16903)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_COMPETENCY_PRFL_X_PK | SOURCE_ID, COMPETENCY_ID, PRFL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the competency. |
| COMPETENCY_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the competency table. |
| PRFL_ID | VARCHAR2 | 500 |  | Yes | The Id of the profile which has the competency. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_COMPETENCY_PRFL_X_N1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_ID, PRFL_ID |
| HWR_COMPETENCY_PRFL_X_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, COMPETENCY_ID, PRFL_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
