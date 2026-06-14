# HRC_TXN_BPEL_NTF

hrc_txn_bpel_ntf table: This table stores the values which are populated for BPEL Notifications. Values are expected to get synced regularly through ess job from the BPELNotificationSec view.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** HRC_TXN_BPEL_NTF

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnbpelntf-27679.html#hrctxnbpelntf-27679](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnbpelntf-27679.html#hrctxnbpelntf-27679)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_BPEL_NTF_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | VARCHAR2 | 200 |  | Yes | This coloumn reveals the id of the BPEL notification table |
| TYPE | VARCHAR2 | 100 |  |  | The type of the notification |
| TRANSACTION_ID | NUMBER |  | 18 |  | Transaction ID associated with the notification |
| STATUS | VARCHAR2 | 200 |  |  | The status of the notification |
| COMPONENT_NAME | VARCHAR2 | 200 |  |  | This coloumn reveals to which process this coloumn belongs to |
| DESTINATIONADDRESS | VARCHAR2 | 2000 |  |  | Addess at which notification is received |
| WFTASKID | VARCHAR2 | 200 |  |  | This is the task id of coloumn |
| WFTASKVERSION | NUMBER |  | 38 |  | This is the task version id of the coloumn |
| NTF_CREATEDTIME | DATE |  |  | Yes | The time at which notification is triggered |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| IS_PROCESSED | VARCHAR2 | 2 |  |  | This coloumn reveals whether this has already been processed or not |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_BPEL_NTF_PK1 | Unique | HRC_TXN_BPEL_NTF_PK1 | ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
