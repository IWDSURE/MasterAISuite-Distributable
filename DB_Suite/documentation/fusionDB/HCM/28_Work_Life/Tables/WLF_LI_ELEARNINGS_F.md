# WLF_LI_ELEARNINGS_F

This table is used to store elearning items information.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflielearningsf-28074.html#wlflielearningsf-28074](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflielearningsf-28074.html#wlflielearningsf-28074)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_ELEARNINGS_F_PK | ELEARNING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| ELEARNING_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| ELEARNING_TYPE | VARCHAR2 | 64 |  |  | This column is used to represents different elearning item types |
| ELEARNING_CATEGORY | VARCHAR2 | 30 |  |  | Column used to differentiate elearning types denormalized from learning_item_category |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | This column behaves as foriegn key and  refers to parent table column |
| SOURCE_TYPE | VARCHAR2 | 30 |  |  | This column populates source_type of elearning for category |
| CREATED_BY_ID | NUMBER |  | 18 | Yes | Indicates the person identifier who created the object. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Identifier of Enterprise, used for multi-tenancy partitioning. Foreign key to HR_ORGANIZATION_UNITS. |
| RELATED_CONTENT_ID | NUMBER |  | 18 |  | This is column holds value of content LEARNING_ITEM_ID from WLF_LEARNING_ITEMS_F table of ORA_CONTENT_ROOT learning item type related to ELearning |
| CONTENT_DELETE_REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for content deletion |
| CONTENT_DELETE_DATE | TIMESTAMP |  |  |  | Content Delete Date |
| CAPACITY_ENABLED | VARCHAR2 | 30 |  |  | Property to represent if capacity is enabled |
| CAPACITY_MINIMUM | NUMBER |  | 18 |  | Minimum capacity setting |
| CAPACITY_MAXIMUM | NUMBER |  | 18 |  | Maximum capacity setting |
| WAITLIST_ENABLED | VARCHAR2 | 30 |  |  | Property to represent if waitlist is enabled |
| WAITLIST_MAXIMUM_ENABLED | VARCHAR2 | 30 |  |  | Property to represent if waitlist maximum capacity is enabled |
| WAITLIST_MAXIMUM | NUMBER |  | 18 |  | Maximum waitlist setting |
| WAITLIST_RULE | VARCHAR2 | 30 |  |  | Waitlisting rule on who can add learners to waitlist |
| TRAINING_SUPPLIER_ID | NUMBER |  | 18 |  | Training supplier id |
| PARENT_LEARNING_ITEM_ID | NUMBER |  | 18 |  | Indicates the Parent (Ex : Course) Learning Item Id to which Event is associated with. |
| CLOSED_DATE | TIMESTAMP |  |  |  | Learning Item closed date |
| CLOSED_ACTIVITY_STATUS | VARCHAR2 | 30 |  |  | Operation for closed event |
| CLOSED_REASON_CODE | VARCHAR2 | 30 |  |  | Reason code for closed event |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_ELEARNINGS_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_ELEARNINGS_F_N2 | Non Unique | Default | RELATED_CONTENT_ID |
| WLF_LI_ELEARNINGS_F_N3 | Non Unique | Default | CONTENT_DELETE_DATE |
| WLF_LI_ELEARNINGS_F_U1 | Unique | Default | ELEARNING_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
