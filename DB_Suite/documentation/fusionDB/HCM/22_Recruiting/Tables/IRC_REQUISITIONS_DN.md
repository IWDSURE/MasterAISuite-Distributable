# IRC_REQUISITIONS_DN

denormalized table for Requisition total applications and prospects count.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionsdn-7956.html#ircrequisitionsdn-7956](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircrequisitionsdn-7956.html#ircrequisitionsdn-7956)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQUISITIONS_DN_PK | REQUISITION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQUISITION_ID | NUMBER |  | 18 | Yes | Primary Key of the table. |
| JA_COUNT | NUMBER |  | 9 | Yes | Stores  the applications count, including the restricted applications. |
| UNRESTRICTED_JA_COUNT | NUMBER |  | 9 | Yes | Stores the unrestricted applications count. |
| PROSPECT_COUNT | NUMBER |  | 9 | Yes | Stores the prospects count |
| NEW_JA_COUNT | NUMBER |  | 9 | Yes | Stores the new applications count. |
| UNRESTRICTED_NEW_JA_COUNT | NUMBER |  | 9 | Yes | Stores the unrestricted new applications count. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQUISITIONS_DN_PK | Unique | Default | REQUISITION_ID |
| IRC_REQUISITION_DN_U1 | Unique | Default | REQUISITION_ID, JA_COUNT |
| IRC_REQUISITION_DN_U2 | Unique | Default | REQUISITION_ID, UNRESTRICTED_JA_COUNT |
| IRC_REQUISITION_DN_U3 | Unique | Default | REQUISITION_ID, PROSPECT_COUNT |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
