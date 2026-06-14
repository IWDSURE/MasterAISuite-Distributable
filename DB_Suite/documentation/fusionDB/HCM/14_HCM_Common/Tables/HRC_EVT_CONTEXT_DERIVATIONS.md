# HRC_EVT_CONTEXT_DERIVATIONS

A context derivation method identifies the mechanism that will be used to derive a context value when processing a particular event object. The context can either be derived from a named EO attribute, including transient attributes, a PLSQL row handler parameter or by using a Java method which is based on a business process root application module.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtcontextderivations-14102.html#hrcevtcontextderivations-14102](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtcontextderivations-14102.html#hrcevtcontextderivations-14102)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_CTX_DERIVATIONS_PK | CONTEXT_DERIVATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTEXT_DERIVATION_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Unique Identifier of Source Object |
| CONTEXT_TYPE | VARCHAR2 | 30 |  | Yes | Context Type, e.g. Legislation Code, Enterprise ID |
| TYPE | VARCHAR2 | 30 |  | Yes | Type of context derivation, values are "ATTRIBUTE", "METHOD", "SERVICE" |
| SOURCE_OBJECT_ATTRIBUTE_ID | NUMBER |  | 18 |  | Unique Identifier of the entity attribute or PLSQL column that contains the context |
| CLASS_NAME | VARCHAR2 | 80 |  |  | Name of the Java Class that contains the derivation method |
| METHOD_NAME | VARCHAR2 | 80 |  |  | Name of method used to derive the context |
| PLSQL_FUNCTION | VARCHAR2 | 80 |  |  | Name of PLSQL packaged function that should be executed to derive the context |
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
| HRC_EVT_CONTEXT_DERIVATIO_N20 | Non Unique | Default | SGUID |
| HRC_EVT_CTX_DERIVATIONS_F2 | Non Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ATTRIBUTE_ID |
| HRC_EVT_CTX_DERIVATIONS_PK | Unique | FUSION_TS_TX_DATA | CONTEXT_DERIVATION_ID, ORA_SEED_SET1 |
| HRC_EVT_CTX_DERIVATIONS_PK1 | Unique | FUSION_TS_TX_DATA | CONTEXT_DERIVATION_ID, ORA_SEED_SET2 |
| HRC_EVT_CTX_DERIVATIONS_U1 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, CONTEXT_TYPE, ORA_SEED_SET1 |
| HRC_EVT_CTX_DERIVATIONS_U11 | Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID, CONTEXT_TYPE, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
