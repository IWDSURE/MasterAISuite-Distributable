# PER_PORTRAIT_CARD_CONFIG

This table is new for Fusion, and has been created to handle user card order in portrait.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcardconfig-26958.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perportraitcardconfig-26958.html)

## Primary Key

| Name | Columns |
|------|----------|
| PER_PORTRAIT_CARD_CONFIG_PK | USER_ID, CARD_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CARD_ID | VARCHAR2 | 25 |  | Yes | This column is used to save the card number |
| USER_ID | NUMBER |  | 18 | Yes | This column is used to save the USER_ID |
| CARD_SEQUENCE | NUMBER |  | 2 |  | This column is used to save the CARD_SEQUENCE |
| SHOW_CARD | VARCHAR2 | 1 |  |  | This column is used to save the card status |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PER_PORTRAIT_CARD_CONFIG_PK | Unique | Default | USER_ID, CARD_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
