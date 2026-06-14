# BEN_CTFN_DOC_MAP

BEN_CTFN_DOC_MAP is a mapping table between certification type and Document Type. This mapping is allowed at two levels(Program or PNIP)

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benctfndocmap-8387.html#benctfndocmap-8387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benctfndocmap-8387.html#benctfndocmap-8387)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CTFN_DOC_MAP_PK | CTFN_DOC_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CTFN_DOC_MAP_ID | NUMBER |  | 18 | Yes | System generated primary key column |
| MAPPING_TABLE_NAME | VARCHAR2 | 30 |  | Yes | Name of the table for which the document setup has been done |
| MAPPING_COLUMN_NAME | VARCHAR2 | 30 |  | Yes | Mapping Table Column Name |
| MAPPING_TABLE_PK_ID | NUMBER |  | 18 | Yes | Mapping table primary key id |
| CTFN_TYPE_CD | VARCHAR2 | 30 |  | Yes | The certification type |
| VALIDITY_CD | VARCHAR2 | 30 |  |  | Code which determines the validity time of the document |
| VALIDITY_TM_NUM | NUMBER |  | 18 |  | This determines the time period for which the document will be valid. This will be blank when the Validity_cd is 'Lifetime' |
| APPROVAL_PERD_CD | VARCHAR2 | 30 |  |  | Code which determines the time for which the approval is valid |
| APPROVAL_PERD_TM_NUM | NUMBER |  | 18 |  | This determines the time period for which the approval will be valid. |
| DOCUMENT_TYPE_ID | NUMBER |  | 18 |  | Foreign Key to hr_document_types_b |
| VERIFICATION_MODE | VARCHAR2 | 30 |  |  | This specifies whether a manual approval from admin is needed or the document will be auto approved |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Description |
| START_DATE | DATE |  |  |  | Start Date |
| END_DATE | DATE |  |  |  | End Date |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | Active FLag |
| DOC_USG_CD | VARCHAR2 | 30 |  |  | This value differentiates whether the row was created as part of Certification Process or as part of Record Life Event |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CONFIG_ID_1 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_2 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_3 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_4 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_ID_5 | NUMBER |  | 18 |  | Template ID field for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template character field for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date field for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date field for future use. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number field for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number field for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CTFN_DOC_MAP_PK | Unique | Default | CTFN_DOC_MAP_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
