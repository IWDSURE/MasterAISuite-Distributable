# PER_LOCATION_DETAILS_F_TL_

PER_LOCATION_DETAILS_F_TL stores the translated attributes of the base table PER_LOCATION_DETAILS_F

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsftl-8309.html#perlocationdetailsftl-8309](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocationdetailsftl-8309.html#perlocationdetailsftl-8309)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOCATION_DETAILS_TL_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOCATION_DETAILS_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LOCATION_CODE | VARCHAR2 | 60 |  |  | Name of the location |
| LOCATION_NAME | VARCHAR2 | 240 |  |  | Concatenation of Location Name and Alternate Location Code |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description for the location. |
| SOURCE_LANG | VARCHAR2 | 4 |  |  | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| AC_LOCATION_CODE | VARCHAR2 | 60 |  |  | Alternate Location Code of the Location |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LOCATION_DETAILS_F_N1_ | Non Unique | Default | LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |
| PER_LOCATION_DETAILS_TL_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_DETAILS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
