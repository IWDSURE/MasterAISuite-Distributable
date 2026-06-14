# HWR_RESOURCE_B

The resource table stores resource details.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresourceb-20610.html#hwrresourceb-20610](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresourceb-20610.html#hwrresourceb-20610)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_RESOURCE_B_PK | RESOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RESOURCE_ID | NUMBER |  | 18 | Yes | This is the primary key for the resource table. |
| PROJECT_KEY | VARCHAR2 | 500 |  | Yes | This is the unique key of the project the resource is a part of. |
| RESOURCE_KEY | VARCHAR2 | 500 |  | Yes | This is the unique key of the resource. |
| PRFL_ID | VARCHAR2 | 500 |  |  | This is the profile Id of the resource. |
| RESOURCE_NAME | VARCHAR2 | 500 |  |  | This stores the name of the resource. |
| RESOURCE_EMAIL | VARCHAR2 | 800 |  |  | This stores the email of the resource. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_RESOURCE_B_U1 | Unique | FUSION_TS_TX_DATA | RESOURCE_ID |
| HWR_RESOURCE_B_U2 | Unique | FUSION_TS_TX_DATA | PROJECT_KEY, RESOURCE_KEY |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
