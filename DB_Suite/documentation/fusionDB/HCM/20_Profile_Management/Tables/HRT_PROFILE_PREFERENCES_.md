# HRT_PROFILE_PREFERENCES_

This table is created to store profile preferences data

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilepreferences-14920.html#hrtprofilepreferences-14920](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilepreferences-14920.html#hrtprofilepreferences-14920)

## Primary Key

| Name | Columns |
|------|----------|
| hrt_profile_preferences_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, PROFILE_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_PREFERENCE_ID | NUMBER |  | 18 | Yes | PROFILE_PREFERENCE_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Business Group ID |
| SECTION_ID | NUMBER |  | 18 |  | Section Id |
| PROFILE_ID | NUMBER |  | 18 |  | Profile Id |
| CONTENT_TYPE_ID | NUMBER |  | 18 |  | Content Type Id |
| PARENT_PREF_ID | NUMBER |  | 18 |  | Parent Preference Id |
| OBJECT_TYPE | VARCHAR2 | 240 |  |  | Object Type |
| OBJECT_ID | NUMBER |  | 18 |  | Object ID |
| OBJECT_CODE | VARCHAR2 | 240 |  |  | Object Code |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Original Impersonator User. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_PREFERENCESN1_ | Non Unique | Default | PROFILE_PREFERENCE_ID |
| HRT_PROFILE_PREFERENCESU1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, PROFILE_PREFERENCE_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
