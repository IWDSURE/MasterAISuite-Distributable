# PER_ACL_EXCLUSIONS

Stores exclusions for Oracle Search ACL computation.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraclexclusions-25857.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/peraclexclusions-25857.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ACL_EXCLUSIONS_PK | ACL_EXCLUSION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ACL_EXCLUSION_ID | NUMBER |  | 18 | Yes | Mandatory Primary Key. Updatable while new key generation. |
| EXCLUSION_TYPE | VARCHAR2 | 30 |  | Yes | The Oracle Search exclusion type for excluding items during ACL computation. |
| USER_ID | NUMBER |  | 18 |  | The user id of the user the exclusion is for (if available). |
| ROLE_ID | NUMBER |  | 18 |  | The role id of the user the exclusion is for (if available). |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_ACL_EXCLUSIONS_N1 | Non Unique | Default | EXCLUSION_TYPE |
| PER_ACL_EXCLUSIONS_U1 | Unique | Default | ACL_EXCLUSION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
