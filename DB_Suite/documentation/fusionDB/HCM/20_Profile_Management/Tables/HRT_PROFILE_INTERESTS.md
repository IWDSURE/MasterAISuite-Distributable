# HRT_PROFILE_INTERESTS

This table is used to capture profile interests of employee. 
Interest lists enable employees to maintain a list of the non-person profiles that are of interest. The interest list can include any profile. 
For example, employees could add profiles for jobs that they want to include in their career planning, or job profiles that are similar to their own profile. Each employee has one interest list that can be modified by the employee, the employee's manager, and the profile administrator

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileinterests-14552.html#hrtprofileinterests-14552](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileinterests-14552.html#hrtprofileinterests-14552)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_INTERESTS_PK | PROFILE_INTEREST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_INTEREST_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F |
| PARTY_ID | NUMBER |  | 18 |  | Foreign Key to HZ_PARTIES |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Object type being bookmarked, like COMPETENCY, PROFILE |
| OBJECT_ID | NUMBER |  | 18 | Yes | Id of the Object type like ProfileId, ContentItemId |
| ASSIGNED_BY_PERSON_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_PEOPLE_F |
| COMMENTS | VARCHAR2 | 2000 |  |  | Comments for the Added Job |
| PRIVACY_CODE | VARCHAR2 | 30 |  | Yes | PRIVACY_CODE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| INTEREST_STATUS | VARCHAR2 | 1 |  |  | INTEREST_STATUS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_INTERESTS_N1 | Non Unique | Default | PERSON_ID, OBJECT_TYPE, OBJECT_ID |
| HRT_PROFILE_INTERESTS_PK | Unique | Default | PROFILE_INTEREST_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
