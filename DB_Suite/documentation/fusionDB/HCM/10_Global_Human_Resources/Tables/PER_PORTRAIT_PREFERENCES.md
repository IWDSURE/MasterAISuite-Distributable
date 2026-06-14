# PER_PORTRAIT_PREFERENCES

This table sores the Portrait Content preferences for person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitpreferences-5054.html#perportraitpreferences-5054](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitpreferences-5054.html#perportraitpreferences-5054)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PORTRAIT_PREFERENCES_PK | PORTRAIT_PREFERENCE_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PORTRAIT_PREFERENCE_ID | NUMBER |  | 18 | Yes | System generated primary key. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| ABOUT_PERSON_ID | NUMBER |  | 18 | Yes | Person identifier number of the Portrait Preferences |
| PORTRAIT_CONTENT_ITEM_KEY | VARCHAR2 | 50 |  | Yes | Portrait content item key reference to the Portrait cards and content. |
| MANAGER_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates if the portrait content is visible to the manager |
| CONNECTIONS_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates if the portrait content is visible to the connections. |
| EVERYONE_VISIBLE | VARCHAR2 | 1 |  | Yes | Indicates if the portrait content is visible to everyone. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_PORTRAIT_PREFERENCES_PK | Unique | Default | PORTRAIT_PREFERENCE_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
