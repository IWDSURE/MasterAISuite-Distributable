# HWR_PROJECT_B

The project table stores project details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojectb-13446.html#hwrprojectb-13446](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojectb-13446.html#hwrprojectb-13446)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PROJECT_B_PK | PROJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJECT_ID | NUMBER |  | 18 | Yes | This column stores the unique ID of the project. |
| PROJECT_KEY | VARCHAR2 | 500 |  | Yes | This is the unique project key of the project. |
| PROJECT_NAME | VARCHAR2 | 500 |  | Yes | This stores the unique name of the project. |
| START_DATE | DATE |  |  |  | This stores the start date of the project. |
| END_DATE | DATE |  |  |  | This stores the end date of the project. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PROJECT_B_U1 | Unique | FUSION_TS_TX_DATA | PROJECT_ID |
| HWR_PROJECT_B_U2 | Unique | FUSION_TS_TX_DATA | PROJECT_KEY |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
