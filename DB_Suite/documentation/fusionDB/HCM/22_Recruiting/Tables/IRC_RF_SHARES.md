# IRC_RF_SHARES

This table stores referral data for job shares.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrfshares-19741.html#ircrfshares-19741](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrfshares-19741.html#ircrfshares-19741)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RF_SHARES_PK | SHARE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SHARE_ID | NUMBER |  | 18 | Yes | Primary Key for this table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 | Yes | Stores REQUISITION_ID. Foreign key to IRC_REQUISITION_B table. |
| REFERRER_PERSON_ID | NUMBER |  | 18 | Yes | Stores PERSON_ID of the referrer. Foreign Key to PER_PERSONS table. |
| TARGET_CHANNEL_CODE | VARCHAR2 | 30 |  | Yes | Stores info on target channel where job is shared. (Email, OSN etc..). Stores the value as lookup code. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RF_SHARES_FK1 | Non Unique | Default | REQUISITION_ID |
| IRC_RF_SHARES_FK2 | Non Unique | Default | REFERRER_PERSON_ID |
| IRC_RF_SHARES_PK | Unique | Default | SHARE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
