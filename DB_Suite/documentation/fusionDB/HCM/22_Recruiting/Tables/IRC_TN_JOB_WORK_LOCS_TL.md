# IRC_TN_JOB_WORK_LOCS_TL

Table for storing the flattened work location information of the requisition.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobworklocstl-25589.html#irctnjobworklocstl-25589](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnjobworklocstl-25589.html#irctnjobworklocstl-25589)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_TN_JOB_WORK_LOCS_TL_PK | TN_JOB_WORK_LOC_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TN_JOB_WORK_LOC_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| FA_LOCATION_NAME | VARCHAR2 | 240 |  | Yes | Concatenation of Location Name & Alternate Location Code. |
| FULL_LOCATION_ADDRESS | VARCHAR2 | 4000 |  |  | Full address which includes columns ADDRESS_LINE_1,ADDRESS_LINE_2,ADDRESS_LINE_3,ADDRESS_LINE_4,BUILDING,TOWN_OR_CITY,POSTAL_CODE,COUNTRY,REGION_1,REGION_2,REGION_3. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_TN_JOB_WORK_LOCS_TL_PK | Unique | Default | TN_JOB_WORK_LOC_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
