# CMP_MKT_VND_JOB_FAMILY_B

Table to store Vendor Job Family data

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndjobfamilyb-10511.html#cmpmktvndjobfamilyb-10511](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktvndjobfamilyb-10511.html#cmpmktvndjobfamilyb-10511)

## Primary Key

| Name | Columns |
|------|----------|
| CMP_MKT_VND_JOB_FAMILY_PK | JOB_FAMILY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| JOB_FAMILY_ID | NUMBER |  | 18 | Yes | Primary Key |
| JOB_FAMILY_SEQ_NUM | NUMBER |  |  |  | Sequence Number |
| JOB_FAMILY_CODE | VARCHAR2 | 30 |  | Yes | Job Family Code |
| VENDOR_ID | NUMBER |  | 18 | Yes | Foreign Key |
| STATUS | VARCHAR2 | 30 |  | Yes | Status |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Business Group Id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CMP_MKT_VND_JOB_FAMILY_B_U1 | Unique | Default | JOB_FAMILY_CODE, VENDOR_ID |
| CMP_MKT_VND_JOB_FAMILY_U1 | Unique | Default | JOB_FAMILY_ID |

---

[← Back to Index](../7_Compensation_Tables_Index.md)
