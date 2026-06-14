# IRC_CAMP_DEEP_LINKS_B

Stores the information of employee campagins deeplinks

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampdeeplinksb-17173.html#irccampdeeplinksb-17173](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampdeeplinksb-17173.html#irccampdeeplinksb-17173)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_CAMP_DEEP_LINKS_B_PK | DEEP_LINK_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEEP_LINK_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| OBJECT_TYPE | VARCHAR2 | 30 |  | Yes | Stores the deep link object type. Foreign Key to FND_DEEP_LINK_LIST table. |
| ACTION | VARCHAR2 | 100 |  | Yes | Stores the deep link action. Foreign Key to FND_DEEP_LINK_LIST table. |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Stores the campaign deep link status code. Corresponding lookup type is ORA_IRC_CAMP_DEEP_LINK_STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_CAMP_DEEP_LINKS_B_FK1 | Non Unique | Default | OBJECT_TYPE, ACTION |
| IRC_CAMP_DEEP_LINKS_B_PK | Unique | Default | DEEP_LINK_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
