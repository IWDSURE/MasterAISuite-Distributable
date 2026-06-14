# HRC_DL_BUS_FLEX_CONTEXTS

HRC_DL_BUS_FLEX_CONTEXTS is used to store flex field contexts

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusflexcontexts-20612.html#hrcdlbusflexcontexts-20612](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlbusflexcontexts-20612.html#hrcdlbusflexcontexts-20612)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_BUS_FLEX_CONTEXTS_PK | FLEX_CONTEXT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| FLEX_CONTEXT_ID | NUMBER |  | 18 | Yes | FLEX_CONTENT_ID |
| APPLICATION_ID | NUMBER |  | 18 | Yes | APPLICATION_ID |
| FLEX_TYPE | VARCHAR2 | 3 |  | Yes | FLEX_TYPE |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| FLEX_CODE | VARCHAR2 | 100 |  | Yes | FLEX_CODE |
| VO_CATEGORY_CODE | VARCHAR2 | 800 |  |  | VO_CATEGORY_CODE |
| VO_CONTEXT_CODE | VARCHAR2 | 80 |  | Yes | VO_CONTEXT_CODE |
| FLEX_CONTEXT_HASH | VARCHAR2 | 100 |  | Yes | FLEX_CONTEXT_HASH |
| CONTEXT_RESTRICTED | VARCHAR2 | 1 |  |  | CONTEXT_RESTRICTED |
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
| HRC_DL_BUS_FLEX_CONTEXTS_N1 | Non Unique | Default | BUSINESS_OBJECT_ID, FLEX_CODE, VO_CONTEXT_CODE, VO_CATEGORY_CODE, ENTERPRISE_ID |
| HRC_DL_BUS_FLEX_CONTEXTS_PK | Unique | Default | FLEX_CONTEXT_ID |
| HRC_DL_BUS_FLEX_CONTEXTS_U1 | Unique | Default | FLEX_CONTEXT_HASH, ENTERPRISE_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
