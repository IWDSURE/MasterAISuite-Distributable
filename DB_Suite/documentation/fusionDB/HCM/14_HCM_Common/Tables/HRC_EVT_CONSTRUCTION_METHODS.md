# HRC_EVT_CONSTRUCTION_METHODS

A Construction Method defines how a published event will be raised in terms of the technology that will be used. It specifies whether the payload will be constructed from a set of defined attributes (in which case these attributes are listed in the Attribute Mappings table), whether it will be derived using a Java method or a PLSQL procedure, or whether it will be derived from attributes passed into a service.

If the Java method is used then a custom Java class must be defined which should contain the method named "constructPayload".

If "Service" is chosen, this indicates that a standard HCM Event service will have been raised to invoke the HCM Events model. As part of the service a set of generic service parameters will have been populated which are subsequently mapped to Event Payload Items.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtconstructionmethods-8079.html#hrcevtconstructionmethods-8079](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtconstructionmethods-8079.html#hrcevtconstructionmethods-8079)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_CONSTRUCT_METHS_PK | CONSTRUCTION_METHOD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONSTRUCTION_METHOD_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| EVENT_DEFINITION_ID | NUMBER |  | 18 | Yes | Unique Identifier of Event Definition |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Unique Identifier of Source Object |
| PLSQL_PROCEDURE | VARCHAR2 | 80 |  |  | Packaged procedure used to build the payload |
| PUBLISHED_EVENT_NAME | VARCHAR2 | 80 |  | Yes | Name of the Published Event |
| EDL_NAMESPACE | VARCHAR2 | 240 |  | Yes | EDL Namespace of the published event |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
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
| HRC_EVT_CONSTRUCTION_METH_N20 | Non Unique | Default | SGUID |
| HRC_EVT_CONSTRUCT_METHS_F1 | Non Unique | FUSION_TS_TX_DATA | EVENT_DEFINITION_ID |
| HRC_EVT_CONSTRUCT_METHS_N1 | Non Unique | Default | UPPER("PUBLISHED_EVENT_NAME"), UPPER("EDL_NAMESPACE") |
| HRC_EVT_CONSTRUCT_METHS_PK | Unique | FUSION_TS_TX_DATA | CONSTRUCTION_METHOD_ID, ORA_SEED_SET1 |
| HRC_EVT_CONSTRUCT_METHS_PK1 | Unique | FUSION_TS_TX_DATA | CONSTRUCTION_METHOD_ID, ORA_SEED_SET2 |
| HRC_EVT_CONSTRUCT_METHS_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, EDL_NAMESPACE, PUBLISHED_EVENT_NAME, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_EVT_CONSTRUCT_METHS_U11 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, EDL_NAMESPACE, PUBLISHED_EVENT_NAME, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
