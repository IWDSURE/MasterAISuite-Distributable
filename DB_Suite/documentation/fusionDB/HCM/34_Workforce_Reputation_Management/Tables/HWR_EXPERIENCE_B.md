# HWR_EXPERIENCE_B

The experience table stores profile experience data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrexperienceb-20847.html#hwrexperienceb-20847](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrexperienceb-20847.html#hwrexperienceb-20847)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_EXPERIENCE_B_PK | SOURCE_ID, EXPERIENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXPERIENCE_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the experience table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The Id of the source for the profile which has the experience. |
| COMPANY | VARCHAR2 | 255 |  |  | The company at which the person held the position. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | The description of the experience. |
| END_DATE | TIMESTAMP |  |  |  | The end date of the period for which the person held the position. |
| START_DATE | TIMESTAMP |  |  |  | The start date of the period for which the person held the position. |
| TITLE | VARCHAR2 | 255 |  |  | The title describing the position. |
| EXPERIENCE_TYPE | VARCHAR2 | 100 |  |  | The experience type of the experience. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_EXPERIENCE_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, EXPERIENCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
