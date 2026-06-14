# WLF_LM_MANDATORY_ENR_REQUESTS

This table is used to store mandatory Enrollment request objects

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmmandatoryenrrequests-19453.html#wlflmmandatoryenrrequests-19453](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmmandatoryenrrequests-19453.html#wlflmmandatoryenrrequests-19453)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_MANDATORY_ENR_REQS_PK | MANDATORY_ENR_REQUEST_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| MANDATORY_ENR_REQUEST_ID | NUMBER |  | 18 | Yes | MANDATORY_ENR_REQUEST_ID |
| REQUESTOR_ID | NUMBER |  | 18 | Yes | REQUESTOR_ID |
| CLASS_ID | NUMBER |  | 18 | Yes | CLASS_ID |
| ENR_PREREQ_TYPE | VARCHAR2 | 30 |  | Yes | ENR_PREREQ_TYPE |
| PERSON_ID | NUMBER |  | 18 | Yes | PERSON_ID |
| ORGANIZATION_ID | NUMBER |  | 18 | Yes | ORGANIZATION_ID |
| ORG_STRUCTURE_VERSION_ID | NUMBER |  | 18 | Yes | ORG_STRUCTURE_VERSION_ID |
| JOB_ID | NUMBER |  | 18 | Yes | JOB_ID |
| POSITION_ID | NUMBER |  | 18 | Yes | POSITION_ID |
| USERGROUP_ID | NUMBER |  | 18 | Yes | USERGROUP_ID |
| CONC_PROGRAM_REQUEST_ID | NUMBER |  | 18 | Yes | CONC_PROGRAM_REQUEST_ID |
| CERTIFICATION_ID | NUMBER |  | 18 | Yes | CERTIFICATION_ID |
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
| WLF_LM_MAND_ENR_REQUESTS_U1 | Unique | Default | MANDATORY_ENR_REQUEST_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
