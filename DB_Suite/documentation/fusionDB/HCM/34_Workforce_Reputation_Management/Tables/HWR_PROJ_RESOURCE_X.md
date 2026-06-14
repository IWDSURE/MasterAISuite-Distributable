# HWR_PROJ_RESOURCE_X

This cross reference (xref) table stores the relation between the project and the resources.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojresourcex-14419.html#hwrprojresourcex-14419](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrprojresourcex-14419.html#hwrprojresourcex-14419)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_PROJ_RESOURCE_X_PK | PROJECT_ID, RESOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROJECT_ID | NUMBER |  | 18 | Yes | This column stores the unique project ID. |
| RESOURCE_ID | NUMBER |  | 18 | Yes | This stores the resource ID of the resource. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_PROJ_RESOURCE_X_N1 | Non Unique | FUSION_TS_TX_DATA | RESOURCE_ID |
| HWR_PROJ_RESOURCE_X_U1 | Unique | FUSION_TS_TX_DATA | PROJECT_ID, RESOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
