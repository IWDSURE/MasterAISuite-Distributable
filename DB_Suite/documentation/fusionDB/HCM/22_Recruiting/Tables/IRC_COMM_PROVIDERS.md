# IRC_COMM_PROVIDERS

This table stores different communication channels supported by Oracle Recruting.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccommproviders-23167.html#irccommproviders-23167](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccommproviders-23167.html#irccommproviders-23167)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_COMM_PROVIDERS_PK | COMM_PROVIDER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COMM_PROVIDER_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| CHANNEL_TYPE_CODE | VARCHAR2 | 40 |  | Yes | Unique code for the communication channel type.The corresponding lookup type is IRC_COMM_CHANNEL_TYPE. |
| NAME | VARCHAR2 | 240 |  | Yes | Name of the communication channel provider. |
| CODE | VARCHAR2 | 40 |  | Yes | Unique code for the communication channel provider. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | Description of the communication channel provider |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_COMM_PROVIDERS_PK | Unique | FUSION_TS_SEED | COMM_PROVIDER_ID, ORA_SEED_SET1 |
| IRC_COMM_PROVIDERS_PK1 | Unique | FUSION_TS_SEED | COMM_PROVIDER_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
