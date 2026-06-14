# HWM_DS_API_CLASSES_TL

Stores translatable information on the API Class for Dynamic Script

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdsapiclassestl-12570.html#hwmdsapiclassestl-12570](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmdsapiclassestl-12570.html#hwmdsapiclassestl-12570)

## Primary Key

| Name | Columns |
|------|----------|
| HWM_DS_API_CLASSES_TL_PK | DS_CLASS_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DS_CLASS_ID | NUMBER |  | 18 | Yes | DS_CLASS_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Standard Enterprise Identifier column for multi tenancy support |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| DESCRIPTION | VARCHAR2 | 1000 |  |  | USER_DEFINED_NAME |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWM_DS_API_CLASSES_TL_PK | Unique | FUSION_TS_TX_DATA | DS_CLASS_ID, LANGUAGE |

---

[← Back to Index](../31_Workforce_Management_Tables_Index.md)
