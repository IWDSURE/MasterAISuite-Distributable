# HRC_SEM_CONFIGURATIONS

This table contains the key value pair for the configurations.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemconfigurations-20868.html#hrcsemconfigurations-20868](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcsemconfigurations-20868.html#hrcsemconfigurations-20868)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_SEM_CONFIGURATIONS_PK | KEY |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| KEY | VARCHAR2 | 255 |  | Yes | This column contains the key of the key value pair configuration. |
| VALUE | VARCHAR2 | 4000 |  |  | This column contains the value of the key value pair configuration. |
| DESCRIPTION | VARCHAR2 | 1024 |  |  | This is the description of the key value pair. |
| PRODUCT | VARCHAR2 | 80 |  |  | This column contains the product information. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRC_SEM_CONFIGURATIONS_U1 | Unique | FUSION_TS_TX_DATA | KEY |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
