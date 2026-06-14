# PAY_RETRO_ENTRIES

This table contains entries that have retrospective changes and thus require reprocessing

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payretroentries-11260.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payretroentries-11260.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_RETRO_ENTRIES_PK | RETRO_ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RETRO_ENTRY_ID | NUMBER |  | 18 | Yes | RETRO_ENTRY_ID |
| ELEMENT_ENTRY_ID | NUMBER |  | 18 | Yes | ELEMENT_ENTRY_ID |
| RETRO_RELATIONSHIP_ID | NUMBER |  | 18 | Yes | RETRO_RELATIONSHIP_ID |
| RETRO_COMPONENT_ID | NUMBER |  | 18 | Yes | RETRO_COMPONENT_ID |
| EFFECTIVE_DATE | DATE |  |  | Yes | EFFECTIVE_DATE |
| REPROCESS_DATE | DATE |  |  | Yes | REPROCESS_DATE |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | ELEMENT_TYPE_ID |
| OWNER_TYPE | VARCHAR2 | 30 |  |  | OWNER_TYPE |
| ORIGINAL_OWNER_TYPE | VARCHAR2 | 30 |  |  | ORIGINAL_OWNER_TYPE |
| SYSTEM_REPROCESS_DATE | DATE |  |  |  | SYSTEM_REPROCESS_DATE |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_RETRO_ENTRIES_N1 | Non Unique | Default | RETRO_RELATIONSHIP_ID, ELEMENT_ENTRY_ID |
| PAY_RETRO_ENTRIES_PK | Unique | Default | RETRO_ENTRY_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
