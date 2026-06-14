# CMP_MKT_VND_LOC_MAP

Table used to store HR location mappings to Survey location mappings.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndlocmap-24253.html#cmpmktvndlocmap-24253](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndlocmap-24253.html#cmpmktvndlocmap-24253)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VND_LOC_MAP_PK | SURVEY_LOCATION_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SURVEY_LOCATION_MAP_ID | NUMBER |  | 18 | Yes | Key Field |
| SURVEY_LOCATION_ID | NUMBER |  | 18 | Yes | Survey Location Id |
| LOCATION_ID | NUMBER |  | 18 | Yes | HR Location Id |
| VENDOR_ID | NUMBER |  | 18 | Yes | Vendor Id |
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
| CMP_MKT_VND_LOC_MAP_N1 | Non Unique | DEFAULT | LOCATION_ID |
| CMP_MKT_VND_LOC_MAP_U1 | Unique | Default | SURVEY_LOCATION_MAP_ID |
| CMP_MKT_VND_LOC_MAP_U2 | Unique | Default | SURVEY_LOCATION_ID, LOCATION_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
