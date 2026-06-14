# WLF_HCM_LIST_ITEMS

This table stores the extracted list of items that are part of a HCM List.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfhcmlistitems-8569.html#wlfhcmlistitems-8569](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfhcmlistitems-8569.html#wlfhcmlistitems-8569)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_HCM_LIST_ITEMS_PK | HCM_LIST_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| HCM_LIST_ITEM_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| HCM_LIST_ID | NUMBER |  | 18 | Yes | Identifier for the HCM List which represents a list of items. |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | Specifies the source of HCM_LIST_ID such as HCM_LIST or SKILL_CONTENT_ITEM_VALUESET. |
| ITEM_ID | NUMBER |  | 18 | Yes | Identifier for the individual item within the given HCM List. |
| ITEM_TYPE | VARCHAR2 | 50 |  |  | Specifies the type of the individual item within the given HCM List. |
| JOB_ID | NUMBER |  | 18 |  | Identifier for the ESS job used to extract items from the given HCM List. |
| IS_PROCESSED | VARCHAR2 | 1 |  |  | Specifies if the item in the given HCM List is processed or not. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_HCM_LIST_ITEMS_N1 | Non Unique | Default | JOB_ID |
| WLF_HCM_LIST_ITEMS_N2 | Non Unique | Default | HCM_LIST_ID, ITEM_TYPE |
| WLF_HCM_LIST_ITEMS_N3 | Non Unique | Default | ITEM_ID |
| WLF_HCM_LIST_ITEMS_U1 | Unique | Default | HCM_LIST_ITEM_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
