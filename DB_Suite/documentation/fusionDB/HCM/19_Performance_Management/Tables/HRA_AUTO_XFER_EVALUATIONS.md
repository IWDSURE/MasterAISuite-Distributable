# HRA_AUTO_XFER_EVALUATIONS

This table store the performance documents transferred as part of the manager changes.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraautoxferevaluations-21315.html#hraautoxferevaluations-21315](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraautoxferevaluations-21315.html#hraautoxferevaluations-21315)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_AUTO_XFER_EVALUATIONS_PK | AUTO_XFER_EVALUATION_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_XFER_EVALUATION_ID | NUMBER |  | 18 | Yes | Primary key of the transferred documents. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| AUTO_XFER_MGR_CHG_ID | NUMBER |  | 18 | Yes | Foreign key to HRA_AUTO_XFER_MGR_CHANGES. |
| EVALUATION_ID | NUMBER |  | 18 |  | Foreign key to HRA_EVALUATIONS. Stores the Id of the performance document transferred on which this manager change is performed. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| HRA_AUTO_XFER_EVALUATIONS_N1 | Non Unique | Default | AUTO_XFER_MGR_CHG_ID, EVALUATION_ID |
| HRA_AUTO_XFER_EVALUATIONS_PK | Unique | Default | AUTO_XFER_EVALUATION_ID |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
