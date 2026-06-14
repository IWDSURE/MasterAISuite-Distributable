# BEN_PER_BNF_ORG

BEN_PER_BNF_ORG identifies the organization's or trustee's that can be designated by a participant as the beneficiary of plan benefits. For e.g., a person may want an NGO as beneficiary of his or her life insurance benefits.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbnforg-29030.html#benperbnforg-29030](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benperbnforg-29030.html#benperbnforg-29030)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_PER_BNF_ORG_PK | PER_BNF_ORG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_BNF_ORG_ID | NUMBER |  | 22 | Yes | PER_BNF_ORG_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| START_DATE | DATE |  |  | Yes | START_DATE |
| END_DATE | DATE |  |  |  | END_DATE |
| PERSON_ID | NUMBER |  | 22 | Yes | PERSON_ID |
| BNF_TYP_CD | VARCHAR2 | 30 |  | Yes | BNF_TYP_CD |
| BNF_ORGANIZATION_ID | NUMBER |  | 22 |  | BNF_ORGANIZATION_ID |
| TRUSTEE_ORG_NAME | VARCHAR2 | 240 |  |  | TRUSTEE_ORG_NAME |
| TRUSTEE_ORG_REG_CD | VARCHAR2 | 240 |  |  | TRUSTEE_ORG_REG_CD |
| TRUSTEE_ORG_DESCRIPTION | VARCHAR2 | 600 |  |  | TRUSTEE_ORG_DESCRIPTION |
| TRUSTEE_ADDL_DETAILS | VARCHAR2 | 600 |  |  | TRUSTEE_ADDL_DETAILS |
| TRUSTEE_EXECUTOR_NAME | VARCHAR2 | 240 |  |  | TRUSTEE_EXECUTOR_NAME |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_PER_BNF_ORG_FK1 | Non Unique | Default | PERSON_ID |
| BEN_PER_BNF_ORG_U1 | Unique | Default | PER_BNF_ORG_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
