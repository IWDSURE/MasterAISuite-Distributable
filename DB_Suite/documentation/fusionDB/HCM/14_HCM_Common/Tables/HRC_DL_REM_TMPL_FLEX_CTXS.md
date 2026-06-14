# HRC_DL_REM_TMPL_FLEX_CTXS

Table for Storing Flex Context Preferences  in a given Data Disposal Template

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplflexctxs-3995.html#hrcdlremtmplflexctxs-3995](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplflexctxs-3995.html#hrcdlremtmplflexctxs-3995)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_dl_rem_tmpl_flex_ctxs_PK | TMPL_FLEX_CTX_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_FLEX_CTX_ID | NUMBER |  |  | Yes | Primary Key for the table |
| TMPL_ENTITY_ID | NUMBER |  |  | Yes | FK reference to HRC_DL_REM_TMPL_ENTITIES |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | FK to BUSINESS_OBJECT_ID |
| FLEX_TYPE | VARCHAR2 | 3 |  |  | Flex type - DFF/EFF |
| FLEX_CODE | VARCHAR2 | 100 |  | Yes | Flex Field Code |
| VO_CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | Context for the Respective Flex Field Business Object |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_TMPL_FLEX_CTXS_U1 | Unique | Default | TMPL_FLEX_CTX_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
