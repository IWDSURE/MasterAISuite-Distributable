# PER_LOC_SEC_PROFILE_LOCATIONS

Location Security Profile Locations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocsecprofilelocations-29140.html#perlocsecprofilelocations-29140](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocsecprofilelocations-29140.html#perlocsecprofilelocations-29140)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOC_SEC_PROFILE_LOC_PK | LOC_SEC_PROFILE_LOCATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOC_SEC_PROFILE_LOCATION_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| LOCATION_SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_LOCATION_SECURITY_PROFILES  table. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| INCLUDE_EXCLUDE_FLAG | VARCHAR2 | 1 |  | Yes | Location security profiles are not in use - leave blank |
| LOCATION_ID | NUMBER |  | 18 | Yes | Foreign Key to PER_LOCATIONS table. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_LOC_SEC_PROFILE_LOC_FK1 | Non Unique | FUSION_TS_TX_DATA | LOCATION_SECURITY_PROFILE_ID |
| PER_LOC_SEC_PROFILE_LOC_PK | Unique | FUSION_TS_TX_DATA | LOC_SEC_PROFILE_LOCATION_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
