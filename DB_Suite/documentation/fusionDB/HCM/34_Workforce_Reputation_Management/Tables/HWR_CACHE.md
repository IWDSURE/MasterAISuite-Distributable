# HWR_CACHE

This table contains the Sync Cache results for HWR application

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcache-31178.html#hwrcache-31178](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrcache-31178.html#hwrcache-31178)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_CACHE_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This column stored the ID for HWR Cache |
| DELTA_TIMESTAMP | TIMESTAMP |  |  | Yes | This column stored the Timestamp of the Delta for HWR Cache |
| NAME | VARCHAR2 | 200 |  | Yes | This column stored the Name for HWR Cache |
| DELTA | VARCHAR2 | 4000 |  |  | This column stored the Delta for HWR Cache |
| IS_FORCE_RELOAD | NUMBER |  |  |  | This column stored the Is Force Reload flag for HWR Cache |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_CACHE_U1 | Unique | Default | ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
