# HWR_USER_BUS_OBJECT_B

The table stores base user defined business objects.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwruserbusobjectb-15689.html#hwruserbusobjectb-15689](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwruserbusobjectb-15689.html#hwruserbusobjectb-15689)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_USER_BUS_OBJECT_B_PK | ID, REVISION_NUMBER, NAME, ONTOLOGY_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the column ID on table HWR_USER_BUS_OBJECT_B. |
| NAME | VARCHAR2 | 256 |  | Yes | This is the column NAME on table HWR_USER_BUS_OBJECT_B. |
| IS_CUSTOM | NUMBER |  |  |  | This is the column IS_CUSTOM on table. |
| ONTOLOGY_TYPE | VARCHAR2 | 64 |  | Yes | This is the column ontology type on table. |
| DS_TYPE | VARCHAR2 | 64 |  |  | This is the column DS_TYPE on table HWR_USER_BUS_OBJECT_B. |
| DS_TYPE_VERSION | VARCHAR2 | 64 |  |  | This is the column DS_TYPE_VERSION on table HWR_USER_BUS_OBJECT_B. |
| LOCALE_KEY | VARCHAR2 | 6 |  |  | This is the column LOCALE_KEY on table HWR_USER_BUS_OBJECT_B. |
| FILE_CLOB | CLOB |  |  |  | This is the column FILE_CLOB on table HWR_USER_BUS_OBJECT_B. |
| CUSTOM_BO_DATA | CLOB |  |  |  | This is the column CUSTOM_BO_DATA on table HWR_USER_BUS_OBJECT_B. |
| DELTA_VERSION | VARCHAR2 | 64 |  |  | This is the column DELTA_VERSION on table HWR_USER_BUS_OBJECT_B. |
| REVISION_NUMBER | NUMBER |  |  | Yes | This is the column revision_number on table HWR_USER_BUS_OBJECT_B. |
| DOMAIN | VARCHAR2 | 255 |  |  | This is the column domain on table HWR_USER_BUS_OBJECT_B. |
| CATEGORY | VARCHAR2 | 255 |  |  | This is the column category on table HWR_USER_BUS_OBJECT_B. |
| STATUS | VARCHAR2 | 30 |  |  | This is the column status on table HWR_USER_BUS_OBJECT_B. |
| STATE_CODE | VARCHAR2 | 30 |  |  | This is the column state code on table HWR_USER_BUS_OBJECT_B. |
| TYPE | VARCHAR2 | 255 |  |  | This is the column type on table HWR_USER_BUS_OBJECT_B. |
| BASE_CONTROL_ID | NUMBER |  | 18 |  | This is the column control on table HWR_USER_BUS_OBJECT_B. |
| ONT_CLASS_URL | VARCHAR2 | 400 |  |  | This is the column ont class url on table HWR_USER_BUS_OBJECT_B. |
| FILE_NAME | VARCHAR2 | 255 |  |  | This is the column file name on table HWR_USER_BUS_OBJECT_B. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_USER_BUS_OBJECT_B_U1 | Unique | Default | ID, REVISION_NUMBER, NAME, ONTOLOGY_TYPE, DS_TYPE, DS_TYPE_VERSION |
| HWR_USER_BUS_OBJECT_B_U2 | Unique | Default | ID, REVISION_NUMBER, NAME, ONTOLOGY_TYPE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
