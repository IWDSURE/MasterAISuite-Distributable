# BEN_CSR_ACTIVITIES

BEN_CSR_ACTIVITIES holds the list of forms and online processes, that are to be navigable from the Oracle Advanced Benefits, Benefits Service Center form. For example, process life events.

## Details

**Schema:** FUSION

**Object owner:** BEN

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencsractivities-17684.html#bencsractivities-17684](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/bencsractivities-17684.html#bencsractivities-17684)

## Primary Key

| Name | Columns |
|------|----------|
| BEN_CSR_ACTIVITIES_PK | CSR_ACTIVITIES_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CSR_ACTIVITIES_ID | NUMBER |  | 18 | Yes | Foreign key to BEN_CSR_ACTIVITIES_F. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign Key to HR_ORGANIZATION_UNITS |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Reference to the unique identifier for the legal entity. |
| ORDR_NUM | NUMBER |  | 18 |  | Order number. |
| FUNCTION_NAME | VARCHAR2 | 90 |  | Yes | Function name. |
| USER_FUNCTION_NAME | VARCHAR2 | 240 |  | Yes | User function name. |
| FUNCTION_TYPE | VARCHAR2 | 90 |  |  | Function type. |
| START_DATE | DATE |  |  |  | Start date. |
| END_DATE | DATE |  |  |  | End date. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| BEN_CSR_ACTIVITIES_FK2 | Non Unique | Default | LEGAL_ENTITY_ID |
| BEN_CSR_ACTIVITIES_PK1 | Unique | Default | CSR_ACTIVITIES_ID |

---

[← Back to Index](../4_Benefits_Tables_Index.md)
