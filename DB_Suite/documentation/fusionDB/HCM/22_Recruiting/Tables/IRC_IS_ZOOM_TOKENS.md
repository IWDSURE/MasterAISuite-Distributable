# IRC_IS_ZOOM_TOKENS

IRC_IS_ZOOM_TOKENS will contain token details for all the authorized users

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciszoomtokens-17738.html#irciszoomtokens-17738](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irciszoomtokens-17738.html#irciszoomtokens-17738)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_IS_ZOOM_TOKENS_PK | ZOOM_TOKEN_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ZOOM_TOKEN_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| PERSON_ID | NUMBER |  | 18 | Yes | Foreign key to PER_PERSONS table |
| TOKEN | VARCHAR2 | 1024 |  | Yes | Refresh Token Value |
| TOKEN_TYPE | VARCHAR2 | 32 |  | Yes | Token type. String suggesting the type of token.Possible values: 'REFRESH' |
| TOKEN_EXP_DATE | TIMESTAMP |  |  |  | Expiration date of the token. |
| LAST_ACCESS_REFRESH_DATE | TIMESTAMP |  |  |  | Last refresh date of the access token |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_IS_ZOOM_TOKENS_PK | Unique | Default | ZOOM_TOKEN_ID |
| IRC_IS_ZOOM_TOKENS_U1 | Unique | Default | PERSON_ID, TOKEN_TYPE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
