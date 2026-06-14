# IRC_AIEVENTS_TRACKING

This table stores non-transactional data normally related to adaptive intelligence events.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaieventstracking-27939.html#ircaieventstracking-27939](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircaieventstracking-27939.html#ircaieventstracking-27939)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_AIEVENTS_TRACKING_PK | ENTRY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ENTRY_ID | NUMBER |  | 18 | Yes | Primary key of the table. System generated. |
| REFERENCE_ID | NUMBER |  | 18 | Yes | Reference to the entity associated with the entry. |
| REFERENCE_AUX | VARCHAR2 | 256 |  |  | Auxiliary reference to the entity associated with the entry. |
| CONTEXT | VARCHAR2 | 50 |  | Yes | Context where the content was generated. |
| CONTENT_TYPE | NUMBER |  | 2 | Yes | JSON content is stored in CONTENT_JSON while non-JSON in CONTENT. |
| CONTENT | CLOB |  |  |  | Non-JSON content. The type of the content is defined by CONTENT_TYPE. |
| CONTENT_JSON | CLOB |  |  |  | The column configuration optimzes access to JSON content. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_AIEVENTS_TRACKING_N1 | Non Unique | Default | CONTEXT, REFERENCE_ID, REFERENCE_AUX |
| IRC_AIEVENTS_TRACKING_N2 | Non Unique | Default | CREATION_DATE |
| IRC_AIEVENTS_TRACKING_PK | Unique | Default | ENTRY_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
