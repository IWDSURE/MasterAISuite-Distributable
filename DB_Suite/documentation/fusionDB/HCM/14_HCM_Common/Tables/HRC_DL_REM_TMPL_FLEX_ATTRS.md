# HRC_DL_REM_TMPL_FLEX_ATTRS

Table used to store the flex attribute preferences provided by the customer in the Data Disposal Template UI

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplflexattrs-24676.html#hrcdlremtmplflexattrs-24676](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplflexattrs-24676.html#hrcdlremtmplflexattrs-24676)

## Primary Key

| Name | Columns |
|------|----------|
| hrc_dl_rem_tmpl_flex_attr_PK | TMPL_FLEX_ATTR_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_FLEX_ATTR_ID | NUMBER |  |  | Yes | Primary Key |
| TMPL_FLEX_CTX_ID | NUMBER |  |  | Yes | Parent Reference to HRC_DL_REM_FLEX_CTXS |
| FLEX_SEGMENT_NAME | VARCHAR2 | 100 |  | Yes | Segment Name |
| FLEX_SEGMENT_CODE | VARCHAR2 | 100 |  | Yes | Segment Code |
| SEGMENT_VALUE | VARCHAR2 | 4000 |  |  | Actual Value provided by the customer in the UI |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  |  |  | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_TMPL_FLEX_ATTRS_U1 | Unique | Default | TMPL_FLEX_ATTR_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
