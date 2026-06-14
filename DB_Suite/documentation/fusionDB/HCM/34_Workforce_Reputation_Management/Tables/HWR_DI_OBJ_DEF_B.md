# HWR_DI_OBJ_DEF_B

The File Format table stores information about the format of flat files.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjdefb-5211.html#hwrdiobjdefb-5211](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiobjdefb-5211.html#hwrdiobjdefb-5211)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_OBJ_DEF_B_PK | ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ID | NUMBER |  | 18 | Yes | This is the primary key for this table. This Stores the sequence value for the object definition. |
| SOURCE_ID | NUMBER |  | 18 | Yes | The social media source ID. |
| NAME | VARCHAR2 | 256 |  |  | This is the name of the Object definition. |
| UUID | VARCHAR2 | 64 |  |  | This is the unique Identifier of the Object Definition created during object creation. |
| PHYSICAL_DEF | CLOB |  |  |  | This stores the Physical Definition of the Object definition. |
| LOGICAL_DEF | CLOB |  |  |  | This stores the Logical Definition of the Object definition. |
| OBJ_DEF_TYPE | VARCHAR2 | 64 |  | Yes | This stores the type of Object definition. |
| MAP_TYPE | VARCHAR2 | 256 |  |  | The mapping type of the OD, source or target. |
| DEF_NAME | VARCHAR2 | 256 |  |  | The definition name from open api file. |
| REF_DEF_NAME | VARCHAR2 | 256 |  |  | The referenced definition name from open api file. |
| PRODUCT | VARCHAR2 | 256 |  |  | This is the product that the Object definitionis associated with. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_OBJ_DEF_B_U1 | Unique | Default | ID |
| HWR_DI_OBJ_DEF_B_U3 | Unique | Default | UUID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
