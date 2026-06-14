# HRC_EVT_PAYLOAD_ITEMS

A Payload Item defines an instance of an XML TAG attribute in an Event Definition.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtpayloaditems-17102.html#hrcevtpayloaditems-17102](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtpayloaditems-17102.html#hrcevtpayloaditems-17102)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_PAYLOAD_ITEMS_PK | PAYLOAD_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PAYLOAD_ITEM_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| EVENT_DEFINITION_ID | NUMBER |  | 18 | Yes | Unique Identifier of Event Definition |
| TAG | VARCHAR2 | 80 |  | Yes | Payload XML Attribute TAG |
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
| HRC_EVT_PAYLOAD_ITEMS_N20 | Non Unique | Default | SGUID |
| HRC_EVT_PAYLOAD_ITEMS_PK | Unique | FUSION_TS_TX_DATA | PAYLOAD_ITEM_ID, ORA_SEED_SET1 |
| HRC_EVT_PAYLOAD_ITEMS_PK1 | Unique | FUSION_TS_TX_DATA | PAYLOAD_ITEM_ID, ORA_SEED_SET2 |
| HRC_EVT_PAYLOAD_ITEMS_U1 | Unique | FUSION_TS_TX_DATA | EVENT_DEFINITION_ID, TAG, ORA_SEED_SET1 |
| HRC_EVT_PAYLOAD_ITEMS_U11 | Unique | FUSION_TS_TX_DATA | EVENT_DEFINITION_ID, TAG, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
