# HRC_DL_REM_ENTITIES

SEED Table for Storing individual Business Objects for in HDL Hierarchy

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrementities-19738.html#hrcdlrementities-19738](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlrementities-19738.html#hrcdlrementities-19738)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_ENTITIES_PK | ENTITY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTITY_ID | NUMBER |  |  | Yes | Primary Key for HRC_DL_REM_ENTITIES |
| TOP_ENTITY_ID | NUMBER |  |  | Yes | FK to HRC_DL_REM_TOP_ENTITIES |
| BUSINESS_OBJECT_ID | NUMBER |  |  | Yes | Fk to HRC_DL_BUSINESS_OBJECTS |
| ENTITY_TYPE | VARCHAR2 | 30 |  | Yes | Entity Type UPDATE/DELETE for data disposal |
| ENABLED_FLAG | VARCHAR2 | 1 |  | Yes | A- Always enabled. Can't be disabled by the Customer.
Y - Enabled
N - Disabled |
| LOCAL_VO_ATTRIBUTE | VARCHAR2 | 100 |  |  | Current VO Attribute Matching the Worker's Hierarchy. |
| REFERENCE_HIERARCHY | VARCHAR2 | 200 |  |  | Reference VO Hierarchy. Example : 

Worker:Worker:V2 |
| DATA_QUERY | CLOB |  |  |  | For Transient Objects, Query will have to be provided by Product Teams |
| ENTITY_HASH | VARCHAR2 | 100 |  | Yes | HASH Generated afresh each time the product definition got modified |
| OVERRIDE_QUERY | CLOB |  |  |  | If product team wants to override the default surrogate key fetching using person Id. Product teams can make use of this query to populate the local surrogate keys |
| ENTERPRISE_ID | NUMBER |  |  | Yes | ENTERPRISE_ID |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| REF_BUSINESS_OBJECT_ID | NUMBER |  | 18 |  | Primary Key to HRC_DL_BUSINESS_OBJECTS  - Referring Business Object ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_REM_ENTITIES_N1 | Non Unique | Default | BUSINESS_OBJECT_ID |
| HRC_DL_REM_ENTITIES_N2 | Non Unique | Default | TOP_ENTITY_ID |
| HRC_DL_REM_ENTITIES_U1 | Unique | Default | ENTITY_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
