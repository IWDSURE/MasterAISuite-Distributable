# HRC_COMP_INST_VALS_TL

Contains translatable metadata for compare object instance values.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalstl-6589.html#hrccompinstvalstl-6589](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalstl-6589.html#hrccompinstvalstl-6589)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_comp_inst_vals_tl_PK | INSTANCE_VALUE_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| VALUE_SUPPLIED | VARCHAR2 | 1000 |  |  | Specifies the supplied value which is used to compare. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMP_VALS_TL_U1 | Unique | FUSION_TS_TX_DATA | INSTANCE_VALUE_ID, LANGUAGE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
