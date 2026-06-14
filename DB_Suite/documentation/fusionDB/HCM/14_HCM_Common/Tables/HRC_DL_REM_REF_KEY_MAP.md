# HRC_DL_REM_REF_KEY_MAP

Whenever parent information is being removed from the product table, to ensure data disposal for respective child tables, parent information will be stored in this table.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremrefkeymap-24266.html#hrcdlremrefkeymap-24266](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdlremrefkeymap-24266.html#hrcdlremrefkeymap-24266)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DL_REM_REF_KEY_MAP_PK | REF_KEY_MAP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| REF_KEY_MAP_ID | NUMBER |  | 18 | Yes | Primary key |
| PERSON_ID | NUMBER |  | 18 | Yes | FK referring to current Person Data |
| BUSINESS_OBJECT_ID | NUMBER |  | 18 | Yes | HDL Business Object ID reference |
| REFERENCE_ID | NUMBER |  | 18 | Yes | FK Surrogate Id Reference to referenced object. |
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
| HRC_DL_REM_REF_KEY_MAP_N1 | Non Unique | Default | BUSINESS_OBJECT_ID, PERSON_ID |
| HRC_DL_REM_REF_KEY_MAP_U1 | Unique | Default | REF_KEY_MAP_ID |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
