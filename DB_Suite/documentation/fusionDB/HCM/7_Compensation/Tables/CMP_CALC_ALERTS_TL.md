# CMP_CALC_ALERTS_TL

Stores custom alerts translation attributes

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcalertstl-13500.html#cmpcalcalertstl-13500](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpcalcalertstl-13500.html#cmpcalcalertstl-13500)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_CALC_ALERTS_TL_PK | ALERT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALERT_ID | NUMBER |  | 18 | Yes | ALERT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ALERT_NAME | VARCHAR2 | 80 |  |  | ALERT_NAME |
| ALERT_DESCRIPTION | VARCHAR2 | 400 |  |  | ALERT_DESCRIPTION |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_CALC_ALERTS_TL_UK1 | Unique | Default | ALERT_ID, LANGUAGE |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
