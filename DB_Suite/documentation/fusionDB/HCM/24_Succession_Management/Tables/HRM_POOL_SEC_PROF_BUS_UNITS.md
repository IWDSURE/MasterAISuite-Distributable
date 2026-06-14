# HRM_POOL_SEC_PROF_BUS_UNITS

Table to store business units added in a talent pool security profile.

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecprofbusunits-8566.html#hrmpoolsecprofbusunits-8566](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmpoolsecprofbusunits-8566.html#hrmpoolsecprofbusunits-8566)

## Primary Key

| Name | Columns |
|------|----------|
| HRM_POOL_SEC_PROF_BUS_UNIT_PK | POOL_SEC_PROF_BUS_UNIT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POOL_SEC_PROF_BUS_UNIT_ID | NUMBER |  | 18 | Yes | Pool security profile business unit id uniquely identifies the businessunits added to security profile. |
| POOL_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Forigen key column for hrm_pool_security_profiles table. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. |
| BUSINESS_UNIT_ID | NUMBER |  | 18 | Yes | Selected business unit id in the talent pool security profile. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRM_POOL_SEC_PROF_BUS_UNIT_PK | Unique | FUSION_TS_TX_DATA | POOL_SEC_PROF_BUS_UNIT_ID |
| HRM_POOL_SEC_PROF_BUS_UNIT_U1 | Unique | FUSION_TS_TX_DATA | POOL_SECURITY_PROFILE_ID, BUSINESS_UNIT_ID |

---

[← Back to Index](../24_Succession_Management_Tables_Index.md)
