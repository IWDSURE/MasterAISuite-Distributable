# IRC_MP_BENEFITS_TL

This table consist of list of benefits which will be associated with the gig.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpbenefitstl-4358.html#ircmpbenefitstl-4358](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpbenefitstl-4358.html#ircmpbenefitstl-4358)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_MP_BENEFITS_TL_PK | BENEFIT_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BENEFIT_ID | NUMBER |  | 18 | Yes | This column is the Primary Key of IRC_MP_BENEFITS_TL table which is unique and not null, Foreign Key to IRC_MP_BENEFITS_B table. |
| BENEFIT_NAME | VARCHAR2 | 240 |  |  | This column indicates the name of the benefit |
| BENEFIT_DESCRIPTION | CLOB |  |  |  | This column is to describe fully about the benefit |
| BENEFIT_SHORT_SUMMARY | VARCHAR2 | 240 |  |  | This coulmn describes the short summary of the benefit |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_MP_BENEFITS_TL_PK | Unique | Default | BENEFIT_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
