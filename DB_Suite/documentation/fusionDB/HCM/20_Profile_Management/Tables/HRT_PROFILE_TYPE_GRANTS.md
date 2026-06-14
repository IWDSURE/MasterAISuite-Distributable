# HRT_PROFILE_TYPE_GRANTS

Profile Type Grants is the table to store information about the roles that are given access to different content sections.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypegrants-23667.html#hrtprofiletypegrants-23667](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofiletypegrants-23667.html#hrtprofiletypegrants-23667)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_TYPE_GRANTS_PK | PROFILE_TYPE_GRANT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_TYPE_GRANT_ID | NUMBER |  | 18 | Yes | Profile Type Grant ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group ID. Foreign key to HRT_PROFILE_TYP_SECTIONS. |
| SECTION_ID | NUMBER |  | 18 | Yes | Section ID. Foreign key to HRT_PROFILE_TYP_SECTIONS. |
| ROLE_ID | NUMBER |  | 18 |  | Role ID. Foreign key to PER_ROLES_DN. |
| SECURITY_MODIFY_FLAG | VARCHAR2 | 30 |  |  | Security Modify Flag to determine Manage Access for the Role Code on Content Section. |
| SECURITY_VIEW_FLAG | VARCHAR2 | 30 |  |  | Security View Flag to determine View Access for the Role Code on Content Section. |
| SECURITY_REPORT_FLAG | VARCHAR2 | 30 |  |  | Security Report Flag to determine Report Access for the Role Code on Content Section. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_TYPE_GRANTS_N1 | Non Unique | Default | SECTION_ID, BUSINESS_GROUP_ID |
| HRT_PROFILE_TYPE_GRANTS_U1 | Unique | Default | PROFILE_TYPE_GRANT_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
