# HRT_PROFILES_B_BK

Backup table for HRT_PROFILES_B

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesbbk-19151.html#hrtprofilesbbk-19151](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilesbbk-19151.html#hrtprofilesbbk-19151)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILES_B_BK_PK | INSTANCE_ID, PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_ID | NUMBER |  | 18 | Yes | Instance Id |
| PROFILE_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_TYPE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILE_TYPES_B |
| PROFILE_CODE | VARCHAR2 | 30 |  | Yes | Unique code which identifies the profile |
| PROFILE_STATUS_CODE | VARCHAR2 | 30 |  | Yes | Status Code if the profile is active or inactive |
| PROFILE_USAGE_CODE | VARCHAR2 | 256 |  | Yes | Usage code which identifies it is used for Person profile or Model profile |
| PERSON_ID | NUMBER |  | 18 |  | Foreign Key to PER_ALL_PEOPLE_F |
| PARTY_ID | NUMBER |  | 18 |  | Foreign Key to HZ_PARTIES |
| OWNER_PERSON_ID | NUMBER |  | 18 |  | Owner person id |
| CAREER_AMBASSADOR_FLAG | VARCHAR2 | 30 |  |  | CAREER_AMBASSADOR_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILES_B_BK_PK | Unique | Default | INSTANCE_ID, PROFILE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
