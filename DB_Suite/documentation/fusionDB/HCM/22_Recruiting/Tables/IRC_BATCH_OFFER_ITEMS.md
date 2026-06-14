# IRC_BATCH_OFFER_ITEMS

Stores all the batch offer item related details.

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbatchofferitems-13781.html#ircbatchofferitems-13781](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircbatchofferitems-13781.html#ircbatchofferitems-13781)

## Primary Key

| Name | Columns |
|------|----------|
| IRC_BATCH_OFFER_ITEMS_PK | BATCH_OFFER_ITEM_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| BATCH_OFFER_ITEM_ID | NUMBER |  | 18 | Yes | Primary key for this table. System generated. |
| BATCH_OFFER_ID | NUMBER |  | 18 | Yes | Foreign key to IRC_BATCH_OFFERS table. Refers to the batch offer. |
| OFFER_ID | NUMBER |  | 18 |  | Foreign key to IRC_OFFERS table. Refers to the  offer. |
| STATUS_CODE | VARCHAR2 | 30 |  |  | Lookup ORA_IRC_OFFER_BATCH_ITEM_STATUS. |
| OFFER_STATUS_CODE | VARCHAR2 | 30 |  |  | Status of Offer data copy from Source offer. |
| ASSIGNMENT_STATUS_CODE | VARCHAR2 | 30 |  |  | Assignment status. Lookup ORA_IRC_OFFER_BATCH_ITEM_COPY_STATUS. |
| PAYROLL_STATUS_CODE | VARCHAR2 | 30 |  |  | Payroll status. Lookup ORA_IRC_OFFER_BATCH_ITEM_COPY_STATUS. |
| SALARY_STATUS_CODE | VARCHAR2 | 30 |  |  | Salary status. Lookup ORA_IRC_OFFER_BATCH_ITEM_COPY_STATUS. |
| CMP_STATUS_CODE | VARCHAR2 | 30 |  |  | Compensation status. Lookup ORA_IRC_OFFER_BATCH_ITEM_COPY_STATUS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| IRC_BATCH_OFFER_ITEMS_FK1 | Non Unique | Default | BATCH_OFFER_ID |
| IRC_BATCH_OFFER_ITEMS_FK2 | Non Unique | Default | OFFER_ID |
| IRC_BATCH_OFFER_ITEMS_PK | Unique | Default | BATCH_OFFER_ITEM_ID |

---

[← Back to Index](../22_Recruiting_Tables_Index.md)
