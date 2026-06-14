# HRC_DL_REM_TMPL_TOP_ENTITIES

All Mandatory Entities will be automatically added here during UI Save and Commit.

For Entites disabled by the customer, data will not exist here. 

For Entities enabled by the customer, entries will be created.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmpltopentities-27875.html#hrcdlremtmpltopentities-27875](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmpltopentities-27875.html#hrcdlremtmpltopentities-27875)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_TMPL_TOP_ENTITI_PK | TMPL_TOP_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_TOP_ENTITY_ID | NUMBER |  |  | Yes | PK column for HRC_DL_REM_TMPL_TOP_ENTITIES |
| TOP_ENTITY_ID | NUMBER |  |  | Yes | FK to HRC_DL_REM_TOP_ENTITIES |
| TEMPLATE_ID | NUMBER |  |  | Yes | TEMPLATE_ID |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | For Enabled Entities. |
| TOP_BUSINESS_OBJECT_ID | NUMBER |  |  |  | Top Business Object Id |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_TMPL_TOP_ENT_N1 | Non Unique | Default | TEMPLATE_ID |
| HRC_DL_REM_TMPL_TOP_ENT_N2 | Non Unique | Default | TOP_BUSINESS_OBJECT_ID |
| HRC_DL_REM_TMPL_TOP_ENT_U1 | Unique | Default | TMPL_TOP_ENTITY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
