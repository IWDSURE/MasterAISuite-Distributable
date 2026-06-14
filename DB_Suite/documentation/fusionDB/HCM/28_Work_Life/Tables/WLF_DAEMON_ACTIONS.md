# WLF_DAEMON_ACTIONS

Table to store daemon action details

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdaemonactions-16053.html#wlfdaemonactions-16053](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfdaemonactions-16053.html#wlfdaemonactions-16053)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_DAEMON_ACTIONS_PK | ACTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACTION_ID | NUMBER |  | 18 | Yes | ACTION_ID |
| ACTION_TYPE | VARCHAR2 | 20 |  | Yes | ACTION_TYPE |
| ACTION_NAME | VARCHAR2 | 30 |  |  | ACTION_NAME |
| ACTION_USER | VARCHAR2 | 30 |  |  | ACTION_USER |
| ACTION_START_DATE | TIMESTAMP |  |  |  | ACTION_START_DATE |
| ACTION_INPUT | CLOB |  |  |  | ACTION_INPUT |
| ACTION_OUTPUT | CLOB |  |  |  | ACTION_OUTPUT |
| PRIORITY | NUMBER |  |  |  | PRIORITY |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| PARENT_ACTION_ID | NUMBER |  | 18 |  | PARENT_ACTION_ID |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_DAEMON_ACTIONS_N1 | Non Unique | WLF_DAEMON_ACTIONS_N1 | ACTION_TYPE, PRIORITY, CREATION_DATE |
| WLF_DAEMON_ACTIONS_U1 | Unique | WLF_DAEMON_ACTIONS_U1 | ACTION_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
