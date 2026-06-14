# HRC_TXN_GROUPS

This table holds transaction group details

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxngroups-17503.html#hrctxngroups-17503](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxngroups-17503.html#hrctxngroups-17503)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_txn_groups_PK | GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GROUP_ID | NUMBER |  | 18 | Yes | Primary key and unique identifier |
| GROUP_OBJECT_ID | NUMBER |  | 18 | Yes | FK from consumer data model table |
| GROUP_NAME | VARCHAR2 | 300 |  | Yes | Descriptive group name for UI display if needed |
| GROUP_APPROVAL_QUOTA | NUMBER |  | 18 | Yes | Maximum count of approved transaction for group |
| GROUP_APPR_QUOTA_ADJUSTMENT | NUMBER |  | 18 |  | Internal column to indicate the count of additional transactions approved for the group beyond the group approval quota if group approval quota is dynamically reduced after group creation. Default value is 0. |
| TXN_GROUP_CUSTOM_VARCHAR_1 | VARCHAR2 | 200 |  |  | Future use char columns |
| TXN_GROUP_CUSTOM_VARCHAR_2 | VARCHAR2 | 200 |  |  | Future use char columns |
| TXN_GROUP_CUSTOM_VARCHAR_3 | VARCHAR2 | 200 |  |  | Future use char columns |
| TXN_GROUP_CUSTOM_VARCHAR_4 | VARCHAR2 | 200 |  |  | Future use char columns |
| TXN_GROUP_CUSTOM_NUMBER_1 | NUMBER |  | 18 |  | Future use number columns |
| TXN_GROUP_CUSTOM_NUMBER_2 | NUMBER |  | 18 |  | Future use number columns |
| TXN_GROUP_CUSTOM_NUMBER_3 | NUMBER |  | 18 |  | Future use number columns |
| TXN_GROUP_CUSTOM_NUMBER_4 | NUMBER |  | 18 |  | Future use number columns |
| TXN_GROUP_CUSTOM_DATE_1 | DATE |  |  |  | Future use date columns |
| TXN_GROUP_CUSTOM_DATE_2 | DATE |  |  |  | Future use date columns |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_GROUPS_FK | Unique | Default | GROUP_OBJECT_ID |
| HRC_TXN_GROUPS_PK | Unique | Default | GROUP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
