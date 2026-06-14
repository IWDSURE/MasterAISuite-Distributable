# HWR_CTL_RSLT_TYP_MAP_B

This table is for types mapping (just like Xref table)

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrctlrslttypmapb-6378.html#hwrctlrslttypmapb-6378](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrctlrslttypmapb-6378.html#hwrctlrslttypmapb-6378)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CTL_RSLT_TYP_MAP_B_PK | TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TYPE_ID | NUMBER |  | 18 | Yes | This column is the Id indicating the type of the post-control record |
| TYPE_NAME | VARCHAR2 | 80 |  | Yes | The column is the name of the post-control record |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | This column is for the description of the post-control record |
| DESCRIPTION_DETAIL | VARCHAR2 | 2000 |  |  | This column is for the additional details of any about the post-control record (like what tables are using it, etc) |
| TYPE_ATTR_1 | VARCHAR2 | 80 |  |  | This column is for the type attribute 1 |
| TYPE_ATTR_2 | VARCHAR2 | 80 |  |  | This column is for type attribute 2 |
| TYPE_ATTR_3 | VARCHAR2 | 80 |  |  | This column is for type attribute 3 |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CTL_RSLT_TYP_MAP_B_N1 | Non Unique | FUSION_TS_TX_DATA | TYPE_NAME |
| HWR_CTL_RSLT_TYP_MAP_B_U1 | Unique | FUSION_TS_TX_DATA | TYPE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
