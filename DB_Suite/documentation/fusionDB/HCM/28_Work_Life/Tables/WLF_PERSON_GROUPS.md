# WLF_PERSON_GROUPS

Table to store of time based destination users

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpersongroups-16825.html#wlfpersongroups-16825](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfpersongroups-16825.html#wlfpersongroups-16825)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_PERSON_GROUPS_PK | PERSON_GROUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_GROUP_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| ASSIGNED_TO_ID | NUMBER |  | 18 | Yes | Indicates the assigned_to_id identifier of destination entry from wlf_assignment_destinations_f. |
| ASSIGNED_TO_TYPE | VARCHAR2 | 30 |  | Yes | Indicates the type of destination. |
| PERSON_ID | NUMBER |  | 18 | Yes | Indicate PersonId who is person in Destination. |
| JOB_RUN_DATE | DATE |  |  | Yes | Day on which the destination is processed. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_PERSON_GROUPS_N1 | Non Unique | Default | ASSIGNED_TO_ID, ASSIGNED_TO_TYPE |
| WLF_PERSON_GROUPS_N2 | Non Unique | Default | JOB_RUN_DATE |
| WLF_PERSON_GROUPS_U1 | Unique | Default | PERSON_GROUP_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
