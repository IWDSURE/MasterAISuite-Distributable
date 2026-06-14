# PAY_COST_CLASSIFICATIONS

This table contains classifications that group elements based on common costing requirements.

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** TABLE

**Tablespace:** APPS_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostclassifications-8104.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paycostclassifications-8104.html)

## Primary Key

| Name | Columns |
|------|----------|
| PAY_COST_CLASSIFICATIONS_PK | COST_CLASSIFICATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| COST_CLASSIFICATION_ID | NUMBER |  | 18 | Yes | COST_CLASSIFICATION_ID |
| CLASSIFICATION_NAME | VARCHAR2 | 80 |  | Yes | CLASSIFICATION_NAME |
| LEGISLATIVE_DATA_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to PER_LEGISLATIVE_DATA_GROUPS. |
| ENTERPRISE_ID | NUMBER |  | 18 | Yes | Foreign key to PER_ENTERPRISES. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|-------|------------|------------|----------|
| PAY_COST_CLASSIFICATIONS_PK | Unique | Default | COST_CLASSIFICATION_ID |

---

[← Back to HRMS Tables Index](../HRMS_Tables_Index.md)
