# BEN_ACA_REPORTING

BEN_ACA_REPORTING contains information related to processing benefits reporting data .

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benacareporting-11281.html#benacareporting-11281](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/benacareporting-11281.html#benacareporting-11281)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ACA_REPORTING_PK | ACA_REPORTING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACA_REPORTING_ID | NUMBER |  | 18 | Yes | Column for Storage of the ACA_REPORTING_ID |
| PERSON_ID | NUMBER |  | 18 |  | Column for Storage of the PERSON_ID |
| DPNT_PERSON_ID | NUMBER |  | 18 |  | Column for Storage of the DPNT_PERSON_ID |
| YEAR | NUMBER |  | 18 |  | This Column is for Storage of the YEAR |
| EFFECTIVE_DATE | DATE |  |  |  | Column for Storage of the EFFECTIVE_DATE |
| BENFIT_RELATION_ID | NUMBER |  | 18 |  | Column for Storage of the BENFIT_RELATION_ID |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Column for Storage of the LEGAL_ENTITY_ID |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Column for Storage of the ASSIGNMENT_ID |
| BUSINESS_GROUP_ID | NUMBER |  | 18 |  | Column for Storage of the BUSINESS_GROUP_ID |
| ACA_FULL_PART_TIME | VARCHAR2 | 100 |  |  | Column for Storage of the ACA_FULL_PART_TIME |
| ACA_LINE_NO | VARCHAR2 | 100 |  |  | Column for Storage of the ACA_LINE_NO |
| ACA_CODE | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CODE |
| ACA_OVERRIDE_CODE | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_OVERRIDE_CODE |
| OVERRIDEN_BY | VARCHAR2 | 4000 |  |  | Column for Storage of the OVERRIDEN_BY |
| OVERRIDEN_DATE | DATE |  |  |  | Column for Storage of the OVERRIDEN_DATE |
| OVERRIDE_REASON | VARCHAR2 | 4000 |  |  | Column for Storage of the OVERRIDE_REASON |
| ACA_NUMBER1 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER1 |
| ACA_NUMBER2 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER2 |
| ACA_NUMBER3 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER3 |
| ACA_NUMBER4 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER4 |
| ACA_NUMBER5 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER5 |
| ACA_NUMBER6 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER6 |
| ACA_NUMBER7 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER7 |
| ACA_NUMBER8 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER8 |
| ACA_NUMBER9 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER9 |
| ACA_NUMBER10 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER10 |
| ACA_NUMBER11 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER11 |
| ACA_NUMBER12 | NUMBER |  |  |  | Column for Storage of the ACA_NUMBER12 |
| ACA_CHAR1 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR1 |
| ACA_CHAR2 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR2 |
| ACA_CHAR3 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR3 |
| ACA_CHAR4 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR4 |
| ACA_CHAR5 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR5 |
| ACA_CHAR6 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR6 |
| ACA_CHAR7 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR7 |
| ACA_CHAR8 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR8 |
| ACA_CHAR9 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR9 |
| ACA_CHAR10 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR10 |
| ACA_CHAR11 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR11 |
| ACA_CHAR12 | VARCHAR2 | 4000 |  |  | Column for Storage of the ACA_CHAR12 |
| ACA_DATE1 | DATE |  |  |  | Column for Storage of the ACA_DATE1 |
| ACA_DATE2 | DATE |  |  |  | Column for Storage of the ACA_DATE2 |
| ACA_DATE3 | DATE |  |  |  | Column for Storage of the ACA_DATE3 |
| ACA_DATE4 | DATE |  |  |  | Column for Storage of the ACA_DATE4 |
| ACA_DATE5 | DATE |  |  |  | Column for Storage of the ACA_DATE5 |
| ACA_DATE6 | DATE |  |  |  | Column for Storage of the ACA_DATE6 |
| ACA_DATE7 | DATE |  |  |  | Column for Storage of the ACA_DATE7 |
| ACA_DATE8 | DATE |  |  |  | Column for Storage of the ACA_DATE8 |
| ACA_DATE9 | DATE |  |  |  | Column for Storage of the ACA_DATE9 |
| ACA_DATE10 | DATE |  |  |  | Column for Storage of the ACA_DATE10 |
| ACA_DATE11 | DATE |  |  |  | Column for Storage of the ACA_DATE11 |
| ACA_DATE12 | DATE |  |  |  | Column for Storage of the ACA_DATE12 |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| REQUEST_ID | NUMBER |  | 18 |  | Enterprise Service Scheduler: indicates the request ID of the job that created or last updated the row. |
| JOB_DEFINITION_NAME | VARCHAR2 | 100 |  |  | Enterprise Service Scheduler: indicates the name of the job that created or last updated the row. |
| JOB_DEFINITION_PACKAGE | VARCHAR2 | 900 |  |  | Enterprise Service Scheduler: indicates the package name of the job that created or last updated the row. |
| PROGRAM_APP_NAME | VARCHAR2 | 30 |  |  | This column is for the storage of PROGRAM_APP_NAME |
| PROGRAM_NAME | VARCHAR2 | 30 |  |  | This column is for the storage of PROGRAM_NAME |
| PROGRAM_UPDATE_DATE | DATE |  |  |  | This column is for the storage of PROGRAM_UPDATE_DATE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ACA_REPORTING_N1 | Non Unique | Default | PERSON_ID |
| BEN_ACA_REPORTING_U1 | Unique | Default | ACA_REPORTING_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
