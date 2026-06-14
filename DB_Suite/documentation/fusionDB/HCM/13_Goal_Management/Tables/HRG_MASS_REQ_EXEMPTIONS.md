# HRG_MASS_REQ_EXEMPTIONS

Stores the details of workers who will be exempted from "Goal mass assignment" process.

## Details

**Schema:** FUSION

**Object owner:** HRG

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqexemptions-11629.html#hrgmassreqexemptions-11629](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrgmassreqexemptions-11629.html#hrgmassreqexemptions-11629)

## Primary Key

| Name | Columns |
|------|----------|
| HRG_MASS_REQ_EXEMPTIONS_PK | MASS_REQUEST_EXEMPTION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MASS_REQUEST_EXEMPTION_ID | NUMBER |  | 18 | Yes | MASS_REQUEST_EXEMPTION_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| MASS_REQUEST_ID | NUMBER |  | 18 | Yes | MASS_REQUEST_ID |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 | Yes | ASSIGNMENT_ID |
| CASCADING_LEVEL | NUMBER |  | 18 |  | CASCADING_LEVEL |
| MASS_REQUEST_HIERARCHY_ID | NUMBER |  | 18 | Yes | MASS_REQUEST_HIERARCHY_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRG_MASS_REQ_EXEMPTIONS_U1 | Unique | Default | MASS_REQUEST_EXEMPTION_ID |

---

[← Back to Index](../13_Goal_Management_Tables_Index.md)
