# IRC_GV_FIELDS_B

This table stores the fields which will be added as part of the grid view  for specific functional area.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvfieldsb-26178.html#ircgvfieldsb-26178](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgvfieldsb-26178.html#ircgvfieldsb-26178)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_GV_FIELDS_B_PK | FIELD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FIELD_ID | NUMBER |  | 18 | Yes | Primary key of table. System Generated. |
| FIELD_CODE | VARCHAR2 | 100 |  | Yes | Stores the code for the field. Field Code can be defined like this ORA_*CONTEXT*_FIELD. For example - Candidate Name Field for Job Application Context , the field code can be ORA_JA_CAND_NAME |
| CATEGORY_CODE | VARCHAR2 | 100 |  | Yes | Stores the information regarding which category the field points to. CATEGORIES can be ORA_EDUCATION , ORA_EXPERIENCE etc. |
| GV_CONTEXT_CODE | VARCHAR2 | 100 |  | Yes | Stores the information about the context for which the fields are being stored. For eg- For Job Applications Feature , this column value will be ORA_SUBMISSION and for Candidates  it will be ORA_CANDIDATE_SEARCH |
| FIELD_TYPE_CODE | VARCHAR2 | 100 |  |  | Stores the information about what type of field is being defined. For eg :- ORA_GENERAL , ORA_COMPOUND , ORA_EFF_GENERAL , ORA_EFF_COMPOUND |
| VO_ATTRIBUTE_PATH | VARCHAR2 | 512 |  |  | The full path of the View Object Attribute. Starting from the parent until the attribute. Each level denotes with a dot. For eg , to define degreeName :- SubmissionListVO.SubmissionEducationVO.degreeName |
| OSCS_ATTRIBUTE_PATH | VARCHAR2 | 512 |  |  | OSCS Index Path for the given field from the Index. Individual fields can be denoted with the index attribute name itself. For eg , if DegreeName needs to be used then this field will have "DegreeName" as a value.
If it is a Compound Field , then the parent node which has these fields would need to be provided. For eg :- if Education Compound Field needs to be denoted then :- JobApplicationEducation |
| DATA_TYPE | VARCHAR2 | 32 |  |  | Stores the data type of the field. The field data type can be - text , number and date |
| TRANSLATABLE_FLAG | VARCHAR2 | 1 |  |  | This column denotes whether the field is translatable in the OSCS Index or DB. If Y , then the field will be used as a translatable field and the corresponding translated values will be fetched from the destined source. If N , then the field will be considered as non-translatable. |
| MULTI_ROW_FLAG | VARCHAR2 | 1 |  |  | This column denotes whether the field is a multi row field or a single row  field. For eg :- Candidate Name is a single row field then the value of this column will be 'N'. But Degree Name is a multi row field , then the value of this column will be 'Y'. |
| DISPLAY_ROWS | NUMBER |  | 2 |  | This column denotes how many rows does user expect to see for this field. For eg :- If 3 is put in , then 3 rows will be shown to the user on the UI related to the given field. |
| HIDDEN_FLAG | VARCHAR2 | 1 |  |  | This column denotes whether the field needs to be hidden on the configuration screen or not. |
| CUSTOM_PROPERTIES | CLOB |  |  |  | This column will be used to store the custom properties of a field. For eg :- Storing Sort field etc. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_GV_FIELDS_B_PK | Unique | Default | FIELD_ID, ORA_SEED_SET1 |
| IRC_GV_FIELDS_B_PK1 | Unique | Default | FIELD_ID, ORA_SEED_SET2 |
| IRC_GV_FIELDS_B_U1 | Unique | Default | FIELD_CODE, ORA_SEED_SET1 |
| IRC_GV_FIELDS_B_U11 | Unique | Default | FIELD_CODE, ORA_SEED_SET2 |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
