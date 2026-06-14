# CMP_MKT_SEGMENTS_TL

Translatino Table for CMP_MKT_SEGMENTS

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsegmentstl-17640.html#cmpmktsegmentstl-17640](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktsegmentstl-17640.html#cmpmktsegmentstl-17640)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_SEGMENTS_TL_PK | SEGMENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEGMENT_ID | NUMBER |  | 18 | Yes | Primary Table Key |
| SEGMENT_NAME | VARCHAR2 | 80 |  | Yes | Segment Name |
| SEGMENT_DESCR | VARCHAR2 | 2000 |  |  | Segment Description |
| MISC_TEXT_1 | VARCHAR2 | 300 |  |  | Miscellaneous Text 1 |
| MISC_TEXT_2 | VARCHAR2 | 300 |  |  | Miscellaneous Text 2 |
| MISC_TEXT_3 | VARCHAR2 | 300 |  |  | Miscellaneous Text 3 |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_SEGMENTS_TL_U1 | Unique | Default | SEGMENT_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
