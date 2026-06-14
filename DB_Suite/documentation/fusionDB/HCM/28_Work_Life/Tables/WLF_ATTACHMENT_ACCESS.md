# WLF_ATTACHMENT_ACCESS

This table stores the relation between assignments and attachments where each row defines the visibility or audience to access the attachments.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattachmentaccess-22182.html#wlfattachmentaccess-22182](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfattachmentaccess-22182.html#wlfattachmentaccess-22182)

## Primary Key

| Name | Columns |
|------|----------|
| wlf_attachment_access_PK | ATTACHMENT_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTACHMENT_ACCESS_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| VISIBILITY_TYPE | VARCHAR2 | 80 |  |  | Visibility Type |
| SOURCE_ID | NUMBER |  | 18 |  | Reference to source id : learning_item_id or assignment id etc |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Source type. |
| SOURCE_INFO | VARCHAR2 | 150 |  |  | SOURCE_INFO |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. 
Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_ATTACHMENT_ACCESS_N1 | Non Unique | Default | SOURCE_ID |
| WLF_ATTACHMENT_ACCESS_N2 | Non Unique | Default | VISIBILITY_TYPE, SOURCE_ID |
| wlf_attachment_access_U1 | Unique | Default | ATTACHMENT_ACCESS_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
