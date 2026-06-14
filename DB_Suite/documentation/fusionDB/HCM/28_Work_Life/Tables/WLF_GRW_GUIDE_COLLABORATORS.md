# WLF_GRW_GUIDE_COLLABORATORS

Table to store list of collaborators added to a grow guide.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguidecollaborators-11753.html#wlfgrwguidecollaborators-11753](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwguidecollaborators-11753.html#wlfgrwguidecollaborators-11753)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_GRW_GUIDE_COLLABORATOR_PK | GUIDE_COLLABORATOR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| GUIDE_COLLABORATOR_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| GUIDE_ID | NUMBER |  | 18 | Yes | ID of guide the collobrator is associated to. |
| STATUS | VARCHAR2 | 30 |  | Yes | Status of the guide collaborator (e.g Active, InActive etc.). |
| COLLABORATOR_TYPE | VARCHAR2 | 30 |  |  | Type of the Collaborator (Person, List etc.) |
| COLLABORATOR_ID | VARCHAR2 | 64 |  | Yes | Id of the associated colloborator. |
| ADDED_ON_DATE | TIMESTAMP |  |  | Yes | Date when the collaborator was added to guide. |
| REMOVED_ON_DATE | TIMESTAMP |  |  |  | Date when the collaborator was removed from guide. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_GRW_GUIDE_COLLABORATORS_N1 | Non Unique | Default | GUIDE_ID |
| WLF_GRW_GUIDE_COLLABORATORS_N2 | Non Unique | Default | STATUS |
| WLF_GRW_GUIDE_COLLABORATORS_N3 | Non Unique | Default | COLLABORATOR_ID |
| WLF_GRW_GUIDE_COLLABORATORS_U1 | Unique | Default | GUIDE_COLLABORATOR_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
