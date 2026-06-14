# HRT_PROFILE_IMPORTS

This table is to store the data retrieved from third party provider like linkedin

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileimports-22703.html#hrtprofileimports-22703](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofileimports-22703.html#hrtprofileimports-22703)

## Primary Key

| Name | Columns |
|------|----------|
| hrt_profile_imports_PK | PROFILE_IMPORT_ID, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_IMPORT_ID | NUMBER |  | 18 | Yes | Profile Import Id |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| INTEGRATION_SOURCE | VARCHAR2 | 4 |  | Yes | Integration Source |
| PROFILE_ID | NUMBER |  | 18 | Yes | Profile Id |
| PROFILE_DATA | CLOB |  |  |  | Profile Data |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | Error Message |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| hrt_profile_imports_U1 | Unique | Default | PROFILE_IMPORT_ID, BUSINESS_GROUP_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
