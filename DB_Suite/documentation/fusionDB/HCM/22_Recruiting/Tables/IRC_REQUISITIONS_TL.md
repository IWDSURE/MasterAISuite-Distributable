# IRC_REQUISITIONS_TL

Translation table for Requisition details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionstl-26662.html#ircrequisitionstl-26662](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionstl-26662.html#ircrequisitionstl-26662)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQUISITIONS_TL_PK | REQUISITION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUISITION_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. Foreign key to IRC_REQUISITIONS_B table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| TITLE | VARCHAR2 | 240 |  |  | Stores the Title for this Requisition. This is the title that is published to external/internal candidates. |
| MANAGER_TITLE | VARCHAR2 | 240 |  |  | Stores the Manager Title for this Requisition. This title is only used internally by the hiring manager, it is not meant to be published to external/internal candidates. |
| EXTERNAL_DESC | CLOB |  |  |  | Stores the html-free version of the External Description for this Requisition. |
| EXTERNAL_DESC_HTML | CLOB |  |  |  | Stores the html version of the External Description for this Requisition. |
| INTERNAL_DESC | CLOB |  |  |  | Stores the html-free version of the Internal Description for this Requisition. |
| INTERNAL_DESC_HTML | CLOB |  |  |  | Stores the html version of the Internal Description for this Requisition. |
| EXTERNAL_SHORT_DESC | CLOB |  |  |  | Stores the External Short Description for this Requisition. |
| INTERNAL_SHORT_DESC | CLOB |  |  |  | Stores the Internal Short Description for this Requisition. |
| EXTERNAL_RESP | CLOB |  |  |  | Stores the html-free version of the External Responsibilities for this Requisition. |
| EXTERNAL_RESP_HTML | CLOB |  |  |  | Stores the html version of the External Responsibilities for this Requisition. |
| INTERNAL_RESP | CLOB |  |  |  | Stores the html-free version of the Internal Responsibilities for this Requisition. |
| INTERNAL_RESP_HTML | CLOB |  |  |  | Stores the html version of the Internal Responsibilities for this Requisition. |
| EXTERNAL_QUAL | CLOB |  |  |  | Stores the html-free version of the External Qualifications for this Requisition. |
| EXTERNAL_QUAL_HTML | CLOB |  |  |  | Stores the html version of the External Qualifications for this Requisition. |
| INTERNAL_QUAL | CLOB |  |  |  | Stores the html-free version of the Internal Qualifications for this Requisition. |
| INTERNAL_QUAL_HTML | CLOB |  |  |  | Stores the html version of the Internal Qualifications for this Requisition. |
| NAME | VARCHAR2 | 240 |  |  | This name is only used internally as the identifier.  This is not unique.  It is not meant to be published to external/internal candidates. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQUISITIONS_TL_PK | Unique | Default | REQUISITION_ID, LANGUAGE |
| IRC_REQUISITIONS_TL_U1 | Unique | Default | REQUISITION_ID, LANGUAGE, TITLE |
| IRC_REQUISITIONS_TL_U2 | Unique | IRC_REQUISITIONS_TL_U2 | REQUISITION_ID, LANGUAGE, TITLE, MANAGER_TITLE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
