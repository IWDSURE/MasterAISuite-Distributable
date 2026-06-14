# PER_TASK_LIB_COM_CONDNS_TL

Translation table of PER_TASK_LIB_COM_CONDNS_B

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasklibcomcondnstl-27921.html#pertasklibcomcondnstl-27921](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pertasklibcomcondnstl-27921.html#pertasklibcomcondnstl-27921)

## Primary Key

| Name | Columns |
|------|----------|
| PER_TASK_LIB_COM_CONDNS_TL_PK | TASK_LIB_COM_CONDITION_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TASK_LIB_COM_CONDITION_ID | NUMBER |  | 18 | Yes | TASK_LIB_COM_CONDITION_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| MESSAGE_TEXT | VARCHAR2 | 400 |  | Yes | MESSAGE_TEXT |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_TASK_LIB_COM_CONDNS_TL_PK | Unique | Default | TASK_LIB_COM_CONDITION_ID, LANGUAGE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
