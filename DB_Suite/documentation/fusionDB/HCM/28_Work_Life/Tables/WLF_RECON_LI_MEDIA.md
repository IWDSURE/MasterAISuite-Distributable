# WLF_RECON_LI_MEDIA

Table to store the snapshot of media available in Learning Item table and Akamai storage.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfreconlimedia-7600.html#wlfreconlimedia-7600](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfreconlimedia-7600.html#wlfreconlimedia-7600)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_RECON_LI_MEDIA_PK | RECON_LI_MEDIA_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RECON_LI_MEDIA_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | Identifier Id for Learning Item from table. |
| UUID | VARCHAR2 | 64 |  |  | UUID for Learning Item from table. |
| STORAGE_UUID | VARCHAR2 | 64 |  |  | UUID for media from Akamai storage. |
| JOB_RUN_ID | NUMBER |  | 18 | Yes | Id to identify which set of Learning Items and Akamai storeage media were processed during a given run. |
| JOB_RUN_DATE | DATE |  |  | Yes | Captures the date on which the job was run. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONTENT_MODIFIED_DATE | TIMESTAMP |  |  |  | The date on which content was last modified at Akamai net storage. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_RECON_LI_MEDIA_N1 | Non Unique | Default | UUID |
| WLF_RECON_LI_MEDIA_N2 | Non Unique | Default | STORAGE_UUID |
| WLF_RECON_LI_MEDIA_N3 | Non Unique | Default | JOB_RUN_ID |
| WLF_RECON_LI_MEDIA_N4 | Non Unique | Default | JOB_RUN_DATE |
| WLF_RECON_LI_MEDIA_U1 | Unique | Default | RECON_LI_MEDIA_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
