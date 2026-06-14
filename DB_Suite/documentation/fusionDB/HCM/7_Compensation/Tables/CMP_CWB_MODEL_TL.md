# CMP_CWB_MODEL_TL

Table stores distribution model translated details

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodeltl-20245.html#cmpcwbmodeltl-20245](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcwbmodeltl-20245.html#cmpcwbmodeltl-20245)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CWB_MODEL_TL_PK | MODEL_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MODEL_ID | NUMBER |  | 18 | Yes | MODEL_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| NAME | VARCHAR2 | 240 |  | Yes | NAME |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CWB_MODEL_TL_UK1 | Unique | Default | MODEL_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
