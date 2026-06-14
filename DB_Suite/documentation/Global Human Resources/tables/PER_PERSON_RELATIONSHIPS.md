# PER_PERSON_RELATIONSHIPS

This table is used to store the relationship details of a person with respect to another person in the system.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonrelationships-29939.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpersonrelationships-29939.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PERSON_RELATIONSHIPS_PK | PERSON_RELATIONSHIP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | System-generated primary key column. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person. |
| RELATED_PERSON_ID | NUMBER |  | 18 | Yes | Identifier of the person to whom the relationship is defined. |
| RELATIONSHIP_TYPE | VARCHAR2 | 30 |  | Yes | Type of relationship defined for the record. |
| RELATIONSHIP_STRENGTH | NUMBER |  | 3 |  | Identifies the strength of the relationship. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PERSON_RELATIONSHIPS_FK2 | Non Unique | Default | RELATED_PERSON_ID |
| PER_PERSON_RELATIONSHIPS_PK | Unique | Default | PERSON_RELATIONSHIP_ID |
| PER_PERSON_RELATIONSHIPS_U1 | Unique | Default | PERSON_ID, RELATED_PERSON_ID, RELATIONSHIP_TYPE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
