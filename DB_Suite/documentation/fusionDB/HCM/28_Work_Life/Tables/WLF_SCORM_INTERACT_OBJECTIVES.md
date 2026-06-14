# WLF_SCORM_INTERACT_OBJECTIVES

Objectives stored for an Interaction

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscorminteractobjectives-16252.html#wlfscorminteractobjectives-16252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscorminteractobjectives-16252.html#wlfscorminteractobjectives-16252)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_INTERACT_OBJS_PK | INTERACTION_OBJECTIVE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| INTERACTION_OBJECTIVE_ID | NUMBER |  | 18 | Yes | INTERACTION_OBJECTIVE_ID |
| SCORM_INTERACTION_ID | NUMBER |  | 18 | Yes | Foreign key into the WLF_SCORM_INTERACTIONS table |
| OBJECTIVE_SEQUENCE | NUMBER |  |  | Yes | INTERACTION_SEQUENCE |
| EXTERNAL_IDENTIFIER | VARCHAR2 | 4000 |  | Yes | EXTERNAL_IDENTIFIER |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_INTERACT_OBJS_N1 | Non Unique | Default | SCORM_INTERACTION_ID, OBJECTIVE_SEQUENCE |
| WLF_SCORM_INTERACT_OBJS_PK | Unique | FUSION_TS_TX_DATA | INTERACTION_OBJECTIVE_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
