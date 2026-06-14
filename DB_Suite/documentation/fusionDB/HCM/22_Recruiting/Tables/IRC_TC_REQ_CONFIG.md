# IRC_TC_REQ_CONFIG

This table contains the tax credits configuration data for requisitions.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcreqconfig-18272.html#irctcreqconfig-18272](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctcreqconfig-18272.html#irctcreqconfig-18272)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TC_REQ_CONFIG_PK | TC_REQ_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TC_REQ_CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_REQUISITIONS_B table. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS table. |
| ACCOUNT_USERNAME | VARCHAR2 | 100 |  | Yes | Partner account username to be used for the tax credits. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TC_REQ_CONFIG_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_TC_REQ_CONFIG_FK2 | Non Unique | Default | PROVISIONING_ID |
| IRC_TC_REQ_CONFIG_PK1 | Unique | Default | TC_REQ_CONFIG_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
