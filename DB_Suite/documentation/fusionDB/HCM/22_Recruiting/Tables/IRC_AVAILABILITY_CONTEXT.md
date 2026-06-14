# IRC_AVAILABILITY_CONTEXT

This table is used to store the configuration data for availability context in recruiting. Each row represents a dimension value in a context.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailabilitycontext-4843.html#ircavailabilitycontext-4843](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailabilitycontext-4843.html#ircavailabilitycontext-4843)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AVAILABILITY_CONTEXT_PK | OBJECT_CTX_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_CTX_ID | NUMBER |  | 18 | Yes | Primary Key - Sequence generated key. Fusion Global sequence generator is used to generate the key at run-time. |
| OBJECT_CTX_CODE | VARCHAR2 | 36 |  | Yes | Object Context Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments |
| OBJECT_ID | NUMBER |  | 18 | Yes | Business Object ID - It can be CSP ID / Apply Flow ID / Content Library Id .. etc |
| OBJECT_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Business Object Type - It can be ORA_CSP or ORA_APPLY_FLOW or ORA_CONTENT_LIBRARY .. etc depends on the business object type |
| RECRUITING_TYPE_CODE | VARCHAR2 | 30 |  |  | Recruiting Type Code |
| ORGANIZATION_ID | NUMBER |  | 18 |  | Organization Id |
| GEOGRAPHY_NODE_ID | NUMBER |  | 18 |  | Geography Node Id |
| JOB_ID | NUMBER |  | 18 |  | Job ID |
| JOB_FAMILY_ID | NUMBER |  | 18 |  | Job Family Id |
| JOB_FUNCTION_CODE | VARCHAR2 | 30 |  |  | Job Function Code |
| SITE_NUMBER | VARCHAR2 | 240 |  |  | Career Site Number refers to IRC_CX_SITES_B.SITE_NUMBER column and defines career site dimension of availability context |
| PERSON_TYPE_CODE | VARCHAR2 | 30 |  |  | Person Type Code |
| DIMENSION_TYPE_CODE | VARCHAR2 | 30 |  |  | Dimension Type Code - E.g Values :  ORA_RECRUITING_TYPE , ORA_JOB_FAMILY, ORA_JOB_FUNCTION, ORA_LOCATION, ORA_ORGANIZATION, ORA_PERSON_TYPE |
| DEFAULT_FLAG | VARCHAR2 | 1 |  |  | Default Flag - Values are 'Y' or 'N' |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AVAILABILITY_CONTEXT_N1 | Non Unique | Default | OBJECT_ID, OBJECT_TYPE_CODE |
| IRC_AVAILABILITY_CONTEXT_U1 | Unique | Default | OBJECT_CTX_ID |
| IRC_AVAILABILITY_CONTEXT_U2 | Unique | Default | OBJECT_CTX_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
