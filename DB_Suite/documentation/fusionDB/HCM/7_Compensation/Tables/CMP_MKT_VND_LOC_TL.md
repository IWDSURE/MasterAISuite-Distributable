# CMP_MKT_VND_LOC_TL

Translate Table for Supplier Locations

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndloctl-24675.html#cmpmktvndloctl-24675](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndloctl-24675.html#cmpmktvndloctl-24675)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VND_LOC_TL_PK | SURVEY_LOCATION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_LOCATION_ID | NUMBER |  | 18 | Yes | Primary Key |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| SURVEY_LOCATION_NAME | VARCHAR2 | 80 |  | Yes | Survey Location Name |
| MISC_TEXT_1 | VARCHAR2 | 300 |  |  | Miscelaneous Text 1 |
| MISC_TEXT_2 | VARCHAR2 | 300 |  |  | Miscelaneous Text 2 |
| MISC_TEXT_3 | VARCHAR2 | 300 |  |  | Miscelaneous Text 3 |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_VND_LOC_TL_U1 | Unique | Default | SURVEY_LOCATION_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
