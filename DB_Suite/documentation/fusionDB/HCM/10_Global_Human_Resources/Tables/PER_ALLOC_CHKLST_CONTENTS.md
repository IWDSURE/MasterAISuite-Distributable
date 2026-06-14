# PER_ALLOC_CHKLST_CONTENTS

PER_ALLOC_CHKLST_CONTENTS : This table has contents of allocated checklist.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocchklstcontents-21401.html#perallocchklstcontents-21401](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perallocchklstcontents-21401.html#perallocchklstcontents-21401)

## Primary Key

| Name | Columns |
|------|----------|
| PER_ALLOC_CHKLST_CONTENTS_PK | ALLOC_CHKLST_CONTENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ALLOC_CHKLST_CONTENT_ID | NUMBER |  | 18 | Yes | ALLOC_CHKLST_CONTENT_ID |
| ALLOCATED_CHECKLIST_ID | NUMBER |  | 18 | Yes | ALLOCATED_CHECKLIST_ID |
| CHECKLIST_CONTENT_ID | NUMBER |  | 18 |  | CHECKLIST_CONTENT_ID |
| CONTENT_TYPE | VARCHAR2 | 30 |  | Yes | CONTENT_TYPE |
| SEQUENCE | NUMBER |  | 9 |  | SEQUENCE |
| CHK_CONTENT_DEFN_ID | NUMBER |  | 18 | Yes | CHK_CONTENT_DEFN_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_ALLOC_CHKLST_CONTENTS_N1 | Non Unique | FUSION_TS_TX_DATA | ALLOCATED_CHECKLIST_ID |
| PER_ALLOC_CHKLST_CONTENTS_PK | Unique | FUSION_TS_TX_DATA | ALLOC_CHKLST_CONTENT_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
