# HEX_EXT_DEL_OPTION_OVERRIDE

The table stores the details of enabled/disabled Delivery options used in Extract Definition.

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** TABLE

**Tablespace:** FUSION_TS_SEED

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexextdeloptionoverride-13479.html#hexextdeloptionoverride-13479](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexextdeloptionoverride-13479.html#hexextdeloptionoverride-13479)

## Primary Key

| Name | Columns |
|------|----------|
| HEX_EXT_DEL_OPTION_OVERRIDE_PK | EXT_DEL_OPTION_OVERRIDE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EXT_DEL_OPTION_OVERRIDE_ID | NUMBER |  | 18 | Yes | System generated Primary Key. Uniquely identifies a record. |
| EXT_DELIVERY_OPTION_ID | NUMBER |  | 18 | Yes | The column indicates the foreign key reference to the delivery option id from PER_EXT_DELIVERY_OPTIONS_B. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | The column indicates the legislation code derived from Legal Entity. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | The column indicates the foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENABLED_FLAG | VARCHAR2 | 1 |  |  | The flag indicates whether the delivery option is enabled or disabled. Valid values are Y and N. Default value is Y. |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HEX_EXT_DEL_OPTION_OVERRIDE_PK | Unique | FUSION_TS_TX_DATA | EXT_DEL_OPTION_OVERRIDE_ID |

---

[← Back to Index](../18_HCM_Extracts_Tables_Index.md)
