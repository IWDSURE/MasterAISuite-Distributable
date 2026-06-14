# CMP_TCS_TEMPLATES

This table will store the BIP template name, definition and other details. This will be used by TCS to customize and manage the BIP templates so that customer does not have to go to BIP to do the same.

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcstemplates-27670.html#cmptcstemplates-27670](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcstemplates-27670.html#cmptcstemplates-27670)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_TCS_TEMPLATES_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| FILE_NAME | VARCHAR2 | 80 |  | Yes | FILE_NAME |
| TEMPLATE_FILE | BLOB |  |  |  | TEMPLATE_FILE |
| BIP_TEMPLATE_NAME | VARCHAR2 | 80 |  | Yes | BIP_TEMPLATE_NAME |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_TCS_TEMPLATES_U1 | Unique | Default | TEMPLATE_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
