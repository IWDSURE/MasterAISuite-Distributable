# IRC_AVAIL_CXT_JOB_FAM

This table is used to store the configuration data for availability context of dimension job family. Each row represents a dimension value in a context.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailcxtjobfam-13182.html#ircavailcxtjobfam-13182](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircavailcxtjobfam-13182.html#ircavailcxtjobfam-13182)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AVAIL_CXT_JOB_FAM_PK | OBJECT_CXT_JOB_FAM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJECT_CXT_JOB_FAM_ID | NUMBER |  | 18 | Yes | Primary Key - Sequence generated key. Fusion Global sequence generator is used to generate the key at run-time. |
| OBJECT_CXT_JOB_FAM_CODE | VARCHAR2 | 36 |  | Yes | Object Context Code is used for data migration purpose. This column will be populated with a GUID value to uniquely identify a row across environments |
| OBJECT_CXT_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_AVAIL_CONTEXT. |
| JOB_FAMILY_ID | NUMBER |  | 18 | Yes | Foreign key to HRQ_JOB_FAMILIES. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AVAIL_CXT_JOB_FAM_N1 | Non Unique | Default | OBJECT_CXT_ID, JOB_FAMILY_ID |
| IRC_AVAIL_CXT_JOB_FAM_PK | Unique | Default | OBJECT_CXT_JOB_FAM_ID |
| IRC_AVAIL_CXT_JOB_FAM_U1 | Unique | Default | OBJECT_CXT_JOB_FAM_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
