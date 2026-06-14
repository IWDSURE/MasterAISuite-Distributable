# PER_SEARCH_FILTER_MAPPINGS

Table to store public person security profile search filter mapping.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchfiltermappings-11327.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchfiltermappings-11327.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SEARCH_FILTER_MAPPINGS_PK | FILTER_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FILTER_MAPPING_ID | NUMBER |  | 18 | Yes | System generated primary key column. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_ID | NUMBER |  | 18 | Yes | Fnd object Id. |
| SECURITY_PROFILE_TYPE | VARCHAR2 | 30 |  |  | Security profile type. |
| SECURITY_PROFILE_ID | NUMBER |  | 18 | Yes | Security profile Id. |
| FILTER_ID | NUMBER |  | 18 | Yes | Filter Id. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_SEARCH_FILTER_MAPPINGS_FK1 | Non Unique | FUSION_TS_TX_DATA | SECURITY_PROFILE_ID |
| PER_SEARCH_FILTER_MAPPINGS_PK | Unique | FUSION_TS_TX_DATA | FILTER_MAPPING_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
