# BEN_ELCN_RULES_TL

BEN_ELCN_RULES identifies the enrollment dependency rules. A rule enforces the person to enroll into dependent opportunities. For example, person must enroll into Employee only option in HDHP plan in order to enroll into Employee only option in HSA plan.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelcnrulestl-25021.html#benelcnrulestl-25021](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benelcnrulestl-25021.html#benelcnrulestl-25021)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELCN_RULES_TL_PK | BEN_ELCN_RULE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BEN_ELCN_RULE_ID | NUMBER |  |  | Yes | System generated primary key column. |
| MSG_TEXT | VARCHAR2 | 4000 |  |  | Translated additional information of the rule. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  |  |  | Foreign Key to HR_ORGANIZATION_UNITS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELCN_RULES_TL_U1 | Unique | Default | BEN_ELCN_RULE_ID, LANGUAGE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
