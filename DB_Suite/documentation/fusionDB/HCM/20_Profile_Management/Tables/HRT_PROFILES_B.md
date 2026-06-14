# HRT_PROFILES_B

This is core  table contains the person profile or model profile.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesb-24973.html#hrtprofilesb-24973](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesb-24973.html#hrtprofilesb-24973)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILES_B_PK | PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILE_TYPES_B |
| PROFILE_CODE | VARCHAR2 | 30 |  | Yes | Unique code which identifies the profile |
| PROFILE_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Status Code if the profile is active or inactive |
| PROFILE_USAGE_CODE | VARCHAR2 | 256 |  | Yes | Usage code which identifies it is used for Person profile or Model profile |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_PEOPLE_F |
| PARTY_ID | NUMBER |  | 18 |  | Foreign Key to HZ_PARTIES |
| OWNER_PERSON_ID | NUMBER |  | 18 |  | Owner person id |
| CAREER_AMBASSADOR_FLAG | VARCHAR2 | 30 |  |  | Career Ambassador Flag |
| REVIEW_REQD_FLAG | VARCHAR2 | 30 |  |  | Review Required Flag |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRT_PROFILES_B_N1 | Non Unique | Default | PERSON_ID | Obsolete |
| HRT_PROFILES_B_N2 | Non Unique | Default | PARTY_ID |  |
| HRT_PROFILES_B_N3 | Non Unique | Default | PROFILE_USAGE_CODE |  |
| HRT_PROFILES_B_N4 | Non Unique | Default | BUSINESS_GROUP_ID, PROFILE_CODE |  |
| HRT_PROFILES_B_PK | Unique | Default | PROFILE_ID |  |
| HRT_PROFILES_B_U1 | Unique | Default | PERSON_ID, PROFILE_ID, PROFILE_STATUS_CODE |  |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
