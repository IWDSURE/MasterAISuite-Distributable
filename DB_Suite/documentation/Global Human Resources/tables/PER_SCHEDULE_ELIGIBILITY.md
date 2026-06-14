# PER_SCHEDULE_ELIGIBILITY

This Table stores the eligibility profiles associated to schedules

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleeligibility-19299.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perscheduleeligibility-19299.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SCHEDULE_ELIGIBILITY_PK | SCHEDULE_ELIGIBILITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| SCHEDULE_ELIGIBILITY_ID | NUMBER |  | 18 | Yes | Primary Key for Schedule Eligibility |  |
| SCHEDULE_ID | NUMBER |  | 18 | Yes | Schedule Id for the referenced Schedule |  |
| ELIGIBILITY_PROFILE_ID | NUMBER |  | 18 | Yes | Eligibility Profile Id of the referenced Eligibility Profile | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SCHEDULE_ELIGIBILITY_N1 | Non Unique | FUSION_TS_TX_IDX | SCHEDULE_ID |
| PER_SCHEDULE_ELIGIBILITY_U1 | Unique | FUSION_TS_TX_IDX | SCHEDULE_ELIGIBILITY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
