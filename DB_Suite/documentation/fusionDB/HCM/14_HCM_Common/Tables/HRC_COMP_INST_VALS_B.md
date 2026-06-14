# HRC_COMP_INST_VALS_B

Defines comparison instance values for an object instance.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalsb-23472.html#hrccompinstvalsb-23472](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalsb-23472.html#hrccompinstvalsb-23472)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_VALUE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| IKEY | VARCHAR2 | 128 |  | Yes | Immutable key. Oracle internal use only. |
| INSTANCE_ID | NUMBER |  | 18 | Yes | Foreign Key to hrc_comp_obj_instances. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign Key to hrc_comp_templates_b. |
| ITEM_ID | NUMBER |  | 18 |  | Foreign Key to hrc_comp_items_b. |
| CAT_DEF_VAL_ID | NUMBER |  | 18 |  | Specifies the value's category value identifier. Foreign key to hrc_comp_def_vals. |
| OPT_DEF_VAL_ID | NUMBER |  | 18 |  | Specifies the value's option value identifier. Foreign key to hrc_comp_def_vals. |
| SUGV_FLAG | VARCHAR2 | 30 |  | Yes | Specifies if a common feature value is being used Y or N. |
| VALUE_TYPE | VARCHAR2 | 30 |  | Yes | Specifies the value's type (HEADER, ITEM, INSTANCE). |
| VALUE_NAME | VARCHAR2 | 128 |  |  | Specifies a value name which is used to compare. |
| VALUE_DATATYPE | VARCHAR2 | 30 |  | Yes | Specifies the value datatype (VARCHAR2, CLOB, BLOB,NUMBER,DATE,TIMESTAMP, SKID). |
| VALUE_VARCHAR2 | VARCHAR2 | 1000 |  |  | Specifies the text value to be used for comparison. |
| VALUE_NUMBER | NUMBER |  | 18 |  | Specifies a number for the value. |
| VALUE_TIMESTAMP | TIMESTAMP |  |  |  | Specifies a timestamp for the value. |
| VALUE_DATE | DATE |  |  |  | Specifies a date value which is used to compare. |
| VALUE_BLOB | BLOB |  |  |  | Specifies a BLOB for the value. |
| VALUE_CLOB | CLOB |  |  |  | Specifies a CLOB for the value. |
| VALUE_SKID | NUMBER |  | 18 |  | Specifies a surrogate key identifier for the value. |
| FOOTNOTE_REFS | VARCHAR2 | 1000 |  |  | Specifies a collection (array) of note item references  in JSON format. |
| ATTR_CHAR1 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_CHAR2 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_CHAR3 | VARCHAR2 | 1000 |  |  | Additional column for storing characters. |
| ATTR_NUMBER1 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_NUMBER2 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_NUMBER3 | NUMBER |  | 18 |  | Additional column for storing a number. |
| ATTR_DATE1 | DATE |  |  |  | Additional column for storing a date. |
| ATTR_DATE2 | DATE |  |  |  | Additional column for storing a date. |
| ATTR_DATE3 | DATE |  |  |  | Additional column for storing a date. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_COMP_VALS_F_B_N1 | Non Unique | FUSION_TS_TX_DATA | INSTANCE_ID |
| HRC_COMP_VALS_F_B_N2 | Non Unique | FUSION_TS_TX_DATA | ITEM_ID |
| HRC_COMP_VALS_F_B_N3 | Non Unique | FUSION_TS_TX_DATA | TEMPLATE_ID |
| HRC_COMP_VALS_F_B_N4 | Non Unique | FUSION_TS_TX_DATA | CAT_DEF_VAL_ID |
| HRC_COMP_VALS_F_B_N5 | Non Unique | FUSION_TS_TX_DATA | OPT_DEF_VAL_ID |
| HRC_COMP_VALS_F_B_N6 | Non Unique | FUSION_TS_TX_DATA | VALUE_SKID |
| HRC_COMP_VALS_F_B_N7 | Non Unique | FUSION_TS_TX_DATA | IKEY |
| HRC_COMP_VALS_F_B_U1 | Unique | FUSION_TS_TX_DATA | INSTANCE_VALUE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
