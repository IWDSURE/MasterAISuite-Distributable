# HWR_DI_REST_ELEMENT

This table stores the rest element information.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdirestelement-27814.html#hwrdirestelement-27814](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdirestelement-27814.html#hwrdirestelement-27814)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_REST_ELEMENT_PK | SOURCE_ID, ELEMENT_TYPE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the source id. |
| ELEMENT_TYPE | VARCHAR2 | 512 |  | Yes | This is the rest element type. |
| ELEMENT_VALUE | VARCHAR2 | 512 |  | Yes | This is the rest element value. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_REST_ELEMENT_U1 | Unique | Default | SOURCE_ID, ELEMENT_TYPE |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
