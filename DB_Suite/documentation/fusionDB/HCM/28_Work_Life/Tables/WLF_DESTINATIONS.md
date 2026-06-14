# WLF_DESTINATIONS

Table to store information of assignment destinations

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdestinations-13927.html#wlfdestinations-13927](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdestinations-13927.html#wlfdestinations-13927)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_destinations_PK | DESTINATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DESTINATION_ID | NUMBER |  | 18 | Yes | DESTINATION_ID |
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| ASSIGNED_TO_ID | NUMBER |  | 18 | Yes | ASSIGNED_TO_ID |
| ASSIGNED_TO_TYPE | VARCHAR2 | 30 |  | Yes | ASSIGNED_TO_TYPE |
| JOB_RUN_DATE | TIMESTAMP |  |  |  | JOB_RUN_DATE |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| wlf_destinations_N1 | Non Unique | Default | JOB_RUN_DATE |
| wlf_destinations_N2 | Non Unique | Default | ASSIGNED_TO_ID, ASSIGNED_TO_TYPE |
| wlf_destinations_U1 | Unique | Default | DESTINATION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
