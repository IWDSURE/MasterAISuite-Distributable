# HRC_COMP_OBJ_INSTANCES

A comparison instance with association to a object instance (e.g. benefit plan) for the template.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompobjinstances-30743.html#hrccompobjinstances-30743](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompobjinstances-30743.html#hrccompobjinstances-30743)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INSTANCE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| IKEY | VARCHAR2 | 128 |  | Yes | Immutable key. Oracle internal use only. |
| TEMPLATE_ID | NUMBER |  | 18 | Yes | Foreign Key to "hrc_comp_templates_b". |
| DATE_FROM | DATE |  |  | Yes | Indicates the date from the instance is active. |
| DATE_TO | DATE |  |  | Yes | Indicates the date the instance  is active to. |
| REF_PRODUCT_CODE | VARCHAR2 | 30 |  |  | Identifies the reference owning product. |
| REF_OBJECT_NAME | VARCHAR2 | 240 |  |  | This column contains the name of the referenced object. |
| REF_BASE_TABLE_NAME | VARCHAR2 | 128 |  |  | Ref Base Table Name (stored in uppercase). |
| REF_SKID | NUMBER |  | 18 |  | Foreign Key Surrogate Key ID to reference table. |
| BEN_DOC_IMG_ID | NUMBER |  | 18 |  | This column contains foreign key to ben_doc_images. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
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
| HRC_COMP_OBJ_INSTANCES_N1 | Non Unique | FUSION_TS_TX_DATA | TEMPLATE_ID |
| HRC_COMP_OBJ_INSTANCES_N2 | Non Unique | FUSION_TS_TX_DATA | REF_SKID, REF_OBJECT_NAME, REF_PRODUCT_CODE |
| HRC_COMP_OBJ_INSTANCES_N3 | Non Unique | FUSION_TS_TX_DATA | REF_OBJECT_NAME, DATE_FROM |
| HRC_COMP_OBJ_INSTANCES_N4 | Non Unique | FUSION_TS_TX_DATA | IKEY |
| HRC_COMP_OBJ_INSTANCES_U1 | Unique | FUSION_TS_TX_DATA | INSTANCE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
