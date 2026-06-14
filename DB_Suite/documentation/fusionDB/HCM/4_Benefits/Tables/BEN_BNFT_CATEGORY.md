# BEN_BNFT_CATEGORY

Benefit Category..
Benefit Category..
Benefit Category..
Benefit Category..
Benefit Category..

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftcategory-16432.html#benbnftcategory-16432](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benbnftcategory-16432.html#benbnftcategory-16432)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_BNFT_CATEGORY_PK | CATEGORY_CD, USAGE_CD, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CATEGORY_CD | VARCHAR2 | 30 |  | Yes | 1 to 6 hardcode number for usage code. ???A???,???B???,???C???,???D???,???E???,???F??? Lets make this Varchar2, for storing codes is better |
| CATEGORY_HELP_TEXT | CLOB |  |  |  | CATEGORY_HELP_TEXT |
| USAGE_CD | VARCHAR2 | 30 |  | Yes | ???SS??? for self service and ???ADMIN??? for Admin UI |
| USER_NAME | VARCHAR2 | 200 |  |  | This can be like ???Health Care???, Flexible Spending Account??? etc. |
| ACTIVE_FLAG | VARCHAR2 | 30 |  |  | ACTIVE_FLAG |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | LEGAL_ENTITY_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| PRMRY_RT_LABEL | VARCHAR2 | 128 |  | Yes | This column keep track of label for Rate with Display Type as Primary |
| DSPLY_ANN_PRMRY_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Annual Primary Rate would be displayed on SSBEN |
| SCNDRY_RT_LABEL | VARCHAR2 | 128 |  | Yes | This column keep track of label for Rate with Display Type as Secondary. |
| DSPLY_SCNDRY_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Secondary  Rate would be displayed on SSBEN. |
| OTHR_PRETAX_RT_LABEL | VARCHAR2 | 128 |  | Yes | This column keep track of label for Rate with Display Type as Other and Tax Type Code as Pre  Tax |
| DSPLY_OTHR_PRETAX_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Other Pre  tax would be displayed on SSBEN |
| OTHR_AFTERTAX_RT_LABEL | VARCHAR2 | 128 |  | Yes | This column keep track of label for Rate with Display Type as Other and Tax Type Code as After Tax |
| DSPLY_OTHR_AFTERTAX_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Other After tax would be displayed on SSBEN |
| OTHR_TAXABLE_RT_LABEL | VARCHAR2 | 128 |  |  | This column keep track of label for Rate with Display Type as Other and Tax Type Code as Taxable |
| DSPLY_OTHR_TAXABLE_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Other Taxable would be displayed on SSBEN |
| OTHR_NONTAX_RT_LABEL | VARCHAR2 | 128 |  |  | This column keep track of label for Rate with Display Type as Other and Tax Type Code as Non Tax |
| DSPLY_OTHR_NONTAX_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Other Non  tax would be displayed on SSBEN |
| OTHR_NOTAPPLICABLE_RT_LABEL | VARCHAR2 | 128 |  |  | This column keep track of label for Rate with Display Type as Other and Tax Type Code as Non Applicable |
| DSPLY_OTHR_NOTAPPLICABLE_RT | VARCHAR2 | 1 |  |  | Flag to keep track whether Other NotApplicable  tax would be displayed on SSBEN |
| COVERAGE_LABEL | VARCHAR2 | 128 |  |  | This column keep track of label for Coverage |
| DSPLY_COVERAGE | VARCHAR2 | 1 |  |  | Flag to keep track whether Coverage would be displayed on SSBEN |
| LABEL1 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| LABEL2 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| LABEL3 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| LABEL4 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| LABEL5 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| LABEL6 | VARCHAR2 | 128 |  |  | Dummy label to cater any future enhancement. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CONFIG_NUM_1 | NUMBER |  |  |  | Template number column for future use. |
| CONFIG_NUM_2 | NUMBER |  |  |  | Template number column for future use. |
| CONFIG_NUM_3 | NUMBER |  |  |  | Template number column for future use. |
| CONFIG_NUM_4 | NUMBER |  |  |  | Template number column for future use. |
| CONFIG_NUM_5 | NUMBER |  |  |  | Template number column for future use. |
| CONFIG_CHAR_1 | VARCHAR2 | 240 |  |  | Template string column for future use. |
| CONFIG_CHAR_2 | VARCHAR2 | 240 |  |  | Template string column for future use. |
| CONFIG_CHAR_3 | VARCHAR2 | 240 |  |  | Template string column for future use. |
| CONFIG_CHAR_4 | VARCHAR2 | 240 |  |  | Template string column for future use. |
| CONFIG_CHAR_5 | VARCHAR2 | 240 |  |  | Template string column for future use. |
| CONFIG_DATE_1 | DATE |  |  |  | Template date column for future use. |
| CONFIG_DATE_2 | DATE |  |  |  | Template date column for future use. |
| CONFIG_DATE_3 | DATE |  |  |  | Template date column for future use. |
| CONFIG_DATE_4 | DATE |  |  |  | Template date column for future use. |
| CONFIG_DATE_5 | DATE |  |  |  | Template date column for future use. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_BNFT_CATEGORY_PK | Unique | FUSION_TS_TX_DATA | CATEGORY_CD, USAGE_CD, BUSINESS_GROUP_ID, ORA_SEED_SET1 |
| BEN_BNFT_CATEGORY_PK1 | Unique | FUSION_TS_TX_DATA | CATEGORY_CD, USAGE_CD, BUSINESS_GROUP_ID, ORA_SEED_SET2 |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
