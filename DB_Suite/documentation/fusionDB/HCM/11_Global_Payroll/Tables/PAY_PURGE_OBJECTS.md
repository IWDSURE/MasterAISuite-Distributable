# PAY_PURGE_OBJECTS

This table is used to identify the objects that are to be purged from the syste,

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypurgeobjects-20979.html#paypurgeobjects-20979](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypurgeobjects-20979.html#paypurgeobjects-20979)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_PURGE_OBJECTS_PK | PURGE_OBJECT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PURGE_OBJECT_ID | NUMBER |  | 18 | Yes | Primary Key Id |
| PURGE_SET_ID | NUMBER |  | 18 | Yes | This identifies all the Objects belonging to a purge set. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Object Type to be purged |
| OBJECT_ID | NUMBER |  | 18 | Yes | The Object Id to be purged |
| SUB_OBJECT_TYPE | VARCHAR2 | 30 |  |  | This further qualifys the Object Type, for example if the Qualifier is for Processing Actions then this will identify the Action Type. |
| DEFINITION_ID | NUMBER |  | 18 |  | This is used to identify a Definition that can be used to qualify the purge. For example, if we are purging HCM Extracts this could be the extract ID |
| QUALIFIER1 | VARCHAR2 | 30 |  |  | Additional Qualifier 1 |
| QUALIFIER2 | VARCHAR2 | 30 |  |  | Additional Qualifier 2 |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PAY_PURGE_OBJECTS_N1 | Non Unique | Default | OBJECT_TYPE, OBJECT_ID |
| PAY_PURGE_OBJECTS_N2 | Non Unique | Default | OBJECT_TYPE, SUB_OBJECT_TYPE, DEFINITION_ID, QUALIFIER1, QUALIFIER2 |
| PAY_PURGE_OBJECTS_U1 | Unique | Default | PURGE_OBJECT_ID |

---

[← Back to Index](../11_Global_Payroll_Tables_Index.md)
