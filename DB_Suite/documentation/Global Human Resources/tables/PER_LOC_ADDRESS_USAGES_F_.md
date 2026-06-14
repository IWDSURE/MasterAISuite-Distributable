# PER_LOC_ADDRESS_USAGES_F_

PER_LOC_ADDRESS_USAGES_F stores the Address Type for an Address associated with a Location

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocaddressusagesf-13548.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocaddressusagesf-13548.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_LOC_ADDRESS_USAGES_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOC_ADDRESS_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LOC_ADDRESS_USAGE_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ADDRESS_USAGE_TYPE | VARCHAR2 | 30 |  |  | Type of Address Usage at the location. |
| LOCATION_ID | NUMBER |  | 18 |  | Foreign Key to PER_LOCATIONS table. |
| ADDRESS_ID | NUMBER |  | 18 |  | Foreign Key to PER_ADDRESSES table. |
| ACTION_OCCURRENCE_ID | NUMBER |  | 18 |  | Foreign Key to PER_ACTION_OCCURRENCES. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |
| AUDIT_IMPERSONATOR_ | VARCHAR2 | 64 |  |  | Who column: indicates the impersonator who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_LOC_ADDRESS_USAGES_FN1_ | Non Unique | Default | LOC_ADDRESS_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOC_ADDRESS_USAGES_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOC_ADDRESS_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOC_ADDRESS_USAGES_U1_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID, ADDRESS_USAGE_TYPE, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOC_ADDRESS_USAGES_U2_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, LOCATION_ID, ADDRESS_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PER_LOC_ADDRESS_USAGES_U3_ | Unique | Default | LAST_UPDATED_BY, LAST_UPDATE_DATE, LOC_ADDRESS_USAGE_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
