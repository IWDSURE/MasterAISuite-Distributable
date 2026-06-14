# IRC_RP_ACTIVATION_CONFIG

Stores the languages supported by third party resume parsers in Recruiting

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrpactivationconfig-26957.html#ircrpactivationconfig-26957](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrpactivationconfig-26957.html#ircrpactivationconfig-26957)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RP_ACTIVATION_CONFIG_PK | CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIG_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| PROVISIONING_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_TP_PARTNER_PROVISNGS |
| RP_LANGUAGE | VARCHAR2 | 4 |  |  | Indicates the code of the language that the third party resume parser supports |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Stores the code identifying the language status. The corresponding lookup type is ORA_IRC_RP_LANG_STATUS |
| TYPE | VARCHAR2 | 30 |  |  | Defines the type of config record. |
| DATACENTER_ID | VARCHAR2 | 100 |  |  | Stores the data center id of the resume parser partner |
| DATACENTER_NAME | VARCHAR2 | 250 |  |  | Store the datacenter name just for display as received from partner service. |
| BOOSTER_PARTNER_FLAG | VARCHAR2 | 1 |  |  | This indicate the provisioning is a booster provisioning. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_RP_ACTIVATION_CONFIG_FK1 | Non Unique | FUSION_TS_SEED | PROVISIONING_ID |
| IRC_RP_ACTIVATION_CONFIG_PK | Unique | FUSION_TS_SEED | CONFIG_ID, ORA_SEED_SET1 |
| IRC_RP_ACTIVATION_CONFIG_PK1 | Unique | FUSION_TS_SEED | CONFIG_ID, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
