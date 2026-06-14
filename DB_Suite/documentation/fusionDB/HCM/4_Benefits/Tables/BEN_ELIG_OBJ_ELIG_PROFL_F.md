# BEN_ELIG_OBJ_ELIG_PROFL_F

Holds the eligibility profiles that are attached to a particular Object

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligobjeligproflf-20288.html#beneligobjeligproflf-20288](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/beneligobjeligproflf-20288.html#beneligobjeligproflf-20288)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_ELIG_OBJ_ELIG_PROFL_PK | ELIG_OBJ_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELIG_OBJ_ELIG_PRFL_ID | NUMBER |  | 18 | Yes | Primary Key |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ELIG_OBJ_ID | NUMBER |  | 18 | Yes | Eligibility Object for which profiles are attached |
| ELIG_PRFL_ID | NUMBER |  | 18 | Yes | Eligibility Profile |
| MNDTRY_FLAG | VARCHAR2 | 1 |  | Yes | Whether the profile is Mandatory or not |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | business group id |
| BEP_ATTRIBUTE_CATEGORY | VARCHAR2 | 150 |  |  | Descriptive Flex Structure defining column |
| BEP_ATTRIBUTE1 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE2 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE3 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE4 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE5 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE6 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE7 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE8 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE9 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE10 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE11 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE12 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE13 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE14 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE15 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE16 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE17 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE18 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE19 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| BEP_ATTRIBUTE20 | VARCHAR2 | 30 |  |  | Descriptive Flex attribute |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_ELIG_OBJ_ELIG_PROFL_F_N1 | Non Unique | Default | ELIG_OBJ_ID |
| BEN_ELIG_OBJ_ELIG_PROFL_F_PK | Unique | Default | ELIG_OBJ_ELIG_PRFL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
