# PER_COUNTRY_SECURITY_PROFILES_

Country Security Profiles Table.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecurityprofiles-21613.html#percountrysecurityprofiles-21613](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/percountrysecurityprofiles-21613.html#percountrysecurityprofiles-21613)

## Primary Key

| Name | Columns |
|------|----------|
| PER_COUNTRY_SEC_PROFILES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, COUNTRY_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COUNTRY_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  |  | This option provides unrestricted security access to the specific country security profile. |
| NAME | VARCHAR2 | 240 |  |  | Denotes the name for Country Security Profile. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | This field represents whether a country security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CNTRY_SEC_PROFILESN1_ | Non Unique | Default | COUNTRY_SECURITY_PROFILE_ID |
| PER_COUNTRY_SEC_PROFILES_PK_ | Unique | FUSION_TS_TX_DATA | LAST_UPDATE_DATE, LAST_UPDATED_BY, COUNTRY_SECURITY_PROFILE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
