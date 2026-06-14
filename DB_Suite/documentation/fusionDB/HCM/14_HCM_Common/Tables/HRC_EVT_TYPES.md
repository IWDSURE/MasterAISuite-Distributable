# HRC_EVT_TYPES

An Event Type identifies a significant change on a data object or a particular trigger point within a process flow. It can be further qualified by Event Conditions and is used to detect the points at which subsequent processing should be invoked.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevttypes-16833.html#hrcevttypes-16833](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevttypes-16833.html#hrcevttypes-16833)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_TYPES_PK | EVENT_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| EVENT_TYPE_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| SOURCE_OBJECT_ID | NUMBER |  | 18 | Yes | Identifier of Source Object |
| NAME | VARCHAR2 | 80 |  | Yes | Name of the event type |
| DESCRIPTION | VARCHAR2 | 240 |  |  | Description of the event type |
| TRIGGER_POINT | VARCHAR2 | 30 |  |  | Event triggering point relating to the supported trigger points with transaction based business processes |
| DML_TYPE | VARCHAR2 | 30 |  |  | For Entity Object and PLSQL based event types, the DML Mode that will trigger the event |
| DATE_EFFECTIVE_OPERATION | VARCHAR2 | 240 |  |  | For Date Effective entity object based events, the "logical" date effective operation that will trigger the event |
| GROOVY_RULE | VARCHAR2 | 2000 |  |  | A Groovy expression that will refer to the attributes of an Entity Object |
| JAVA_RULE | VARCHAR2 | 80 |  |  | A Java method that can accept either an Entity Object or a Root AM, depending on the parent event type |
| PLSQL_RULE | VARCHAR2 | 80 |  |  | A PLSQL function that can be used to filter the PLSQL row handler based events |
| ENABLED | VARCHAR2 | 30 |  | Yes | Indicator of whether the event type is currently enabled |
| PROTECTED_FLAG | VARCHAR2 | 30 |  | Yes | Indicator that the event has been used by an application that depends on the event definition not changing in the future. It will prevent the event type from being deleted and the conditions from changing. |
| STORAGE_DURATION | NUMBER |  | 9 | Yes | Number of days that the event audit data should be stored before it can be purged |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| EVENT_TYPE | VARCHAR2 | 30 |  | Yes | Discriminator to determine the event type |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_TYPES_F1 | Non Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ID |
| HRC_EVT_TYPES_F2 | Non Unique | FUSION_TS_TX_DATA | ENTERPRISE_ID |
| HRC_EVT_TYPES_N1 | Non Unique | Default | UPPER("NAME") |
| HRC_EVT_TYPES_N20 | Non Unique | Default | SGUID |
| HRC_EVT_TYPES_PK | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, ORA_SEED_SET1 |
| HRC_EVT_TYPES_PK1 | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, ORA_SEED_SET2 |
| HRC_EVT_TYPES_U1 | Unique | FUSION_TS_TX_DATA | NAME, ENTERPRISE_ID, ORA_SEED_SET1 |
| HRC_EVT_TYPES_U11 | Unique | FUSION_TS_TX_DATA | NAME, ENTERPRISE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
