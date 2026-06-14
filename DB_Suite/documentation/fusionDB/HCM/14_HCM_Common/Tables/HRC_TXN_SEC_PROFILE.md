# HRC_TXN_SEC_PROFILE

Transaction Console Security Profile table: The top level record identifying each security profile uniquely is saved here.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofile-28914.html#hrctxnsecprofile-28914](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnsecprofile-28914.html#hrctxnsecprofile-28914)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_TXN_SEC_PROFILE_PK | TXN_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TXN_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | The primary key to the current table. |
| NAME | VARCHAR2 | 240 |  | Yes | This column holds the name of the Security Profile. |
| VIEW_ALL | VARCHAR2 | 1 |  |  | Flag to indicate if view privilege is granted to all or not. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Flag to indicate if security profile is enabled or not. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Provide the details about the Security Profile. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_TXN_SEC_PROFILE_N20 | Non Unique | Default | SGUID |
| HRC_TXN_SEC_PROFILE_U1 | Unique | Default | TXN_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| HRC_TXN_SEC_PROFILE_U11 | Unique | Default | TXN_SECURITY_PROFILE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
