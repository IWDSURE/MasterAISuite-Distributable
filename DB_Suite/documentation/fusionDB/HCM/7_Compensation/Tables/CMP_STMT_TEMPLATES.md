# CMP_STMT_TEMPLATES

Table stores statment templates records.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmttemplates-24320.html#cmpstmttemplates-24320](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmttemplates-24320.html#cmpstmttemplates-24320)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_STMT_TEMPLATES_PK | STMT_TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| STMT_TEMPLATE_ID | NUMBER |  | 18 | Yes | STMT_TEMPLATE_ID |
| FILE_NAME | VARCHAR2 | 80 |  | Yes | FILE_NAME |
| TEMPLATE_TYPE | VARCHAR2 | 10 |  | Yes | TEMPLATE_TYPE |
| GROUP_TYPE | VARCHAR2 | 10 |  | Yes | GROUP_TYPE |
| BIP_TEMPLATE_NAME | VARCHAR2 | 80 |  | Yes | BIP_TEMPLATE_NAME |
| TEMPLATE_FILE | BLOB |  |  |  | TEMPLATE_FILE |
| SEEDED_FLAG | VARCHAR2 | 1 |  | Yes | SEEDED_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_STMT_TEMPLATES_UK1 | Unique | Default | STMT_TEMPLATE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
