# HWR_DI_SOURCE_XREF

This table stores HWR source reference.

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdisourcexref-18511.html#hwrdisourcexref-18511](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdisourcexref-18511.html#hwrdisourcexref-18511)

## Primary Key

| Name | Columns |
|------|----------|
| HWR_DI_SOURCE_XREF_PK | SOURCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SOURCE_ID | NUMBER |  | 18 | Yes | This is the HWR DI source id. |
| EXTERNAL_SOURCE_ID | NUMBER |  | 18 |  | This is the external HWR source id. |
| SETUP_STATUS | VARCHAR2 | 500 |  |  | This is the set up status. |
| ENABLE_STATUS | VARCHAR2 | 500 |  |  | This is the enable status. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HWR_DI_SOURCE_XREF_U1 | Unique | Default | SOURCE_ID |

---

[← Back to Index](../34_Workforce_Reputation_Management_Tables_Index.md)
