# IRC_REQ_INFO_RESERVED

Table containing the reserved values for Requisition

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqinforeserved-7153.html#ircreqinforeserved-7153](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircreqinforeserved-7153.html#ircreqinforeserved-7153)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_REQ_INFO_RESERVED_PK | REQ_INFO_RESERVED_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REQ_INFO_RESERVED_ID | NUMBER |  | 18 | Yes | Primary Key of the table. System generated. |
| REQUISITION_ID | NUMBER |  | 18 |  | Holds the REQUISITION_ID that reserved the informations. |
| REQUISITION_NUMBER | VARCHAR2 | 240 |  | Yes | Reserved unique readable number for the Requistion |
| REQ_SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Stores the source type of the Requisition. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_REQ_INFO_RESERVED_N1 | Non Unique | Default | REQUISITION_ID |
| IRC_REQ_INFO_RESERVED_PK | Unique | Default | REQ_INFO_RESERVED_ID |
| IRC_REQ_INFO_RESERVED_U1 | Unique | Default | REQUISITION_NUMBER |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
