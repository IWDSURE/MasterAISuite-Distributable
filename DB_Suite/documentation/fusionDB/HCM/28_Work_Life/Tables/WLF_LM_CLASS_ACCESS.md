# WLF_LM_CLASS_ACCESS

This table is used to manage the access to the class objects

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassaccess-7734.html#wlflmclassaccess-7734](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmclassaccess-7734.html#wlflmclassaccess-7734)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LM_CLASS_ACCESS_PK | CLASS_ACCESS_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CLASS_ACCESS_ID | NUMBER |  | 18 | Yes | CLASS_ACCESS_ID |
| CLASS_ID | NUMBER |  | 18 |  | CLASS_ID |
| ORGANIZATION_ID | NUMBER |  | 18 |  | ORGANIZATION_ID |
| JOB_ID | NUMBER |  | 18 |  | JOB_ID |
| POSITION_ID | VARCHAR2 | 18 |  |  | POSITION_ID |
| CUSTOMER_ID | NUMBER |  | 18 |  | CUSTOMER_ID |
| COMMENTS | VARCHAR2 | 2000 |  |  | COMMENTS |
| CATEGORY_ID | NUMBER |  | 18 |  | CATEGORY_ID |
| COURSE_ID | NUMBER |  | 18 |  | COURSE_ID |
| SELF_ENROLLMENT_FLAG | VARCHAR2 | 30 |  |  | SELF_ENROLLMENT_FLAG |
| MATCH_TYPE | VARCHAR2 | 30 |  |  | MATCH_TYPE |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PARTY_ID | NUMBER |  | 18 |  | PARTY_ID |
| LEARNING_PATH_ID | NUMBER |  | 18 |  | LEARNING_PATH_ID |
| FORUM_ID | NUMBER |  | 18 |  | FORUM_ID |
| CHAT_ID | NUMBER |  | 18 |  | CHAT_ID |
| CERTIFICATION_ID | NUMBER |  | 18 |  | CERTIFICATION_ID |
| ORG_STRUCTURE_VERSION_ID | NUMBER |  | 18 |  | ORG_STRUCTURE_VERSION_ID |
| MANDATORY_ENROLLMENT_FLAG | VARCHAR2 | 30 |  |  | MANDATORY_ENROLLMENT_FLAG |
| MANDATORY_ENROLLMENT_PREREQ | VARCHAR2 | 30 |  |  | MANDATORY_ENROLLMENT_PREREQ |
| USER_GROUP_ID | NUMBER |  | 18 |  | USER_GROUP_ID |
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
| WLF_LM_CLASS_ACCESS_N50 | Non Unique | Default | CUSTOMER_ID |
| WLF_LM_CLASS_ACCESS_N51 | Non Unique | Default | ORGANIZATION_ID |
| WLF_LM_CLASS_ACCESS_N52 | Non Unique | Default | JOB_ID |
| WLF_LM_CLASS_ACCESS_N53 | Non Unique | Default | POSITION_ID |
| WLF_LM_CLASS_ACCESS_N54 | Non Unique | Default | PERSON_ID |
| WLF_LM_CLASS_ACCESS_N55 | Non Unique | Default | LEARNING_PATH_ID |
| WLF_LM_CLASS_ACCESS_N56 | Non Unique | Default | PARTY_ID |
| WLF_LM_CLASS_ACCESS_N57 | Non Unique | Default | CATEGORY_ID |
| WLF_LM_CLASS_ACCESS_N58 | Non Unique | Default | COURSE_ID |
| WLF_LM_CLASS_ACCESS_N59 | Non Unique | Default | FORUM_ID |
| WLF_LM_CLASS_ACCESS_N60 | Non Unique | Default | CHAT_ID |
| WLF_LM_CLASS_ACCESS_N61 | Non Unique | Default | CERTIFICATION_ID |
| WLF_LM_CLASS_ACCESS_N63 | Non Unique | Default | LAST_UPDATE_DATE |
| WLF_LM_CLASS_ACCESS_U1 | Unique | Default | CLASS_ACCESS_ID |
| WLF_LM_CLASS_ACCESS_U2 | Unique | Default | CLASS_ID, CUSTOMER_ID, ORGANIZATION_ID, JOB_ID, POSITION_ID, LEARNING_PATH_ID, CATEGORY_ID, COURSE_ID, PERSON_ID, PARTY_ID, FORUM_ID, CHAT_ID, CERTIFICATION_ID, USER_GROUP_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
