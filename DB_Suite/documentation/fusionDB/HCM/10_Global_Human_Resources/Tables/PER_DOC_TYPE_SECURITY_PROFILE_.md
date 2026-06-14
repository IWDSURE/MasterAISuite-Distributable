# PER_DOC_TYPE_SECURITY_PROFILE_

This table is contains the Document Type Security profiles created in the application.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecurityprofile-22512.html#perdoctypesecurityprofile-22512](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perdoctypesecurityprofile-22512.html#perdoctypesecurityprofile-22512)

## Primary Key

| Name | Columns |
|------|----------|
| PER_DOC_TYPE_SECURITY_PRO_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_TYPE_SECURITY_PROFILE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DOC_TYPE_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| VIEW_ALL | VARCHAR2 | 1 |  |  | When this is set to True, all document types become available when the document type security profile is applied. |
| NAME | VARCHAR2 | 240 |  |  | Defines the name for Security Profile |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to enable or disable the?document type security profile |
| INCLUDE_EXCLUDE_FLAG | VARCHAR2 | 1 |  |  | Indicates whether to include or exclude the associated document types in the document type security profile. |
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
| PER_DOC_TYPE_SECURITY_PRO_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DOC_TYPE_SECURITY_PROFILE_ID |
| PER_DOC_TYPE_SEC_PROFN1_ | Non Unique | Default | DOC_TYPE_SECURITY_PROFILE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
