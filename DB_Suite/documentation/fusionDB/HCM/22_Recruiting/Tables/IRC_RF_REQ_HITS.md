# IRC_RF_REQ_HITS

This table stores audit information when a requisition is viewed (through referral links).

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrfreqhits-10096.html#ircrfreqhits-10096](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrfreqhits-10096.html#ircrfreqhits-10096)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RF_JOB_HITS_PK | REQ_HIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_HIT_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Stores REQUISITION_ID. Foreign Key to IRC_REQUISITIONS_B table. |
| REFERRAL_ID | NUMBER |  | 18 |  | Stores REFERRAL_ID. Foreign Key to IRC_RF_REFERRALS table. |
| SHARE_ID | NUMBER |  | 18 |  | Stores SHARE_ID. Foreign Key to IRC_RF_SHARES table. |
| SOURCE | VARCHAR2 | 512 |  |  | Stores source information from where referral link is clicked from. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RF_REQ_HITS_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_RF_REQ_HITS_FK2 | Non Unique | Default | REFERRAL_ID |
| IRC_RF_REQ_HITS_FK3 | Non Unique | Default | SHARE_ID |
| IRC_RF_REQ_HITS_PK | Unique | Default | REQ_HIT_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
