# HRT_ESTABLISHMENTS_TL

Profile Management Establishment translation table.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtestablishmentstl-29108.html#hrtestablishmentstl-29108](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtestablishmentstl-29108.html#hrtestablishmentstl-29108)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_ESTABLISHMENTS_TL_PK | ESTABLISHMENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ESTABLISHMENT_ID | NUMBER |  | 18 | Yes | Unique identifier of Establishment |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| NAME | VARCHAR2 | 240 |  | Yes | Maintains the name of an educational establishment |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the Establishment |
| LOCATION | VARCHAR2 | 240 |  |  | Holds the location details of an establishment |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_ESTABLISHMENTS_TL_PK | Unique | Default | ESTABLISHMENT_ID, LANGUAGE |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
