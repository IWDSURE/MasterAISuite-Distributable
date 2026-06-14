# HRC_EVT_HANDLERS

An Event Handler identifies how a particular event will be managed once it is determined that its criteria has been satisfied.

Detection of an event can result in
a) an event being published to the SOA server (payload is dependent on the type of event)
b) a standard event (i.e. the payload is a fixed shape) is published to the SOA server; this can represent either a data change, in which case the standard event will contain the Source Object Change ID, or a transaction framework based event, in which case the payload will contain the Transaction ID
c) an internal call to a synchronous process, allowing invocation of processing in the same transaction
d) storage of data in the Source Object Change tables without publishing an event to SOA.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevthandlers-22451.html#hrcevthandlers-22451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevthandlers-22451.html#hrcevthandlers-22451)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_HANDLERS_PK | EVENT_HANDLER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_HANDLER_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| EVENT_TYPE_ID | NUMBER |  | 18 | Yes | Identifier of Event Type |
| CONSTRUCTION_METHOD_ID | NUMBER |  | 18 |  | Identifier of a Construction Method |
| HANDLER_TYPE | VARCHAR2 | 30 |  | Yes | Indicator of whether the event handler is "Internal" or "External" |
| PRODUCT_CODE | VARCHAR2 | 30 |  |  | Product Code used for filtering of events |
| PRODUCT_LABEL | VARCHAR2 | 80 |  |  | Free text label to allow multiple event handlers within a product for the same event |
| CLASS_NAME | VARCHAR2 | 240 |  |  | The name of an internal Java class used to invoke synchronous event processing |
| PROPAGATE_FUSION_CONTEXT | VARCHAR2 | 30 |  |  | Propagate Fusion Context to External Service. |
| SERVICE_URL | VARCHAR2 | 2000 |  |  | The External Service URL to be called. |
| CSF_KEY | VARCHAR2 | 2000 |  |  | Credential Store Factory Key. |
| MESSAGE_ENCRYPTION_KEY | VARCHAR2 | 2000 |  |  | Message Encryption Key. |
| OWSM_POLICY | VARCHAR2 | 2000 |  |  | Oracle Web Service Client Policy. |
| NOTIFY_FLAG | VARCHAR2 | 30 |  |  | Determines whether an event is published to the SOA server to notify the product that the event has occurred |
| ENABLED | VARCHAR2 | 30 |  | Yes | Determines whether the event handler is currently enabled |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJ_CONDITION_ID | NUMBER |  | 18 |  | Identifier of Event Object Condition |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_HANDLERS_F2 | Non Unique | FUSION_TS_TX_DATA | CONSTRUCTION_METHOD_ID |
| HRC_EVT_HANDLERS_N1 | Non Unique | Default | UPPER("PRODUCT_CODE"), UPPER("PRODUCT_LABEL") |
| HRC_EVT_HANDLERS_N20 | Non Unique | Default | SGUID |
| HRC_EVT_HANDLERS_PK | Unique | FUSION_TS_TX_DATA | EVENT_HANDLER_ID, ORA_SEED_SET1 |
| HRC_EVT_HANDLERS_PK1 | Unique | FUSION_TS_TX_DATA | EVENT_HANDLER_ID, ORA_SEED_SET2 |
| HRC_EVT_HANDLERS_U1 | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, CONSTRUCTION_METHOD_ID, PRODUCT_CODE, PRODUCT_LABEL, ENTERPRISE_ID, SERVICE_URL, OBJ_CONDITION_ID, ORA_SEED_SET1 |
| HRC_EVT_HANDLERS_U11 | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, CONSTRUCTION_METHOD_ID, PRODUCT_CODE, PRODUCT_LABEL, ENTERPRISE_ID, SERVICE_URL, OBJ_CONDITION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
