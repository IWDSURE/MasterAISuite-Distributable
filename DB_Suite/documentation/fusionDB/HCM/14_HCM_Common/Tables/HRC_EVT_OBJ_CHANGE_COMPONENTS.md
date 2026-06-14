# HRC_EVT_OBJ_CHANGE_COMPONENTS

An Source Object Change Component stores information about the date range over which a specific change takes place. In the case of a non-DE change there will be a single record with no Validation start/end dates. In the case of a DE change each individual change that is part of a series of changes brought about by the DE Operation will be captured.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchangecomponents-22122.html#hrcevtobjchangecomponents-22122](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchangecomponents-22122.html#hrcevtobjchangecomponents-22122)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_OBJ_CHG_CMPNTS_PK | CHANGE_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_COMPONENT_ID | NUMBER |  | 18 | Yes | Unique Identifier |
| CHANGE_ID | NUMBER |  | 18 | Yes | Identifier of the Change Instance |
| PHYSICAL_TYPE | VARCHAR2 | 30 |  | Yes | Indication that the component contains physical record changes |
| LOGICAL_TYPE | VARCHAR2 | 30 |  | Yes | Indication that the component contains logical record changes |
| VALIDATION_START_DATE | DATE |  |  |  | For DE entities the Validation Start Date of the affected change |
| VALIDATION_END_DATE | DATE |  |  |  | For DE entities the Validation End Date of the affected change |
| OLD_EFFECTIVE_START_DATE | DATE |  |  |  | Effective Start Date old value |
| NEW_EFFECTIVE_START_DATE | DATE |  |  |  | Effective Start Date new value |
| OLD_EFFECTIVE_END_DATE | DATE |  |  |  | Effective End Date old value |
| NEW_EFFECTIVE_END_DATE | DATE |  |  |  | Effective End Date new value |
| OLD_SEQUENCE | NUMBER |  | 9 |  | The old sequence number of the changed record in the case of Multiple Changes per Day |
| NEW_SEQUENCE | NUMBER |  | 9 |  | The new sequence number of the changed record in the case of Multiple Changes per Day |
| CHANGE_ATTRS | CLOB |  |  |  | Changed Attributes stored in the form of name and values |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_EVT_OBJ_CHG_CMPNTS_FK1 | Non Unique | FUSION_TS_TX_DATA | CHANGE_ID |
| HRC_EVT_OBJ_CHG_CMPNTS_PK | Unique | FUSION_TS_TX_DATA | CHANGE_COMPONENT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
