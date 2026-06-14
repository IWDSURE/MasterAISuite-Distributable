# IRC_LC_REASON_GROUPS_B

IRC_LC_REASON_GROUPS_B: Represents a group of reasons, basically the group is like a bag for the reasons.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasongroupsb-8276.html#irclcreasongroupsb-8276](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclcreasongroupsb-8276.html#irclcreasongroupsb-8276)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LC_REASON_GROUPS_B_PK | REASON_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| REASON_GROUP_ID | NUMBER |  | 18 | Yes | REASON GROUP ID: Primary key of the table. System generated. |  |
| REASON_GROUP_CODE | VARCHAR2 | 30 |  | Yes | Stores the code for this phase. |  |
| REASON_GROUP_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the status code of the reason group. |  |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. | Obsolete |
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
| IRC_LC_REASON_GROUPS_B_U1 | Unique | Default | REASON_GROUP_ID |
| IRC_LC_REASON_GROUPS_B_U2 | Unique | Default | REASON_GROUP_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
