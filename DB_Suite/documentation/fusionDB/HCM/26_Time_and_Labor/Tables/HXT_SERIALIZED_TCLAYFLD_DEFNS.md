# HXT_SERIALIZED_TCLAYFLD_DEFNS

This table is to store the serialized object of TCF information

## Details

**Schema:** FUSION

**Object owner:** HXT

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtserializedtclayflddefns-14327.html#hxtserializedtclayflddefns-14327](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hxtserializedtclayflddefns-14327.html#hxtserializedtclayflddefns-14327)

## Primary Key

| Name | Columns |
|------|----------|
| HXT_SERIALIZED_TCLAYFLD_D_PK | SERIALIZED_TCF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SERIALIZED_TCF_ID | NUMBER |  | 18 | Yes | SERIALIZED_TCF_ID |
| TCLAYFLD_DEFNS_ID | NUMBER |  | 18 | Yes | This column refers to Timecard field Id |
| SCHEMA_VERSION | VARCHAR2 | 30 |  | Yes | This column refers to the json schema version |
| LAYOUT_CACHE | CLOB |  |  | Yes | This column refers to the json object |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HXT_SERIALIZED_TCLAYFLD_D_PK | Unique | DEFAULT | SERIALIZED_TCF_ID |

---

[← Back to Index](../26_Time_and_Labor_Tables_Index.md)
