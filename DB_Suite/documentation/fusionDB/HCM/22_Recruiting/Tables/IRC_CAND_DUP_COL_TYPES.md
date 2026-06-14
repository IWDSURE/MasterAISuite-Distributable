# IRC_CAND_DUP_COL_TYPES

The purpose of this new  table is to store info related to notification of collaborators types for new action : Duplicate Candidate Notification

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupcoltypes-8710.html#irccanddupcoltypes-8710](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccanddupcoltypes-8710.html#irccanddupcoltypes-8710)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAND_DUP_COL_TYPES_PK | DUP_CAND_COL_TYPE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DUP_CAND_COL_TYPE_ID | NUMBER |  | 18 | Yes | DUP_CAND_COL_TYPE_ID : Primary key for this table |
| DUP_CAND_NOTIF_CONFIG_ID | NUMBER |  | 18 | Yes | DUP_CAND_NOTIF_CONFIG_ID : Foriegn Key IRC_CAND_DUP_notif_config table. (Life cycle action context) |
| COLAB_TYPE_CODE | VARCHAR2 | 128 |  | Yes | Field that captures collaborator types,  uses lookup type code ORA_IRC_COLLABORATOR_RESP_TYPE |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAND_DUP_COL_TYPES_FK1 | Non Unique | Default | DUP_CAND_NOTIF_CONFIG_ID |
| IRC_CAND_DUP_COL_TYPES_PK | Unique | Default | DUP_CAND_COL_TYPE_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
