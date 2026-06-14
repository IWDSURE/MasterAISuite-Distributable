# WLF_LI_SECTIONS_F

Table to store learning item sections.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflisectionsf-25354.html#wlflisectionsf-25354](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflisectionsf-25354.html#wlflisectionsf-25354)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_SECTIONS_F_PK | SECTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SECTION_ID | NUMBER |  | 18 | Yes | System generated unique identifier. |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 |  | LEARNING_ITEM_ID |
| SECTION_TYPE | VARCHAR2 | 30 |  |  | SECTION_TYPE |
| RENEWAL_TYPE | VARCHAR2 | 30 |  |  | RENEWAL_TYPE |
| COMPLETION_TYPE | VARCHAR2 | 30 |  |  | COMPLETION_TYPE |
| NO_OF_MANDATORY_ITEMS | NUMBER |  |  |  | NO_OF_MANDATORY_ITEMS |
| MANDATORY_FLAG | VARCHAR2 | 3 |  |  | MANDATORY_FLAG |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| INITIAL_LA_STATUS | VARCHAR2 | 32 |  |  | Used to override the Learning assignment status of courses viewed through specilization |
| COMPLETION_RULE_TYPE | VARCHAR2 | 32 |  |  | Column value represents completion rule of section |
| IS_HIDDEN | VARCHAR2 | 1 |  |  | Used to determine the section is visible or not |
| DISPLAY_PREDECESSOR_ID | NUMBER |  | 18 |  | Used to store predecessor section calculated by position |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_SECTIONS_F_N1 | Non Unique | Default | SECTION_TYPE |
| WLF_LI_SECTIONS_F_N2 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_SECTIONS_F_U1 | Unique | Default | SECTION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
