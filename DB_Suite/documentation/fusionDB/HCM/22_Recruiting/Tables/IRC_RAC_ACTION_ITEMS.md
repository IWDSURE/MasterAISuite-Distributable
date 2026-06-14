# IRC_RAC_ACTION_ITEMS

This table stores the list of action items which are supposed to be shown to the team member in recruiting activity center.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracactionitems-12320.html#ircracactionitems-12320](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircracactionitems-12320.html#ircracactionitems-12320)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_RAC_ACTION_ITEMS_PK | ACTION_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| ACTION_ITEM_ID | NUMBER |  | 18 | Yes | This column will be used to store the primary key of this table. Auto Generated Key. |  |
| SUBSCRIBER_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_RAC_SUBSCRIBERS table. | Obsolete |
| SUBSCRIBER_ID#01 | NUMBER |  | 18 | Yes | Foreign Key to IRC_RAC_SUBSCRIBERS table. |  |
| SUBSCRIBER_TYPE_CODE | VARCHAR2 | 30 |  | Yes | Stores the information about the subscriber for which this action item is supposed to be displayed. Lookup used for this - ORA_IRC_RAC_SUBSCRIBER | Obsolete |
| SUBSCRIBER_TYPE_CODE#01 | VARCHAR2 | 30 |  | Yes | Stores the information about the subscriber for which this action item is supposed to be displayed. Lookup used for this - ORA_IRC_RAC_SUBSCRIBER |  |
| SUBSCRIBER_RULE_ID | NUMBER |  | 18 | Yes | Foreign Key to IRC_RAC_SUBSCR_RULES_B table. |  |
| OBJECT_ID | NUMBER |  | 18 | Yes | This column stores the object id for a given subsriber. For eg - If Subscriber is SUBMISSIONS , then it will be submissionId . If subscriber is OFFER then it will be offerId etc. |  |
| SUBJECT | VARCHAR2 | 30 |  |  | Subject associated to the OBJECT_ID for which the Action Item applies |  |
| SUBJECT_TYPE | VARCHAR2 | 30 |  |  | Subject type associated to the OBJECT_ID for which the Action Item applies |  |
| ACTION_DATE | TIMESTAMP |  |  |  | This column stores the date when the action was supposed to be taken care of. |  |
| STATUS_CODE | VARCHAR2 | 30 |  | Yes | Status of each action item.Lookup used - ORA_IRC_ACTION_ITEM_STATUS |  |
| ESS_REQUEST_ID | NUMBER |  | 18 |  | If this action item was executed by the ESS Job , the respective request id will be stored here. |  |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |  |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |  |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |  |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |  |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |  |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| IRC_RAC_ACTION_ITEMS_FK1 | Non Unique | Default | SUBSCRIBER_ID#01 |  |
| IRC_RAC_ACTION_ITEMS_FK2 | Non Unique | Default | SUBSCRIBER_RULE_ID | Obsolete |
| IRC_RAC_ACTION_ITEMS_N1 | Non Unique | Default | SUBSCRIBER_RULE_ID, OBJECT_ID |  |
| IRC_RAC_ACTION_ITEMS_PK | Unique | Default | ACTION_ITEM_ID |  |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
