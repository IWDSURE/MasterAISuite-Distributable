# IRC_LABELS_B

Table contains labels configured by recruiters/admins and to be used for entity tagging.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclabelsb-7165.html#irclabelsb-7165](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irclabelsb-7165.html#irclabelsb-7165)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_LABELS_B_PK | LABEL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LABEL_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| ENTITY_TYPE | VARCHAR2 | 100 |  | Yes | Entity for which this label will be applicable. |
| LABEL_CODE | VARCHAR2 | 256 |  | Yes | Code of the label being created. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_LABELS_B_PK | Unique | Default | LABEL_ID |
| IRC_LABELS_B_U1 | Unique | Default | ENTITY_TYPE, LABEL_CODE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
