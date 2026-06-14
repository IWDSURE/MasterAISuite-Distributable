# PER_CHK_CONFIGURATIONS

Table to store configurations that will determine checklist behaviour.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkconfigurations-21402.html#perchkconfigurations-21402](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkconfigurations-21402.html#perchkconfigurations-21402)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CHK_CONFIGURATIONS_PK | CONFIGURATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONFIGURATION_ID | NUMBER |  | 18 | Yes | CONFIGURATION_ID |
| CONFIGURATION_TYPE | VARCHAR2 | 30 |  | Yes | CONFIGURATION_TYPE |
| CONFIGURATION_SUB_TYPE | VARCHAR2 | 30 |  |  | CONFIGURATION_SUB_TYPE |
| CONFIGURATION_CODE | VARCHAR2 | 80 |  | Yes | CONFIGURATION_CODE |
| CONFIGURATION_NAME | VARCHAR2 | 240 |  | Yes | CONFIGURATION_NAME |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | DESCRIPTION |
| ENABLED_FLAG | VARCHAR2 | 4 |  | Yes | ENABLED_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CONFIGURATION_TEXT1 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT1 |
| CONFIGURATION_TEXT2 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT2 |
| CONFIGURATION_TEXT3 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT3 |
| CONFIGURATION_TEXT4 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT4 |
| CONFIGURATION_TEXT5 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT5 |
| CONFIGURATION_TEXT6 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT6 |
| CONFIGURATION_TEXT7 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT7 |
| CONFIGURATION_TEXT8 | VARCHAR2 | 4000 |  |  | CONFIGURATION_TEXT8 |
| CONFIGURATION_DETAILS | CLOB |  |  |  | CONFIGURATION_DETAILS |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHK_CONFIGURATIONS_PK | Unique | Default | CONFIGURATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
