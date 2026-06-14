# HRC_EVT_ATTRIBUTE_ARCHIVE_REQS

An Archive Attribute identifies that a particular entity object attribute or PLSQL row handler column should be stored in the Source Object Change tables. There is the option to always store the column/attribute value regardless of whether the value changed or to only store it when its value changes. In addition it is possible to indicate whether both Old and New values are required.
N.B. If no archive attribute records are created, then a detected event will still be stored in the Source Object Change tables, however there will be no attribute data stored The data that will be stored in this case will be the primary key data and, in the case of date effective change, the date ranges over which the changes took place.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtattributearchivereqs-31194.html#hrcevtattributearchivereqs-31194](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtattributearchivereqs-31194.html#hrcevtattributearchivereqs-31194)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_ATTR_ARCH_REQS_PK | ATTRIBUTE_ARCHIVE_REQ_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ATTRIBUTE_ARCHIVE_REQ_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| EVENT_TYPE_ID | NUMBER |  | 18 | Yes | Identifier of Event Type |
| SOURCE_OBJECT_ATTRIBUTE_ID | NUMBER |  | 18 | Yes | Identifier of Source Object Attribute |
| CHANGED_ALWAYS | VARCHAR2 | 30 |  | Yes | Indication of whether the value should always be stored or only when changed. Values must be either "ALWAYS" or "CHANGED" |
| OLD_VALUE | VARCHAR2 | 30 |  | Yes | Indication of whether the Old Value should be stored |
| NEW_VALUE | VARCHAR2 | 30 |  | Yes | Indication of whether the New Value should be stored |
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
| HRC_EVT_ATTRIBUTE_ARCHIVE_N20 | Non Unique | Default | SGUID |
| HRC_EVT_ATTR_ARCH_REQS_F2 | Non Unique | FUSION_TS_TX_DATA | SOURCE_OBJECT_ATTRIBUTE_ID |
| HRC_EVT_ATTR_ARCH_REQS_PK | Unique | FUSION_TS_TX_DATA | ATTRIBUTE_ARCHIVE_REQ_ID, ORA_SEED_SET1 |
| HRC_EVT_ATTR_ARCH_REQS_PK1 | Unique | FUSION_TS_TX_DATA | ATTRIBUTE_ARCHIVE_REQ_ID, ORA_SEED_SET2 |
| HRC_EVT_ATTR_ARCH_REQS_U1 | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, SOURCE_OBJECT_ATTRIBUTE_ID, ORA_SEED_SET1 |
| HRC_EVT_ATTR_ARCH_REQS_U11 | Unique | FUSION_TS_TX_DATA | EVENT_TYPE_ID, SOURCE_OBJECT_ATTRIBUTE_ID, ORA_SEED_SET2 |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
