# HRC_EVT_OBJ_CHANGES

A Source Object Change Instancet identifies a particular entity object or PLSQL row handler record that changed as part of a transaction. The PK1 - PK9 values correspond to the Source Object Attribute record PRIMARY_KEY and PK_SEQ columns.
N.B. The Effective Dates of a date effective EO are not stored in this table, only the primary key of the logical DE entity.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchanges-3080.html#hrcevtobjchanges-3080](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcevtobjchanges-3080.html#hrcevtobjchanges-3080)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_EVT_OBJ_CHANGES_PK | CHANGE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHANGE_ID | NUMBER |  | 18 | Yes | Identifier of Change Instance |
| SOURCE_OBJECT_NAME | VARCHAR2 | 240 |  |  | Name of the Source Object |
| CHANGE_GROUP_ID | NUMBER |  | 18 |  | Identifier of a set of Object Changes that are related to each other |
| CHANGE_GROUP_SEQUENCE | NUMBER |  | 18 |  | Sequence of the Object Change within a group of related changes |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign key to Action Occurrence |
| OPERATION_TYPE | VARCHAR2 | 240 |  | Yes | The type of Operation that brought about the Event Audit. In the case of a non-Date Effective entity this will simply be the DML Mode. In the case of a DE entity it will be one of the set of DE Operations. |
| DATE_EFFECTIVE_MODE | VARCHAR2 | 240 |  |  | For Date Effective entities the date effective mode or pseudo mode used to create the change. |
| VALIDATION_START_DATE | DATE |  |  |  | Start of date range over which the changes occurred (DE entities only) |
| VALIDATION_END_DATE | DATE |  |  |  | End of date range over which the changes occurred (DE entities only) |
| EFFECTIVE_DATE | DATE |  |  |  | For DE entities, the Effective Date of the change |
| PK1_NAME | VARCHAR2 | 80 |  |  | Name of Primary Key 1 |
| PK1_DATA_TYPE | VARCHAR2 | 30 |  |  | Data Type of Primary Key 1 |
| PK1_VALUE_V | VARCHAR2 | 2000 |  |  | Varchar2 value of Primary Key 1 |
| PK1_VALUE_N | NUMBER |  | 18 |  | Number value of Primary Key 1 |
| PK1_VALUE_D | DATE |  |  |  | Date value of Primary Key 1 |
| PK2_NAME | VARCHAR2 | 80 |  |  | Name of Primary Key 2 |
| PK2_DATA_TYPE | VARCHAR2 | 30 |  |  | Data Type of Primary Key 2 |
| PK2_VALUE_V | VARCHAR2 | 2000 |  |  | Varchar2 value of Primary Key 2 |
| PK2_VALUE_N | NUMBER |  | 18 |  | Number value of Primary Key 2 |
| PK2_VALUE_D | DATE |  |  |  | Date value of Primary Key 2 |
| PK3_NAME | VARCHAR2 | 80 |  |  | Name of Primary Key 3 |
| PK3_DATA_TYPE | VARCHAR2 | 30 |  |  | Data Type of Primary Key 3 |
| PK3_VALUE_V | VARCHAR2 | 2000 |  |  | Varchar2 value of Primary Key 3 |
| PK3_VALUE_N | NUMBER |  | 18 |  | Number value of Primary Key 3 |
| PK3_VALUE_D | DATE |  |  |  | Date value of Primary Key 3 |
| PURGE_DATE | DATE |  |  | Yes | Date on which the Event Audit data can be purged |
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
| HRC_EVT_OBJ_CHANGES_PK | Unique | FUSION_TS_TX_DATA | CHANGE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
