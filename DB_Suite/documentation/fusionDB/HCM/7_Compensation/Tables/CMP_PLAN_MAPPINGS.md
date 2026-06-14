# CMP_PLAN_MAPPINGS

This table stores the plan mappings for integration with outside vendors ( Taleo etc.)

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanmappings-19615.html#cmpplanmappings-19615](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpplanmappings-19615.html#cmpplanmappings-19615)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_PLAN_MAPPINGS_PK | VENDOR, VENDOR_PLAN_CODE, VENDOR_COMPONENT_CODE, BUSINESS_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| VENDOR | VARCHAR2 | 80 |  | Yes | VENDOR |
| VENDOR_PLAN_CODE | VARCHAR2 | 80 |  | Yes | VENDOR_PLAN_CODE |
| VENDOR_COMPONENT_CODE | VARCHAR2 | 80 |  | Yes | VENDOR_COMPONENT_CODE |
| FUSION_PLAN_ID | NUMBER |  | 18 |  | FUSION_PLAN_ID |
| FUSION_COMPONENT_ID | NUMBER |  | 18 |  | FUSION_COMPONENT_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_PLAN_MAPPINGS_N1 | Non Unique | FUSION_TS_TX_DATA | BUSINESS_GROUP_ID, VENDOR |
| CMP_PLAN_MAPPINGS_N21 | Non Unique | FUSION_TS_TX_DATA | FUSION_PLAN_ID, FUSION_COMPONENT_ID |
| CMP_PLAN_MAPPINGS_PK | Unique | FUSION_TS_TX_DATA | VENDOR, VENDOR_PLAN_CODE, VENDOR_COMPONENT_CODE, BUSINESS_GROUP_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
