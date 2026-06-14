# HWR_ACCOMPLISH_B

The accomplishment table stores profile accomplishment data.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwraccomplishb-4119.html#hwraccomplishb-4119](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwraccomplishb-4119.html#hwraccomplishb-4119)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_ACCOMPLISH_B_PK | SOURCE_ID, ACCOMPLISHMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACCOMPLISHMENT_ID | VARCHAR2 | 500 |  | Yes | This is the primary key for the accomplishment table. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The source Id for the profile which has the accomplishment. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This is the description of the accomplishment |
| COMMENTS | VARCHAR2 | 1000 |  |  | This is the user comment for the accomplishment. |
| START_DATE | TIMESTAMP |  |  |  | This is the start date of the accomplishment. |
| END_DATE | TIMESTAMP |  |  |  | This is the end date of the accomplishment. |
| COMPLETION_DATE | TIMESTAMP |  |  |  | This is the completion date of the accomplishment. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_ACCOMPLISH_B_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_ID, ACCOMPLISHMENT_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
