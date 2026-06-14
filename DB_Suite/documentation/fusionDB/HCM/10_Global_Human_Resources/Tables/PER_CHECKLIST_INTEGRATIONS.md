# PER_CHECKLIST_INTEGRATIONS

Stores the configuration details for various checklist integrations.

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistintegrations-20114.html#perchecklistintegrations-20114](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchecklistintegrations-20114.html#perchecklistintegrations-20114)

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| CHECKLIST_INTEGRATION_ID | NUMBER |  | 18 | Yes | CHECKLIST_INTEGRATION_ID |
| CHECKLIST_INTEGRATION_CODE | VARCHAR2 | 120 |  | Yes | CHECKLIST_INTEGRATION_CODE |
| INTEGRATION_CATEGORY | VARCHAR2 | 80 |  | Yes | INTEGRATION_CATEGORY |
| INTEGRATION_TYPE | VARCHAR2 | 80 |  | Yes | INTEGRATION_TYPE |
| CONTENT_1 | VARCHAR2 | 240 |  |  | CONTENT_1 |
| CONTENT_2 | VARCHAR2 | 240 |  |  | CONTENT_2 |
| CONTENT_3 | VARCHAR2 | 240 |  |  | CONTENT_3 |
| CONTENT_4 | VARCHAR2 | 240 |  |  | CONTENT_4 |
| CONTENT_5 | VARCHAR2 | 240 |  |  | CONTENT_5 |
| CONTENT_6 | VARCHAR2 | 240 |  |  | CONTENT_6 |
| CONTENT_7 | VARCHAR2 | 240 |  |  | CONTENT_7 |
| CONTENT_8 | VARCHAR2 | 240 |  |  | CONTENT_8 |
| CONTENT_9 | VARCHAR2 | 240 |  |  | CONTENT_9 |
| CONTENT_10 | VARCHAR2 | 240 |  |  | CONTENT_10 |
| CONTENT_11 | VARCHAR2 | 240 |  |  | CONTENT_11 |
| CONTENT_12 | VARCHAR2 | 240 |  |  | CONTENT_12 |
| CONTENT_13 | VARCHAR2 | 240 |  |  | CONTENT_13 |
| CONTENT_14 | VARCHAR2 | 240 |  |  | CONTENT_14 |
| CONTENT_15 | VARCHAR2 | 240 |  |  | CONTENT_15 |
| CONTENT_16 | VARCHAR2 | 240 |  |  | CONTENT_16 |
| CONTENT_17 | VARCHAR2 | 240 |  |  | CONTENT_17 |
| CONTENT_18 | VARCHAR2 | 240 |  |  | CONTENT_18 |
| CONTENT_19 | VARCHAR2 | 240 |  |  | CONTENT_19 |
| CONTENT_20 | VARCHAR2 | 240 |  |  | CONTENT_20 |
| CONTENT_21 | VARCHAR2 | 240 |  |  | CONTENT_21 |
| CONTENT_22 | VARCHAR2 | 240 |  |  | CONTENT_22 |
| CONTENT_23 | VARCHAR2 | 240 |  |  | CONTENT_23 |
| CONTENT_24 | VARCHAR2 | 240 |  |  | CONTENT_24 |
| CONTENT_25 | VARCHAR2 | 240 |  |  | CONTENT_25 |
| CONTENT_26 | VARCHAR2 | 240 |  |  | CONTENT_26 |
| CONTENT_27 | VARCHAR2 | 240 |  |  | CONTENT_27 |
| CONTENT_28 | VARCHAR2 | 240 |  |  | CONTENT_28 |
| CONTENT_29 | VARCHAR2 | 240 |  |  | CONTENT_29 |
| CONTENT_30 | VARCHAR2 | 240 |  |  | CONTENT_30 |
| MAPPING_1 | VARCHAR2 | 80 |  |  | MAPPING_1 |
| MAPPING_2 | VARCHAR2 | 80 |  |  | MAPPING_2 |
| MAPPING_3 | VARCHAR2 | 80 |  |  | MAPPING_3 |
| MAPPING_4 | VARCHAR2 | 80 |  |  | MAPPING_4 |
| MAPPING_5 | VARCHAR2 | 80 |  |  | MAPPING_5 |
| MAPPING_6 | VARCHAR2 | 80 |  |  | MAPPING_6 |
| MAPPING_7 | VARCHAR2 | 80 |  |  | MAPPING_7 |
| MAPPING_8 | VARCHAR2 | 80 |  |  | MAPPING_8 |
| MAPPING_9 | VARCHAR2 | 80 |  |  | MAPPING_9 |
| MAPPING_10 | VARCHAR2 | 80 |  |  | MAPPING_10 |
| MAPPING_11 | VARCHAR2 | 80 |  |  | MAPPING_11 |
| MAPPING_12 | VARCHAR2 | 80 |  |  | MAPPING_12 |
| MAPPING_13 | VARCHAR2 | 80 |  |  | MAPPING_13 |
| MAPPING_14 | VARCHAR2 | 80 |  |  | MAPPING_14 |
| MAPPING_15 | VARCHAR2 | 80 |  |  | MAPPING_15 |
| MAPPING_16 | VARCHAR2 | 80 |  |  | MAPPING_16 |
| MAPPING_17 | VARCHAR2 | 80 |  |  | MAPPING_17 |
| MAPPING_18 | VARCHAR2 | 80 |  |  | MAPPING_18 |
| MAPPING_19 | VARCHAR2 | 80 |  |  | MAPPING_19 |
| MAPPING_20 | VARCHAR2 | 80 |  |  | MAPPING_20 |
| MAPPING_21 | VARCHAR2 | 80 |  |  | MAPPING_21 |
| MAPPING_22 | VARCHAR2 | 80 |  |  | MAPPING_22 |
| MAPPING_23 | VARCHAR2 | 80 |  |  | MAPPING_23 |
| MAPPING_24 | VARCHAR2 | 80 |  |  | MAPPING_24 |
| MAPPING_25 | VARCHAR2 | 80 |  |  | MAPPING_25 |
| MAPPING_26 | VARCHAR2 | 80 |  |  | MAPPING_26 |
| MAPPING_27 | VARCHAR2 | 80 |  |  | MAPPING_27 |
| MAPPING_28 | VARCHAR2 | 80 |  |  | MAPPING_28 |
| MAPPING_29 | VARCHAR2 | 80 |  |  | MAPPING_29 |
| MAPPING_30 | VARCHAR2 | 80 |  |  | MAPPING_30 |
| ENABLED_FLAG | VARCHAR2 | 30 |  | Yes | ENABLED_FLAG |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | BUSINESS_GROUP_ID |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| PER_CHECKLISTS_INTEGRATIONS_PK | Unique | Default | CHECKLIST_INTEGRATION_ID |
| PER_CHECKLISTS_INTEGRATION_N1 | Non Unique | Default | CHECKLIST_INTEGRATION_CODE |
| PER_CHECKLIST_INTEGRATIONS_N2 | Non Unique | Default | INTEGRATION_CATEGORY, INTEGRATION_TYPE |

---

[← Back to Index](../10_Global_Human_Resources_Tables_Index.md)
