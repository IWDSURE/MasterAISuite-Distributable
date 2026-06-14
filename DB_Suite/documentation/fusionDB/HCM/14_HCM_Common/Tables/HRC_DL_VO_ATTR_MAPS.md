# HRC_DL_VO_ATTR_MAPS

HRC_DL_VO_ATTR_MAPS is used to record mappings used for individual View Object attributes at import time so that they may be referenced at load time for the staged physical data row being processed.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvoattrmaps-27514.html#hrcdlvoattrmaps-27514](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlvoattrmaps-27514.html#hrcdlvoattrmaps-27514)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_VO_ATTR_MAPS_PK | VO_ATTRIBUTE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VO_ATTRIBUTE_MAPPING_ID | NUMBER |  | 18 | Yes | VO_ATTRIBUTE_MAPPING_ID |
| SQL_TYPE | VARCHAR2 | 30 |  |  | SQL type of the attribute, given in a string format. |
| VO_MAPPING_ID | NUMBER |  | 18 | Yes | VO_MAPPING_ID |
| VO_ATTRIBUTE_MAPPING_HASH | VARCHAR2 | 100 |  | Yes | VO_ATTRIBUTE_MAPPING_HASH |
| VO_ATTRIBUTE_NAME | VARCHAR2 | 100 |  | Yes | VO_ATTRIBUTE_NAME |
| ATTRIBUTE_ALIAS_NAME | VARCHAR2 | 100 |  |  | ALIAS_NAME |
| STAGE_COLUMN_NAME | VARCHAR2 | 100 |  | Yes | STAGE_COLUMN_NAME |
| STAGE_ALT_SOURCE_SYSTEM_OWNER | VARCHAR2 | 100 |  |  | STAGE_ALT_SOURCE_SYSTEM_OWNER |
| STAGE_INTEGRATION_KEY | VARCHAR2 | 100 |  |  | STAGE_INTEGRATION_KEY |
| REF_TYPE | VARCHAR2 | 30 |  |  | REF_TYPE |
| REF_TABLE_NAME | VARCHAR2 | 100 |  |  | REF_TABLE_NAME |
| LOCAL_REF_TABLE_COL_NAME | VARCHAR2 | 100 |  |  | LOCAL_REF_TABLE_COL_NAME |
| REF_SUR_KEY_COL_NAME | VARCHAR2 | 100 |  |  | REF_SUR_KEY_COL_NAME |
| REF_INT_KEY_MAP_OBJ_NAME | VARCHAR2 | 100 |  |  | REF_INT_KEY_MAP_OBJ_NAME |
| HIDDEN_DL | VARCHAR2 | 30 |  |  | A value of H indicates this attribute should be excluded from the Data Loader generated templates and the information user interface. A value of D or null indicates the attribute should be included. |
| LENGTH | NUMBER |  | 8 |  | Either the maximum number or characters in a string or the number of significant digits in a numerical attribute. |
| SCALE | NUMBER |  | 8 |  | The number of decimal places to the right of the decimal point in a numerical attribute. For example, Long integers like surrogate ids have a scale of 0, floating point values like 123.45 have a scale of 2. |
| ADF_JAVA_TYPE | VARCHAR2 | 60 |  |  | The fully qualified java class name for an attribute. |
| HCM_LOOKUP_TYPE | VARCHAR2 | 30 |  |  | The lookup type if this attribute is identified as a HcmLookup. |
| UI_MANDATORY | VARCHAR2 | 30 |  |  | An attribute mandatory code representing one unifed mandatory status specifically for the HDL UI. |
| ADF_MANDATORY | VARCHAR2 | 1 |  |  | ADF API AttributeDef.isMandatory() returns true. |
| MANDATORY_ALWAYS | VARCHAR2 | 30 |  |  | Lookup value indicating whether the attribute is part of the Required Always (R) specification. |
| MANDATORY_ONLY_CREATE | VARCHAR2 | 30 |  |  | Lookup value indicating whether the attribute is part of the Required Only on Create (RC) specification. |
| MANDATORY_ALWAYS_SETS | VARCHAR2 | 1500 |  |  | The attribute combinations that involve this attribute in the Required Always (R) specification. |
| MANDATORY_ONLY_CREATE_SETS | VARCHAR2 | 1500 |  |  | The attribute combinations that involve this attribute in the Required Only on Create (RC) specification. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_VO_ATTR_MAPS_PK | Unique | Default | VO_ATTRIBUTE_MAPPING_ID |
| HRC_DL_VO_ATTR_MAPS_U1 | Unique | Default | VO_MAPPING_ID, VO_ATTRIBUTE_MAPPING_HASH |
| HRC_DL_VO_ATTR_MAPS_U2 | Unique | Default | VO_MAPPING_ID, VO_ATTRIBUTE_MAPPING_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
