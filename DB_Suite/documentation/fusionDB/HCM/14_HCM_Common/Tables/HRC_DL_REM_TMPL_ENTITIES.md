# HRC_DL_REM_TMPL_ENTITIES

All Mandatory Entities will be automatically added here during UI Save and Commit.

For Entites disabled by the customer, data will not exist here. 

For Entities enabled by the customer, entries will be created.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplentities-24123.html#hrcdlremtmplentities-24123](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremtmplentities-24123.html#hrcdlremtmplentities-24123)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_TMPL_ENT_PK | TMPL_ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TMPL_ENTITY_ID | NUMBER |  |  | Yes | Primary Key |
| TMPL_TOP_ENTITY_ID | NUMBER |  |  | Yes | FK to HRC_DL_REM_TMPL_TOP_ENTITIES |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | BUSINESS_OBJECT_ID |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | ENTITY_TYPE |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | Y/A/N

A- Always Enabled |
| LOCAL_VO_ATTRIBUTE | VARCHAR2 | 100 |  |  | LOCAL_VO_ATTRIBUTE |
| REFERENCE_HIERARCHY | VARCHAR2 | 200 |  |  | REFERENCE_HIERARCHY |
| DATA_QUERY | CLOB |  |  |  | DATA_QUERY |
| OVERRIDE_QUERY | CLOB |  |  |  | In general, the surrogate keys for the current entity will be fetched based on the person list. If product teams wants to override default implementation, they can make use of this query to provide surrogate Keys |
| ENTITY_ID | NUMBER |  |  |  | FK to HRC_DL_REM_ENTITTIES |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| FLEX_ENABLED | VARCHAR2 | 1 |  |  | If Flex enabled for this business object, value will be Y, else N |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_TMPL_ENT_N1 | Non Unique | Default | TMPL_TOP_ENTITY_ID |
| HRC_DL_REM_TMPL_ENT_N2 | Non Unique | Default | BUSINESS_OBJECT_ID |
| HRC_DL_REM_TMPL_ENT_N3 | Non Unique | Default | ENTITY_TYPE |
| HRC_DL_REM_TMPL_ENT_U1 | Unique | Default | TMPL_ENTITY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
