# PER_SEARCH_OBJECTS

This table holds named query statements used to populate the table PER_KEYWORDS. The statements are maintained by external consumers of Person Search and are used by consumers to add their keywords to PER_KEYWORDS for subsequently searching for people by keywords.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** REFERENCE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchobjects-24925.html#persearchobjects-24925](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persearchobjects-24925.html#persearchobjects-24925)

## Primary Key

| Name | Columns |
|------|----------|
| PER_SEARCH_OBJECT_PK | SEARCH_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEARCH_OBJECT_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| SEARCH_OBJECT_NAME | VARCHAR2 | 255 |  | Yes | Object Identifier |
| APPLICATION_ID | NUMBER |  | 18 |  | References FND_APPLICATIONS |
| SEARCH_OBJECT_QUERY | CLOB |  |  |  | actual query |
| SECURED | VARCHAR2 | 1 |  |  | This identifies whether keywords for this query is secured or not. |
| STATUS | VARCHAR2 | 1 |  |  | Active/Inactive allows consumers to remove. |
| LAST_CRAWL_TS | TIMESTAMP |  |  |  | Last time the data was crawled. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| SGUID | VARCHAR2 | 32 |  |  | The seed global unique identifier. Oracle internal use only. |
| SEED_DATA_SOURCE | VARCHAR2 | 512 |  |  | Source of seed data record. A value of 'BULK_SEED_DATA_SCRIPT' indicates that record was bulk loaded. Otherwise, specifies the name of the seed data file. |
| ORA_SEED_SET1 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET1. Context values are Y or N. |
| ORA_SEED_SET2 | VARCHAR2 | 1 |  | Yes | Oracle internal use only. Indicates the edition-based redefinition (EBR) context of the row for SET2. Context values are Y or N. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_SEARCH_OBJECTS_N20 | Non Unique | Default | SGUID |
| PER_SEARCH_OBJECT_PK | Unique | Default | SEARCH_OBJECT_ID, ORA_SEED_SET1 |
| PER_SEARCH_OBJECT_PK1 | Unique | Default | SEARCH_OBJECT_ID, ORA_SEED_SET2 |
| PER_SEARCH_OBJECT_U1 | Unique | Default | SEARCH_OBJECT_NAME, APPLICATION_ID, ORA_SEED_SET1 |
| PER_SEARCH_OBJECT_U11 | Unique | Default | SEARCH_OBJECT_NAME, APPLICATION_ID, ORA_SEED_SET2 |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
