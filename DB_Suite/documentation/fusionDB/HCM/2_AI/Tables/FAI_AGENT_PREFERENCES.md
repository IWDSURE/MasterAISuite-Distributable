# FAI_AGENT_PREFERENCES

This table will store agent user preferences.

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiagentpreferences-19107.html#faiagentpreferences-19107](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiagentpreferences-19107.html#faiagentpreferences-19107)

## Primary Key

| Name | Columns |
|------|----------|
| FAI_AGENT_PREFERENCES_PK | AGENT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AGENT_PREFERENCE_ID | NUMBER |  | 18 | Yes | The system generated primary key. |
| USER_ID | VARCHAR2 | 200 |  | Yes | User identification of the agent preference. |
| PREFERENCE_NAME | VARCHAR2 | 200 |  |  | The name of the Agent Preference. |
| PREFERENCE_JSON_VALUE | CLOB |  |  |  | The preference value represented as JSON. |
| UPDATED_DATE | TIMESTAMP |  |  |  | The date and time of the last update. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| FAI_AGENT_PREFERENCES_PK | Unique | Default | AGENT_PREFERENCE_ID |
| FAI_AGENT_PREFERENCES_U1 | Unique | Default | USER_ID, PREFERENCE_NAME |

---

[← Back to Index](../2_AI_Tables_Index.md)
