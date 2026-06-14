# WLF_SCORM_SEQUENCING_INFOS_F

Sequencing attributes for a SCORM 2004 content object

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormsequencinginfosf-14034.html#wlfscormsequencinginfosf-14034](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfscormsequencinginfosf-14034.html#wlfscormsequencinginfosf-14034)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_SCORM_SEQUENCING_INFOS_PK | SEQUENCING_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| SEQUENCING_INFO_ID | NUMBER |  | 18 | Yes | SEQUENCING_INFO_ID |
| EFFECTIVE_START_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the beginning of the date range within which the row is effective. |
| EFFECTIVE_END_DATE | DATE |  |  | Yes | Date Effective Entity: indicates the date at the end of the date range within which the row is effective. |
| CONTENT_ID | NUMBER |  | 18 | Yes | CONTENT_ID |
| IS_OBJECTIVES_GLOBAL_TO_SYSTEM | VARCHAR2 | 1 |  |  | IS_OBJECTIVES_GLOBAL_TO_SYSTEM |
| CM_CHOICE | VARCHAR2 | 1 |  |  | CM_CHOICE |
| CM_CHOICE_EXIT | VARCHAR2 | 1 |  |  | CM_CHOICE_EXIT |
| CM_FLOW | VARCHAR2 | 1 |  |  | CM_FLOW |
| CM_FORWARD_ONLY | VARCHAR2 | 1 |  |  | CM_FORWARD_ONLY |
| CM_USE_ATTEMPT_OBJECTIVE | VARCHAR2 | 1 |  |  | CM_USE_ATTEMPT_OBJECTIVE |
| CM_USE_ATTEMPT_PROGRESS | VARCHAR2 | 1 |  |  | CM_USE_ATTEMPT_PROGRESS |
| LC_ATTEMPT_LIMIT | NUMBER |  |  |  | LC_ATTEMPT_LIMIT |
| LC_ATTEMPT_DURATION_LIMIT | NUMBER |  |  |  | LC_ATTEMPT_DURATION_LIMIT |
| ROLLUP_OBJECTIVE_SATISFIED | VARCHAR2 | 1 |  |  | ROLLUP_OBJECTIVE_SATISFIED |
| ROLLUP_PROGRESS_COMPLETION | VARCHAR2 | 1 |  |  | ROLLUP_PROGRESS_COMPLETION |
| ROLLUP_OBJ_MEASURE_WEIGHT | NUMBER |  |  |  | ROLLUP_OBJ_MEASURE_WEIGHT |
| RANDOM_TIMING | VARCHAR2 | 1 |  |  | RANDOM_TIMING |
| RANDOM_SELECT_COUNT | NUMBER |  |  |  | RANDOM_SELECT_COUNT |
| RANDOM_REORDER_CHILDREN | VARCHAR2 | 1 |  |  | RANDOM_REORDER_CHILDREN |
| RANDOM_SELECTION_TIMING | VARCHAR2 | 1 |  |  | RANDOM_SELECTION_TIMING |
| DELIVERY_TRACKED | VARCHAR2 | 1 |  |  | DELIVERY_TRACKED |
| DELIVERY_IS_COMPLETION_SET | VARCHAR2 | 1 |  |  | DELIVERY_IS_COMPLETION_SET |
| DELIVERY_IS_OBJECTIVE_SET | VARCHAR2 | 1 |  |  | DELIVERY_IS_OBJECTIVE_SET |
| PREVENT_ACTIVATION | VARCHAR2 | 1 |  |  | PREVENT_ACTIVATION |
| CONSTRAIN_CHOICE | VARCHAR2 | 1 |  |  | CONSTRAIN_CHOICE |
| ROLLUP_REQD_FOR_SATISFIED | VARCHAR2 | 1 |  |  | ROLLUP_REQD_FOR_SATISFIED |
| ROLLUP_REQD_FOR_NOT_STATISFIED | VARCHAR2 | 1 |  |  | ROLLUP_REQD_FOR_NOT_STATISFIED |
| ROLLUP_REQUIRED_FOR_COMPLETED | VARCHAR2 | 1 |  |  | ROLLUP_REQUIRED_FOR_COMPLETED |
| ROLLUP_REQUIRED_FOR_INCOMPLETE | VARCHAR2 | 1 |  |  | ROLLUP_REQUIRED_FOR_INCOMPLETE |
| ROLLUP_MEAS_SATIS_IF_ACTIVE | VARCHAR2 | 1 |  |  | ROLLUP_MEAS_SATIS_IF_ACTIVE |
| NAV_HIDE_PREVIOUS | VARCHAR2 | 1 |  |  | NAV_HIDE_PREVIOUS |
| NAV_HIDE_CONTINUE | VARCHAR2 | 1 |  |  | NAV_HIDE_CONTINUE |
| NAV_HIDE_EXIT | VARCHAR2 | 1 |  |  | NAV_HIDE_EXIT |
| NAV_HIDE_EXIT_ALL | VARCHAR2 | 1 |  |  | NAV_HIDE_EXIT_ALL |
| NAV_HIDE_ABANDON | VARCHAR2 | 1 |  |  | NAV_HIDE_ABANDON |
| NAV_HIDE_ABANDON_ALL | VARCHAR2 | 1 |  |  | NAV_HIDE_ABANDON_ALL |
| NAV_HIDE_SUSPEND_ALL | VARCHAR2 | 1 |  |  | NAV_HIDE_SUSPEND_ALL |
| IS_DATA_GLOBAL_TO_SYSTEM | VARCHAR2 | 1 |  |  | IS_DATA_GLOBAL_TO_SYSTEM |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | ENTERPRISE_ID |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_SCORM_SEQUENCING_INFOS_N1 | Non Unique | Default | CONTENT_ID |
| WLF_SCORM_SEQUENCING_INFOS_PK | Unique | FUSION_TS_TX_DATA | SEQUENCING_INFO_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
