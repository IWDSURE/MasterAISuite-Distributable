# HRC_DL_TEMPLATES

This table contains the details of the ESS Job process invoked for Template file generation and the UCM file details.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdltemplates-22690.html#hrcdltemplates-22690](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdltemplates-22690.html#hrcdltemplates-22690)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_TEMPLATES_PK | TEMPLATE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TEMPLATE_ID | NUMBER |  | 18 | Yes | TEMPLATE_ID |
| LEVEL_CODE | VARCHAR2 | 30 |  |  | LEVEL_ID |
| MODULE_CODE | VARCHAR2 | 30 |  |  | MODULE |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | BUSINESS_OBJECT_ID |
| UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | UCM_CONTENT_ID |
| TEMPLATE_FILE_NAME | VARCHAR2 | 200 |  |  | TEMPLATE_FILE_NAME |
| STATUS | VARCHAR2 | 30 |  | Yes | STATUS |
| UCM_FILE_VERSION | NUMBER |  | 9 |  | UCM_FILE_VERSION |
| PARENT_TEMPLATE_ID | NUMBER |  | 18 |  | PARENT_TEMPLATE_ID |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| MAPPING_FILE_UCM_CONTENT_ID | VARCHAR2 | 30 |  |  | MAPPING_FILE_UCM_CONTENT_ID |
| MAPPING_FILE_NAME | VARCHAR2 | 200 |  |  | MAPPING_FILE_NAME |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_TEMPLATES_F1 | Non Unique | Default | BUSINESS_OBJECT_ID |
| HRC_DL_TEMPLATES_F2 | Non Unique | Default | REQUEST_ID |
| HRC_DL_TEMPLATES_PK | Unique | Default | TEMPLATE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
