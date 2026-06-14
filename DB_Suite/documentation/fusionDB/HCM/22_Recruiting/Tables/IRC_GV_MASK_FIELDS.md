# IRC_GV_MASK_FIELDS

This table is created to save the information of the fields to be masked.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvmaskfields-30429.html#ircgvmaskfields-30429](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvmaskfields-30429.html#ircgvmaskfields-30429)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_MASK_FIELDS_PK | MASK_FIELD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASK_FIELD_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| GV_CONTEXT_CODE | VARCHAR2 | 100 |  | Yes | Stores the context code for which all the views will be stored. For example : Context can be ORA_SUBMISSION and all the fields related to Job Application would be specified with this context code. |
| FIELD_CODE | VARCHAR2 | 100 |  | Yes | Stores the code for the field. Field Code can be defined like this ORA_*CONTEXT*_FIELD. For example - Candidate Name Field for Job Application Context , the field code can be ORA_JA_CAND_NAME |
| FIELD_TYPE_CODE | VARCHAR2 | 100 |  |  | Stores the information about what type of field is being defined. For eg :- ORA_GENERAL , ORA_COMPOUND , ORA_EFF_GENERAL , ORA_EFF_COMPOUND |
| FLEX_SEGMENT_CODE | VARCHAR2 | 100 |  |  | Stores the segment code of the flex field. |
| FLEX_CONTEXT_CODE | VARCHAR2 | 100 |  |  | Stores the context code of the flex field. |
| PROFILE_CONTENT_SECTION_ID | NUMBER |  | 18 |  | This column stores the Section Id for a given category. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GV_MASK_FIELDS_PK | Unique | Default | MASK_FIELD_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
