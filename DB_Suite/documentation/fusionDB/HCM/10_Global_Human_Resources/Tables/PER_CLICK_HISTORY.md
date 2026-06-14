# PER_CLICK_HISTORY

This table stores the click history of a person.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perclickhistory-26778.html#perclickhistory-26778](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perclickhistory-26778.html#perclickhistory-26778)

## Primary Key

| Name | Columns |
|------|----------|
| PER_CLICK_HISTORY_PK | PERSON_CLICK_HISTORY_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PERSON_CLICK_HISTORY_ID | NUMBER |  | 18 | Yes | PERSON CLICK HISTORY IDENTIFIER |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Identifier |
| USER_GUID | VARCHAR2 | 64 |  |  | User GUID of the person. |
| RELATED_PERSON_ID | NUMBER |  | 18 | Yes | The referenced person identifier |
| CLICK_DATE | DATE |  |  | Yes | The date on which the person visited the related person's record. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_L0GIN | VARCHAR2 | 32 |  |  | Standard WHO Column: Indicates the last update login. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CLICK_HISTORY_FK1 | Non Unique | Default | RELATED_PERSON_ID |
| PER_CLICK_HISTORY_FK2 | Non Unique | Default | PERSON_ID |
| PER_CLICK_HISTORY_N1 | Non Unique | Default | USER_GUID |
| PER_CLICK_HISTORY_PK | Unique | Default | PERSON_CLICK_HISTORY_ID |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
