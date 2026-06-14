# IRC_REQ_SEC_PROFILES

Requisition Security Profile table - Each record stores conditions used to generate instance set based on requisition related objects.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqsecprofiles-16546.html#ircreqsecprofiles-16546](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqsecprofiles-16546.html#ircreqsecprofiles-16546)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQ_SECURITY_PROFILES_PK | REQ_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| NAME | VARCHAR2 | 240 |  | Yes | Name for the requisition security profile. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether a requisition security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| SECURE_BY_ORGANIZATION_FLAG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict requisition security profile access based on organization. |
| SECURE_BY_LOCATION_FLAG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict requisition security profile access based on location. |
| SECURE_BY_JOB_FAMILY_FLAG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict requisition security profile access based on job family. |
| SECURE_BY_JOB_FUNCTION_FLAG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict requisition security profile access based on job function. |
| SECURE_BY_REC_TYPE_FLAG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict requisition security profile access based on recruitment type. |
| SECURE_BY_AOR_FLAG | VARCHAR2 | 1 |  |  | This option allows users to restrict requisition security profiles based on areas of responsibility. |
| SECURE_BY_TM_TYPE_FLAG | VARCHAR2 | 1 |  |  | This option allows users to restrict requisition security profiles based on team member type. |
| ACCESS_SUBORDINATE_REQ_FLAG | VARCHAR2 | 1 |  |  | This option allows users to access requisition seen by the subordinates |
| RESPONSIBILITY_TYPE | VARCHAR2 | 30 |  |  | Responsibility type for areas of responsibility. |
| VIEW_ALL_FLAG | VARCHAR2 | 1 |  | Yes | This option provides unrestricted security access to the specific requisition security profile. |
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
| IRC_REQ_SECURITY_PROFILE_PK | Unique | FUSION_TS_SEED | REQ_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| IRC_REQ_SECURITY_PROFILE_PK1 | Unique | FUSION_TS_SEED | REQ_SECURITY_PROFILE_ID, ORA_SEED_SET2 |
| IRC_REQ_SECURITY_PROFILE_U1 | Unique | FUSION_TS_SEED | UPPER("NAME"), ORA_SEED_SET1 |
| IRC_REQ_SECURITY_PROFILE_U11 | Unique | FUSION_TS_SEED | UPPER("NAME"), ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
