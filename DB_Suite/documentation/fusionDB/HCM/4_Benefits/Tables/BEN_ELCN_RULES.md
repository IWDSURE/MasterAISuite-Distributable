# BEN_ELCN_RULES

BEN_ELCN_RULES identifies the enrollment dependency rules. A rule enforces the person to enroll into dependent opportunities. For example, person must enroll into Employee only option in HDHP plan in order to enroll into Employee only option in HSA plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelcnrules-26193.html#benelcnrules-26193](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelcnrules-26193.html#benelcnrules-26193)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELCN_RULES_PK | BEN_ELCN_RULE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BEN_ELCN_RULE_ID | NUMBER |  |  | Yes | System generated primary key column. |
| PL_TYP_GRP_CD | VARCHAR2 | 30 |  | Yes | Indicates the plan type grouping code. |
| NAME | VARCHAR2 | 240 |  | Yes | Indicates the name of the rule. |
| DESCRIPTION | VARCHAR2 | 4000 |  |  | Indicates the description of the rule. |
| PGM_ID | NUMBER |  |  | Yes | Foreign key to BEN_PGM_F. Used to identify the program. |
| PL_ID | NUMBER |  |  | Yes | Foreign key to BEN_PL_F.Used to identify the plan. |
| OIPL_ID | NUMBER |  |  |  | Foreign key to BEN_OIPL_F.Used to identify the option in plan. |
| OPT_ID | NUMBER |  |  |  | Foreign key to BEN_OPT_F.Used to identify the option. |
| RULE_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the type of the election rule. |
| MUST_OIPL_ID | NUMBER |  |  |  | Foreign key to BEN_OIPL_F.Used to identify the option in plan. |
| MUST_PL_ID | NUMBER |  |  | Yes | Foreign key to BEN_PL_F.Used to identify the plan. |
| MUST_OPT_ID | NUMBER |  |  |  | Foreign key to BEN_OPT_F.Used to identify the option. |
| MUST_PGM_ID | NUMBER |  |  | Yes | Foreign key to BEN_PGM_F.Used to identify the program. |
| SCOPE | VARCHAR2 | 30 |  | Yes | Module where rule needs to be validated. |
| MSG_TEXT | VARCHAR2 | 4000 |  |  | Additional information of the rule. |
| STAT_CD | VARCHAR2 | 30 |  | Yes | Indicates the status of the rule. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  |  |  | Foreign Key to HR_ORGANIZATION_UNITS |
| INFO_CHAR_1 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_2 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_3 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_4 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_5 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_6 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_7 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_8 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_9 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_CHAR_10 | VARCHAR2 | 400 |  |  | Template string column for future use. |
| INFO_DATE_1 | DATE |  |  |  | Template date column for future use. |
| INFO_DATE_2 | DATE |  |  |  | Template date column for future use. |
| INFO_DATE_3 | DATE |  |  |  | Template date column for future use. |
| INFO_DATE_4 | DATE |  |  |  | Template date column for future use. |
| INFO_DATE_5 | DATE |  |  |  | Template date column for future use. |
| INFO_NUM_1 | NUMBER |  |  |  | Template number column for future use. |
| INFO_NUM_2 | NUMBER |  |  |  | Template number column for future use. |
| INFO_NUM_3 | NUMBER |  |  |  | Template number column for future use. |
| INFO_NUM_4 | NUMBER |  |  |  | Template number column for future use. |
| INFO_NUM_5 | NUMBER |  |  |  | Template number column for future use. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELCN_RULES_N1 | Non Unique | Default | PL_TYP_GRP_CD, PGM_ID, PL_ID |
| BEN_ELCN_RULES_PK | Unique | Default | BEN_ELCN_RULE_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
