# PAY_DIR_COMP_DETAILS_F_

This table contains any flexfield data defined for components of the deduction card.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircompdetailsf-13744.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydircompdetailsf-13744.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_DIR_COMP_DETAILS_F_PK_ | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_COMP_DETAIL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DIR_COMP_DETAIL_ID | NUMBER |  | 18 | Yes | DIR_COMP_DETAIL_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| DIR_CARD_COMP_ID | NUMBER |  | 18 |  | DIR_CARD_COMP_ID |
| DIR_COMP_FLEX_ID | NUMBER |  | 18 |  | DIR_COMP_FLEX_ID |
| PERSON_ID | NUMBER |  | 18 |  | PERSON_ID |
| PARENT_DIR_COMP_FLEX_ID | NUMBER |  | 18 |  | PARENT_DIR_COMP_FLEX_ID |
| DIR_INFORMATION_CATEGORY | VARCHAR2 | 80 |  |  | DIR_INFORMATION_CATEGORY |
| DIR_INFORMATION_CHAR1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR16 | VARCHAR2 | 4000 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_CHAR30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER11 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER12 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER13 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER14 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER15 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER16 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER17 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER18 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER19 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_NUMBER20 | NUMBER |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE1 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE2 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE3 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE4 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE5 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE6 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE7 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE8 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE9 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE10 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE11 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE12 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE13 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE14 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| DIR_INFORMATION_DATE15 | DATE |  |  |  | Descriptive Flexfield: segment of the descriptive flexfield. |
| STATUS | VARCHAR2 | 30 |  |  | STATUS |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 |  | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  |  | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  |  | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 |  | Foreign key to PER_ENTERPRISES. |
| AUDIT_ACTION_TYPE_ | VARCHAR2 | 10 |  |  | Action Type - have values like INSERT, UPDATE and DELETE. |
| AUDIT_CHANGE_BIT_MAP_ | VARCHAR2 | 1000 |  |  | Used to store a bit map of 1s and 0s for each column in the table. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_DIR_COMP_DETAILS_FN1_ | Non Unique | Default | DIR_COMP_DETAIL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |
| PAY_DIR_COMP_DETAILS_F_PK_ | Unique | Default | LAST_UPDATE_DATE, LAST_UPDATED_BY, DIR_COMP_DETAIL_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
