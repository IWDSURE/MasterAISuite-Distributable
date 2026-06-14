# IRC_CAMP_POST_CONTENT_TL

Stores translatable data for the content of a post created in post campaigns.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostcontenttl-31277.html#irccamppostcontenttl-31277](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccamppostcontenttl-31277.html#irccamppostcontenttl-31277)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_POST_CONTENT_TL_PK | POST_CONTENT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| POST_CONTENT_ID | NUMBER |  | 18 | Yes | Part of the primary key for this table. Foreign key to irc_camp_post_content_b table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| TITLE | VARCHAR2 | 256 |  | Yes | Stores the title of the post. |
| DESCRIPTION | VARCHAR2 | 1024 |  | Yes | Stores the description of the post. |
| PRIMARY_LABEL | VARCHAR2 | 64 |  |  | Stores the label for primary post button. |
| SECONDARY_LABEL | VARCHAR2 | 64 |  |  | Stores the label for secondary post button. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_POST_CONTENT_TL_PK | Unique | Default | POST_CONTENT_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
