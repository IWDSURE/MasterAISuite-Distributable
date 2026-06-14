# WLF_LI_OBSERVERS_F

Content Learning Item Observers

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliobserversf-13049.html#wlfliobserversf-13049](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfliobserversf-13049.html#wlfliobserversf-13049)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LI_OBSERVERS_F_PK | LI_OBSERVER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LI_OBSERVER_ID | NUMBER |  | 18 | Yes | KEY attribute for an observer row of a learning item |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| LEARNING_ITEM_ID | NUMBER |  | 18 | Yes | Learning item id for which observer is created. |
| OBSERVER_ID | NUMBER |  | 18 |  | Observer ID. ie., PERSON_ID |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | enterprise id |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LI_OBSERVERS_F_N1 | Non Unique | Default | LEARNING_ITEM_ID |
| WLF_LI_OBSERVERS_F_U1 | Unique | Default | LI_OBSERVER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
