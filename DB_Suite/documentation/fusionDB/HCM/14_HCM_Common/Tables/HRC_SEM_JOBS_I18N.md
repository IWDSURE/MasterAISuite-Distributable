# HRC_SEM_JOBS_I18N

This table is to store job data which might be localized (NOT MLS).

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobsi18n-29285.html#hrcsemjobsi18n-29285](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemjobsi18n-29285.html#hrcsemjobsi18n-29285)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_JOBS_I18N_PK | JOB_I18N_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_I18N_ID | NUMBER |  | 18 | Yes | This is the primary column of the Jobs i18n table. |
| JOB_ID | NUMBER |  | 18 | Yes | This column contains the Job ID referenced to the Job table. |
| LANGUAGE_CODE | VARCHAR2 | 8 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| REQUISITION_TITLE | VARCHAR2 | 240 |  |  | This column contains the requisition title. |
| JOB_FAMILY_NAME | VARCHAR2 | 240 |  |  | This column contains the job family name. |
| JOB_FUNCTION_NAME | VARCHAR2 | 128 |  |  | This column contains the job function name. |
| ORGANIZATION_NAME | VARCHAR2 | 240 |  |  | This column contains the organization name. |
| SHORT_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the short description clob. |
| LONG_DESCRIPTION_CLOB | CLOB |  |  |  | This column contains the long description clob. |
| IS_ERROR | NUMBER |  | 8 |  | This column indicates if there is an error in the indexing event. |
| ERROR_MESSAGE | VARCHAR2 | 4000 |  |  | This column contains the error message of the indexing event. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_JOBS_I18N_U1 | Unique | FUSION_TS_TX_DATA | JOB_I18N_ID |
| HRC_SEM_JOBS_I18N_U2 | Unique | FUSION_TS_TX_DATA | JOB_ID, LANGUAGE_CODE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
