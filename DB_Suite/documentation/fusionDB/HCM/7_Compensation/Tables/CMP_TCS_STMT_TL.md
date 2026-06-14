# CMP_TCS_STMT_TL

Setup Translatable Table that stores the statement definition. Captures the Eligibility Profile, Summary page description details and the additional information details, latest date on which statement is generated using the setup

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmttl-29324.html#cmptcsstmttl-29324](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmttl-29324.html#cmptcsstmttl-29324)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_STMT_TL_PK | STMT_ID, LANGUAGE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_ID | NUMBER |  | 18 | Yes | STMT_ID |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| DESCRIPTION | VARCHAR2 | 2000 |  |  | DESCRIPTION |
| SMRY_DESC_TXT | CLOB |  |  |  | SMRY_DESC_TXT |
| SMRY_ADDL_INFO | CLOB |  |  |  | SMRY_ADDL_INFO |
| SMRY_ADDL_INFO_TITLE | VARCHAR2 | 240 |  |  | SMRY_ADDL_INFO_TITLE |
| SMRY_TITLE | VARCHAR2 | 240 |  |  | SMRY_TITLE |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_STMT_TL_N1 | Non Unique | Default | UPPER("NAME") |
| CMP_TCS_STMT_TL_UK1 | Unique | FUSION_TS_TX_DATA | STMT_ID, LANGUAGE, BUSINESS_GROUP_ID |
| CMP_TCS_STMT_TL_UK2 | Unique | FUSION_TS_TX_DATA | NAME, LANGUAGE, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
