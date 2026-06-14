# WLF_CONTENT_DEFAULT_OBSERVERS

Content Learning Item Default Observers

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** wlf_content_default_observers

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentdefaultobservers-22389.html#wlfcontentdefaultobservers-22389](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcontentdefaultobservers-22389.html#wlfcontentdefaultobservers-22389)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_CONTENT_OBSERVERS_PK | DEFAULT_OBSERVER_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| DEFAULT_OBSERVER_ID | NUMBER |  | 18 | Yes | KEY attribute for an observer row of a learning item |
| CONTENT_RULE_ID | NUMBER |  | 18 | Yes | Content rule id for which observer is created. |
| OBSERVER_PERSON_ID | NUMBER |  | 18 | Yes | Observer Person Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_CONTENT_OBSERVERS_N1 | Non Unique | Default | CONTENT_RULE_ID |
| WLF_CONTENT_OBSERVERS_U1 | Unique | Default | DEFAULT_OBSERVER_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
