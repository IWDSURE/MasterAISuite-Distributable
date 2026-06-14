# IRC_CAMP_ASSETS_TL

Stores the translatable data for an asset of a campaign.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetstl-16917.html#irccampassetstl-16917](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampassetstl-16917.html#irccampassetstl-16917)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_ASSETS_TL_PK | ASSET_ID, LANGUAGE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ASSET_ID | NUMBER |  | 18 | Yes | Part of the Primary Key for this table. Foreign key to IRC_CAMPAIGN_ASSETS_B table. |
| LANGUAGE | VARCHAR2 | 4 |  | Yes | Indicates the code of the language into which the contents of the translatable columns are translated. |
| SOURCE_LANG | VARCHAR2 | 4 |  | Yes | Indicates the code of the language in which the contents of the translatable columns were originally created. |
| ASSET_NAME | VARCHAR2 | 240 |  | Yes | Stores the name of the asset for this campaign. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_ASSETS_TL_PK | Unique | Default | ASSET_ID, LANGUAGE |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
