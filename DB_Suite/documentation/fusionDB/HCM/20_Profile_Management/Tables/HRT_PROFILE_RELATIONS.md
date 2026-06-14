# HRT_PROFILE_RELATIONS

This table relates the model profiles with actual model entities like job,position etc.

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilerelations-20712.html#hrtprofilerelations-20712](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtprofilerelations-20712.html#hrtprofilerelations-20712)

## Primary Key

| Name | Columns |
|------|----------|
| HRT_PROFILE_RELATIONS_PK | PROFILE_RELATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROFILE_RELATION_ID | NUMBER |  | 18 | Yes | System generated primary key |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_PROFILES_B |
| RELATION_ID | NUMBER |  | 18 | Yes | Foreign Key to HRT_RELATION_CONFIG_B |
| OBJECT_ID | NUMBER |  | 18 | Yes | Contains the id of the actual model entity i.e., job_id or position_id |
| OBJECT_EFF_START_DATE | DATE |  |  |  | Effective Start Date |
| OBJECT_EFF_END_DATE | DATE |  |  |  | Effective End Date |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRT_PROFILE_RELATIONS_N1 | Non Unique | Default | RELATION_ID, PROFILE_ID, OBJECT_ID |
| HRT_PROFILE_RELATIONS_N2 | Non Unique | Default | OBJECT_ID |
| HRT_PROFILE_RELATIONS_N3 | Non Unique | Default | PROFILE_ID |
| HRT_PROFILE_RELATIONS_PK | Unique | Default | PROFILE_RELATION_ID |

---

[← Back to Index](../20_Profile_Management_Tables_Index.md)
