# PAY_PROCESS_CHANGES

This table contains a functional audit of the processing of CIR Components.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** SYSTEM

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesschanges-3138.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payprocesschanges-3138.html)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PROCESS_CHANGE_ID | NUMBER |  | 18 | Yes | Primary Key |
| STATUS | VARCHAR2 | 30 |  | Yes | Recorded status |
| CREATOR_ID | NUMBER |  | 18 | Yes | Foreign Key to the Creator Entity |
| CREATOR_TYPE | VARCHAR2 | 30 |  | Yes | Type of object the Creator is. |
| SOURCE_ID | NUMBER |  | 18 | Yes | Foreign Key to the Source Entity |
| SOURCE_DEFINITION_ID | NUMBER |  | 18 | Yes | Foreign Key to the Definition of the Source Entity |
| SOURCE_TYPE | VARCHAR2 | 30 |  | Yes | Type of Object that the source is |
| CHANGE_TIME | TIMESTAMP |  |  | Yes | Time the Change occurred |
| EFFECTIVE_DATE | DATE |  |  |  | Effective Date the Change occurred |
| THIRD_PARTY_ID | NUMBER |  | 18 |  | Key for the 3rd Party Identifier |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign Key to the Enterprise |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_PROCESS_CHANGES_N1 | Non Unique | Default | CREATOR_ID, CREATOR_TYPE |
| PAY_PROCESS_CHANGES_N2 | Non Unique | Default | SOURCE_ID, SOURCE_TYPE |
| PAY_PROCESS_CHANGES_PK | Unique | Default | PROCESS_CHANGE_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
