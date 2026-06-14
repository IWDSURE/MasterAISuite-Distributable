# PAY_FLW_SECURITY_PROFILES_

This table holds information of flow security profiles.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflwsecurityprofiles-4573.html#payflwsecurityprofiles-4573](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payflwsecurityprofiles-4573.html#payflwsecurityprofiles-4573)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_FLW_SECURITY_PROFILES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, FLW_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLW_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | FLW_SECURITY_PROFILE_ID |
| VIEW_ALL | VARCHAR2 | 1 |  |  | VIEW_ALL |
| NAME | VARCHAR2 | 240 |  |  | NAME |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | BUSINESS_GROUP_ID |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | ENABLED_FLAG |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_FLW_SECURITY_PROFILES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, FLW_SECURITY_PROFILE_ID |
| PAY_FLW_SECURITY_PROFN1_ | Non Unique | Default | FLW_SECURITY_PROFILE_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
