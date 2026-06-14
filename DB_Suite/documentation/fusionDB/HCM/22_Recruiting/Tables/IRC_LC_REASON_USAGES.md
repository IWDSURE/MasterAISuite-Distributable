# IRC_LC_REASON_USAGES

IRC_LC_REASON_USAGES: table used to link groups and reasons, so you have a group linking to many reasons.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasonusages-12389.html#irclcreasonusages-12389](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasonusages-12389.html#irclcreasonusages-12389)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_REASON_USAGES_PK | REASON_USAGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REASON_USAGE_ID | NUMBER |  | 18 | Yes | REASON USAGE ID: Defines the primary key for the table. |  |
| REASON_USAGE_CODE | VARCHAR2 | 256 |  |  | REASON USAGE CODE : Code used for the import/export, could be reason code + reason group code |  |
| REASON_GROUP_ID | NUMBER |  | 18 | Yes | REASON GROUP ID: Id of a reason group which uses some reasons |  |
| REASON_ID | NUMBER |  | 18 | Yes | REASON ID: if of the reason being used by a given group |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. | Obsolete |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LC_REASON_USAGES_N1 | Non Unique | Default | REASON_GROUP_ID |
| IRC_LC_REASON_USAGES_N2 | Non Unique | Default | REASON_ID |
| IRC_LC_REASON_USAGES_U1 | Unique | Default | REASON_USAGE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
