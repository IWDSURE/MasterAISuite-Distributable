# PAY_TMPLT_DSGN_PTRN

This holds various design patterns available for a given functional area. E.g. An Element Template might have various patterns for how the back dated payment is made. This will allow the legislation or the customer to pick the pattern that is suitable to them.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltdsgnptrn-30228.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paytmpltdsgnptrn-30228.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_TMPLT_DSGN_PTRN_PK | PATTERN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PATTERN_ID | NUMBER |  | 18 | Yes | PATTERN_ID |
| PATTERN_NAME | VARCHAR2 | 30 |  | Yes | PATTERN_NAME |
| BASE_PATTERN_NAME | VARCHAR2 | 30 |  | Yes | BASE_PATTERN_NAME |
| MODULE_ID | VARCHAR2 | 32 |  |  | Seed Data Framework: indicates the module that owns the row. A module is an entry in Application Taxonomy such as a Logical Business Area. When the MODULE_ID column exists and the owner of the row is not specified, then the Seed Data Framework will not extract the row as seed data. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 |  | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Foreign key to FND_TERRITORIES. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_TMPLT_DSGN_PTRN_PK | Unique | Default | PATTERN_ID |
| PAY_TMPLT_DSGN_PTRN_U1 | Unique | Default | BASE_PATTERN_NAME, LEGISLATIVE_DATA_GROUP_ID, LEGISLATION_CODE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
