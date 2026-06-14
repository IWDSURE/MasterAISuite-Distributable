# BEN_SS_CONFIGURATION

BEN_SS_CONFIGURATION identifies the self service configuration settings related to benefits spaces, self-service effective date, primary care physician, parameter region, enrollments region, confirmation region and unrestricted processing which are applied across a business group.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benssconfiguration-16872.html#benssconfiguration-16872](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benssconfiguration-16872.html#benssconfiguration-16872)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_SS_CONFIGURATION_PK | SS_CONFIG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SS_CONFIG_ID | NUMBER |  | 18 | Yes | THIS COLUMN FIELD IS USED FOR S_CONFIG_ID |
| DISP_PARAM_FLAG | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DISP_PARAM_FLAG |
| DISP_SIGN_REGION | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DISP_SIGN_REGION |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | THIS COLUMN FIELD IS USED FOR BUSINESS_GROUP_ID |
| SS_DATE_TO_USE | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR SS_DATE_TO_USE |
| DISP_GRP_SPACE | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DISP_GRP_SPACE |
| GRP_SPACE_NAME | VARCHAR2 | 200 |  |  | THIS COLUMN FIELD IS USED FOR GRP_SPACE_NAME |
| GRP_SPACE_DESC | VARCHAR2 | 600 |  |  | THIS COLUMN FIELD IS USED FOR GRP_SPACE_DESC |
| ALLOW_SS_UNRST_PROCG_CD | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR ALLOW_SS_UNRST_PROCG_CD |
| DISP_SS_PCP_REGION | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DISP_SS_PCP_REGION |
| DFLT_SS_OVERVIEW_REGION | VARCHAR2 | 30 |  | Yes | THIS COLUMN FIELD IS USED FOR DFLT_SS_OVERVIEW_REGION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| DSPLY_OVW_CONT_WARN | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DSPLY_OVW_CONT_WARN |
| CONT_WARN_DAYS | NUMBER |  | 18 |  | THIS COLUMN FIELD IS USED FOR CONT_WARN_DAYS |
| CONFIG_CHAR_1 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_1 |
| CONFIG_CHAR_2 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_2 |
| CONFIG_CHAR_3 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_3 |
| CONFIG_CHAR_4 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_4 |
| CONFIG_CHAR_5 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_5 |
| CONFIG_CHAR_6 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_CHAR_6 |
| CONFIG_DATE_1 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_1 |
| CONFIG_DATE_2 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_2 |
| CONFIG_DATE_3 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_3 |
| CONFIG_DATE_4 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_4 |
| CONFIG_NUMBER_2 | NUMBER |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_NUMBER_2 |
| CONFIG_NUMBER_1 | NUMBER |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_NUMBER_1 |
| DSPLY_CHC_WARN | VARCHAR2 | 30 |  |  | THIS COLUMN FIELD IS USED FOR DSPLY_CHC_WARN |
| CONFIG_CHAR_7 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL |
| CONFIG_CHAR_8 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL |
| CONFIG_CHAR_9 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL |
| CONFIG_CHAR_10 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL |
| CONFIG_CHAR_11 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_12 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_13 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_14 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_CHAR_15 | VARCHAR2 | 4000 |  |  | Template character field for future use. |
| CONFIG_DESC_1 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_2 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_3 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_4 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_5 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_6 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_7 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_8 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_9 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DESC_10 | VARCHAR2 | 4000 |  |  | THIS COLUMN FIELD IS USED FOR TO CAPTURE THE URL DESCRIPTION |
| CONFIG_DATE_5 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_5 |
| CONFIG_DATE_6 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_6 |
| CONFIG_DATE_7 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_7 |
| CONFIG_DATE_8 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_8 |
| CONFIG_DATE_9 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_9 |
| CONFIG_DATE_10 | DATE |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_DATE_10 |
| CONFIG_NUMBER_3 | NUMBER |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_NUMBER_3 |
| CONFIG_NUMBER_4 | NUMBER |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_NUMBER_4 |
| CONFIG_NUMBER_5 | NUMBER |  |  |  | THIS COLUMN FIELD IS USED FOR CONFIG_NUMBER_5 |
| SHOW_WELCOME_CD | VARCHAR2 | 240 |  |  | This column will store the welcome screen code. |
| PATH_SEL_CD | VARCHAR2 | 240 |  |  | This column will store the path selection code. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_SS_CONFIGURATION_U1 | Unique | Default | SS_CONFIG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
