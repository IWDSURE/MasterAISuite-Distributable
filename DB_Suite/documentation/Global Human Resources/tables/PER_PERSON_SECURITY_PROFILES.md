# PER_PERSON_SECURITY_PROFILES

Person Security Profile Table-Each Record stores conditions used to generate instance set based on  person related objects.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecurityprofiles-31134.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonsecurityprofiles-31134.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_SEC_PROFILE_PK | PERSON_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  | Yes | This option provides unrestricted security access to the specific person security profile. |
| NAME | VARCHAR2 | 240 |  | Yes | Name for the Person Security Profiles. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | This field represents whether a person security profile is enabled or disabled. When it is enabled, it can be associated with a role. |
| SECURE_BY_PERSON_TYPE | VARCHAR2 | 1 |  | Yes | This option allows users to select  different person types and select the security restrictions options, such as view all or restricted. |
| SECURE_BY_MGR_HIERARCHY | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profiles based on the manager hierarchy. |
| PRIMARY_ASSIGNMENT_ONLY | VARCHAR2 | 1 |  | Yes | The sub-ordinates of a manager hierarchy within a person security profile can be secured based on either Person or assignment. This options allows for primary assignment level restriction. |
| PERSON_OR_ASSIGNMENT_LEVEL | VARCHAR2 | 1 |  | Yes | The sub-ordinates of a manager hierarchy within a person security profile can be secured based on either Person or assignment. This options allows either person level or assignment level restriction. |
| MANAGER_TYPES | VARCHAR2 | 30 |  | Yes | When securing by manager hierarchy, this is the manager type option securing the person security profile. |
| MAX_LEVELS_IN_HIERARCHY | NUMBER |  |  |  | A positive integer indicating the level below the manager hierarchy up to which the sub-ordinates are secured. |
| SECURE_BY_DEPARTMENT | VARCHAR2 | 1 |  | Yes | This option allows users to restrict the person security profile based on a set of departments defined by an organization security profile. |
| DEPT_ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | The unique organization security profile used to identify the list of departments secured by the person security profile. |
| SECURE_BY_BUSINESS_UNIT | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profile access based on a list of business units from a selected organization security profile. |
| BU_ORG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | The unique organization security profile used to identify the list of business units secured by the person security profile. |
| SECURE_BY_LEGAL_EMPLOYER | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profile access based on a list of legal employers from a selected organization security profile. |
| SECURE_BY_POSITION | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profile access based on a list of positions from a selected position security profile. |
| POSITION_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_POSITION_SECURITY_PROFILES table. |
| SECURE_BY_PAYROLL | VARCHAR2 | 1 |  | Yes | This option allows user to restrict person types based on different payrolls in a payroll security profile |
| PAY_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PAY_PAY_SECURITY_PROFILES table. |
| SECURE_BY_JOB | VARCHAR2 | 1 |  | Yes | This option is not available.  Leave blank. |
| JOB_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_JOB_SECURITY_PROFILES table. |
| SECURE_BY_LOCATION | VARCHAR2 | 1 |  | Yes | This option is not available.  Leave blank. |
| LOCATION_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATION_SECURITY_PROFILES table. |
| SECURE_BY_LDG | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person types based on legislative data groups in a Legislative data group security profile. |
| LDG_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_LDG_SECURITY_PROFILES table. |
| SECURE_BY_GRADE | VARCHAR2 | 1 |  | Yes | This option is not available.  Leave blank. |
| GRADE_SECURITY_PROFILE_ID | NUMBER |  | 18 |  | Foreign Key to PER_GRADE_SECURITY_PROFILES table. |
| SECURE_BY_GLOBAL_NAME_RANGE | VARCHAR2 | 1 |  | Yes | You can restrict access to person records based on a person?s global list name. For example, the security profile could enable users to access persons whose global list names are in the range A through E. This field represents an option to secure based on global list names of employees. |
| GLOBAL_NAME_RANGE_START | VARCHAR2 | 30 |  |  | When restricting access based on a person's global list name, this field represents the starting point from which a user wants to restrict security based on names. |
| GLOBAL_NAME_RANGE_END | VARCHAR2 | 30 |  |  | When restricting access based on a person's global list name, this field represents the ending point from which a user wants to restrict security based on names. |
| SECURE_INDV_ASSIGNMENT | VARCHAR2 | 1 |  | Yes | This option is not available.  Leave blank. |
| SECURE_BY_CUSTOM_RESTRICTION | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profiles by their own specified criteria. |
| CUSTOM_RESTRICTION_TEXT | VARCHAR2 | 4000 |  |  | When securing by custom criteria, specify the SQL statement in this field. |
| ACCESS_TO_OWN_RECORD | VARCHAR2 | 1 |  | Yes | This option allows users access to their own records, those records belong to the instance set defined by the profile, regardless of whether they satisfy the other criteria in the profile. If users are denied access to their own records, then users are unable to access them even if they would otherwise belong to the instance set defined by the profile. |
| INCLUDE_RELATED_CONTACTS | VARCHAR2 | 1 |  | Yes | This option allows this person security profile the access to include person records belonging to the contacts of the people identified in the Person Security Profile.  If 'Include Related Contacts' is set to 'N' then profile will include people identified by other criteria defined in the profile.  If 'Include Related Contacts' is set to 'Y' then profile will include people identified by other criteria defined in the profile and the related contacts who are not workers. |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description for the person security profile. |
| SECURE_BY_AOR | VARCHAR2 | 1 |  | Yes | This option allows users to restrict person security profiles based on areas of responsibility. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LEG_EMP_ORG_SEC_PROFILE_ID | NUMBER |  | 18 |  | When securing by legal employer, this field contains the unique identifier for the selected organization security profile. |
| EVAL_MGR_HIERARCHY_FOR | VARCHAR2 | 30 |  | Yes | EVAL_MGR_HIERARCHY_FOR |
| INCLUDE_SHARED_PEOPLE_INFO | VARCHAR2 | 1 |  | Yes | This option allows the user to access shared people information. |
| INCLUDE_FUTURE_PERSONS | VARCHAR2 | 1 |  | Yes | This option allows users to configure future dated person access. |
| PURPOSE | VARCHAR2 | 30 |  | Yes | PURPOSE column for candidate security profile |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ASGS_TO_EVALUATE | VARCHAR2 | 30 |  |  | This option allows users to provide choice of
assignments to be considered while deriving secured access. |
| ACCESS_TO_CAND_WITH_OFFER | VARCHAR2 | 1 |  |  | This option allows users access to candidates for whom offer has been generated. This access is derived based on other criteria selected in the profile. |
| ENABLE_EXCLUSION | VARCHAR2 | 1 |  |  | Column to designate if exclusion configuration enabled on person security profile or not. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_SECURITY_PROFI_N20 | Non Unique | Default | SGUID |
| PER_PERSON_SEC_PROFILE_PK | Unique | FUSION_TS_TX_DATA | PERSON_SECURITY_PROFILE_ID, ORA_SEED_SET1 |
| PER_PERSON_SEC_PROFILE_PK1 | Unique | FUSION_TS_TX_DATA | PERSON_SECURITY_PROFILE_ID, ORA_SEED_SET2 |
| PER_PERSON_SEC_PROF_U1 | Unique | Default | UPPER("NAME"), ORA_SEED_SET1 |
| PER_PERSON_SEC_PROF_U11 | Unique | Default | UPPER("NAME"), ORA_SEED_SET2 |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
