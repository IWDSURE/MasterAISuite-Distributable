# IRC_WABA_TEMPLATE_TOKEN_MAP

Table storing the mapping between WhatsApp and Recruiting Messaging Template Tokens

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwabatemplatetokenmap-15608.html#ircwabatemplatetokenmap-15608](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircwabatemplatetokenmap-15608.html#ircwabatemplatetokenmap-15608)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_WABA_TEMPLATE_TOKEN_MAP_PK | TOKEN_MAPPING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| TOKEN_MAPPING_ID | NUMBER |  | 18 | Yes | Primary key for the token mapping record |
| WABA_TEMPLATE_ID | VARCHAR2 | 50 |  |  | WhatsApp template ID used in Recruiting |
| NAMED_PLACEHOLDER_TOKEN | VARCHAR2 | 100 |  | Yes | Token name for the content category in Recruiting |
| NUMBERED_PLACEHOLDER_TOKEN | NUMBER |  | 2 | Yes | Placeholder token to be used in WhatsApp Template |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_WABA_TEMPLATE_TOKEN_MAP_N1 | Non Unique | Default | WABA_TEMPLATE_ID |
| IRC_WABA_TEMPLATE_TOKEN_MAP_PK | Unique | Default | TOKEN_MAPPING_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
