# WLF_LMC_CONTENT_OBJ_XREFS

Many to Many relationship between content objects and objectives

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmccontentobjxrefs-23390.html#wlflmccontentobjxrefs-23390](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflmccontentobjxrefs-23390.html#wlflmccontentobjxrefs-23390)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LMC_CONTENT_OBJ_XREFS_PK | CONTENT_XREF_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CONTENT_XREF_ID | NUMBER |  | 18 | Yes | CONTENT_XREF_ID |
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| OBJECTIVE_ID | NUMBER |  | 18 | Yes | Foreign key to the wlf_lmc_objectives table |
| OBJECTIVE_SEQUENCE | NUMBER |  |  | Yes | OBJECTIVE_SEQUENCE |
| IS_PRIMARY | VARCHAR2 | 1 |  | Yes | IS_PRIMARY |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LMC_CONTENT_OBJ_XREFS_N1 | Non Unique | Default | CONTENT_ID, OBJECTIVE_ID |
| WLF_LMC_CONTENT_OBJ_XREFS_PK | Unique | Default | CONTENT_XREF_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
