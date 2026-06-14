# HRC_EVT_ATTRIBUTE_MAPPINGS

A Attribute Mapping is used to indicate that a particular Entity Object or PLSQL Row Handler attribute should be included in an Event Payload.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtattributemappings-25557.html#hrcevtattributemappings-25557](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtattributemappings-25557.html#hrcevtattributemappings-25557)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_ATTR_MAPPINGS_PK | ATTRIBUTE_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_MAPPING_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| CONSTRUCTION_METHOD_ID | NUMBER |  | 18 | Yes | Unique Identifier of the Construction Method |
| SOURCE_OBJECT_ATTRIBUTE_ID | NUMBER |  | 18 |  | Unique Identifier of the Source Object Attribute |
| PAYLOAD_ITEM_ID | NUMBER |  | 18 | Yes | Unique Identifier of the Payload Item to which the Attribute Mapping relates |
| CHANGED_ALWAYS | VARCHAR2 | 30 |  |  | Indication of whether the Attributes should Always be included in the Payload or only when its value has Changed |
| OLD_NEW | VARCHAR2 | 30 |  |  | Indication of whether the Old or the New  value should be used in the payload item mapping |
| EO_METHOD | VARCHAR2 | 80 |  |  | Name of the entity object method used to return the attribute value |
| SERVICE_PARAMETER | VARCHAR2 | 80 |  |  | Name of the standard Service Parameter that contains the payload data |
| LITERAL_VALUE | VARCHAR2 | 240 |  |  | Literal value that will be put in the event payload |
| MESSAGE_NAME | VARCHAR2 | 240 |  |  | Message Name that will be translated before being put in the event payload |
| SYSTEM_VARIABLE | VARCHAR2 | 80 |  |  | The name of a system variable that will be used to populate the event payload. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_ATTRIBUTE_MAPPING_N20 | Non Unique | Default | SGUID |
| HRC_EVT_ATTR_MAPPINGS_F2 | Non Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ATTRIBUTE_ID |
| HRC_EVT_ATTR_MAPPINGS_F3 | Non Unique | FUSION_TS_TX_DATA | PAYLOAD_ITEM_ID |
| HRC_EVT_ATTR_MAPPINGS_PK | Unique | FUSION_TS_TX_DATA | ATTRIBUTE_MAPPING_ID, ORA_SEED_SET1 |
| HRC_EVT_ATTR_MAPPINGS_PK1 | Unique | FUSION_TS_TX_DATA | ATTRIBUTE_MAPPING_ID, ORA_SEED_SET2 |
| HRC_EVT_ATTR_MAPPINGS_U1 | Unique | FUSION_TS_TX_DATA | CONSTRUCTION_METHOD_ID, SOURCE_OBJECT_ATTRIBUTE_ID, PAYLOAD_ITEM_ID, SERVICE_PARAMETER, EO_METHOD, LITERAL_VALUE, MESSAGE_NAME, SYSTEM_VARIABLE, ORA_SEED_SET1 |
| HRC_EVT_ATTR_MAPPINGS_U11 | Unique | FUSION_TS_TX_DATA | CONSTRUCTION_METHOD_ID, SOURCE_OBJECT_ATTRIBUTE_ID, PAYLOAD_ITEM_ID, SERVICE_PARAMETER, EO_METHOD, LITERAL_VALUE, MESSAGE_NAME, SYSTEM_VARIABLE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
