# HRC_DL_OBJ_HIER_COMPONENTS

Table to store the object components in the hierarchy for required objects as defined from product annotation

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlobjhiercomponents-10206.html#hrcdlobjhiercomponents-10206](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlobjhiercomponents-10206.html#hrcdlobjhiercomponents-10206)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_OBJ_HIER_COMPS_PK | OBJ_HIER_COMPONENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| OBJ_HIER_COMPONENT_ID | NUMBER |  | 18 | Yes | OBJ_HIER_COMPONENT_ID |
| OBJECT_HIERARCHY_ID | NUMBER |  | 18 | Yes | OBJECT_HIERARCHY_ID |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | BUSINESS_OBJECT_ID |
| REQUIRED_FLAG | VARCHAR2 | 30 |  | Yes | REQUIRED_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_DL_OBJ_HIER_COMPS_N1 | Non Unique | Default | BUSINESS_OBJECT_ID |
| HRC_DL_OBJ_HIER_COMPS_U1 | Unique | Default | OBJ_HIER_COMPONENT_ID |
| HRC_DL_OBJ_HIER_COMPS_U2 | Unique | Default | OBJECT_HIERARCHY_ID, BUSINESS_OBJECT_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
