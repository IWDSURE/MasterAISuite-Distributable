# CEL_POST_RUN_ELEMENTS

Stores details of elements selected to post in a transfer process run.

## Details

**Schema:** FUSION

**Object owner:** CEL

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpostrunelements-7072.html#celpostrunelements-7072](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/celpostrunelements-7072.html#celpostrunelements-7072)

## Primary Key

| Name | Columns |
|------|----------|
| CEL_POST_RUN_ELEMENTS_PK | RUN_ELEMENT_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| RUN_ELEMENT_ID | NUMBER |  | 18 | Yes | Unique identifier of an element in a transfer process run |
| RUN_ID | NUMBER |  | 18 | Yes | Run identifier |
| ELEMENT_TYPE_ID | NUMBER |  | 18 |  | Element type identifier |
| INPUT_VALUE_ID | NUMBER |  | 18 |  | Input value identifier |
| LEGISLATIVE_GROUP_ID | NUMBER |  | 18 |  | Legislative data group identifier |
| LEGISLATION_CODE | VARCHAR2 | 30 |  |  | Legislation code |
| LEGAL_ENTITY_ID | NUMBER |  | 18 |  | Legal entity identifier |
| INPUT_CURRENCY_CODE | VARCHAR2 | 15 |  |  | Input currency code |
| POSTING_DATE_CODE | VARCHAR2 | 30 |  |  | Code that indicates date behavior selected for posting |
| POSTING_DATE | DATE |  |  |  | Posting date specified |
| FIXED_VALUE | NUMBER |  |  |  | Fixed value for the element entry |
| MINIMUM_VALUE | NUMBER |  |  |  | Minimum allowed value for the element entry |
| MAXIMUM_VALUE | NUMBER |  |  |  | Maximum allowed value for the element entry |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| CEL_POST_RUN_ELEMENTS_N1 | Non Unique | Default | RUN_ID |
| CEL_POST_RUN_ELEMENTS_PK | Unique | Default | RUN_ELEMENT_ID |

---

[← Back to Index](../6_Celebrate_Tables_Index.md)
