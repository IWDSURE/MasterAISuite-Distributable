# HRA_AUTO_XFER_MGR_CHANGES

This table store the manager change of a worker which are used to auto transfer in progress performance documents.

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** TABLE

**Tablespace:** Default

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraautoxfermgrchanges-28998.html#hraautoxfermgrchanges-28998](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hraautoxfermgrchanges-28998.html#hraautoxfermgrchanges-28998)

## Primary Key

| Name | Columns |
|------|----------|
| HRA_AUTO_XFER_MGR_CHANGES_PK | AUTO_XFER_MGR_CHG_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| AUTO_XFER_MGR_CHG_ID | NUMBER |  | 18 | Yes | Primary key of the manager change. |
| BUSINESS_GROUP_ID | NUMBER |  | 18 | Yes | Foreign key to HR_ALL_ORGANIZATION_UNITS. |
| PERSON_ID | NUMBER |  | 18 |  | Global Id of the person. Stores the Id of the person on which this manager change is performed. |
| ASSIGNMENT_ID | NUMBER |  | 18 |  | Foreign key to PER_ALL_ASSIGNMENTS_M. Stores the Id of the assignment of the person on which this manager change is performed. |
| OLD_MANAGER_ID | NUMBER |  | 18 |  | Stores the Id of the previous manager on which this manager change is performed. |
| NEW_MANAGER_ID | NUMBER |  | 18 |  | Stores the Id of the new manager on which this manager change is performed. |
| OLD_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the Id of the previous manager's assignment on which this manager change is performed. |
| NEW_MGR_ASSIGNMENT_ID | NUMBER |  | 18 |  | Stores the Id of the new manager's assignment on which this manager change is performed. |
| MANAGER_TYPE | VARCHAR2 | 30 |  |  | Stores the role of the manager for the change manager action. |
| EFFECTIVE_DATE | DATE |  |  |  | Stores the effective date on which this manager change is performed. |
| PROCESSED_DATE | TIMESTAMP |  |  |  | Stores the processing date and time on which this manager change is performed. |
| EVENT_CREATION_DATE | TIMESTAMP |  |  |  | tores the event creation date and time on which this manager change is performed. |
| CHANGE_ID | NUMBER |  | 18 |  | Foreign key to HRC_EVT_OBJ_CHANGES. Stores the Id of the HCM Event created. |
| STATUS | VARCHAR2 | 64 |  |  | Stores the processing status of this manager change. |
| COMMENTS | VARCHAR2 | 4000 |  |  | Stores processing error or comments of this manager change. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HRA_AUTO_XFER_MGR_CHANGES_N1 | Non Unique | Default | BUSINESS_GROUP_ID, EFFECTIVE_DATE |  |
| HRA_AUTO_XFER_MGR_CHANGES_N2 | Non Unique | Default | PERSON_ID, ASSIGNMENT_ID |  |
| HRA_AUTO_XFER_MGR_CHANGES_N3 | Non Unique | Default | OLD_MANAGER_ID, OLD_MGR_ASSIGNMENT_ID |  |
| HRA_AUTO_XFER_MGR_CHANGES_N4 | Non Unique | Default | NEW_MANAGER_ID, NEW_MGR_ASSIGNMENT_ID |  |
| HRA_AUTO_XFER_MGR_CHANGES_N5 | Non Unique | Default | EFFECTIVE_DATE, EVENT_CREATION_DATE, PROCESSED_DATE |  |
| HRA_AUTO_XFER_MGR_CHANGES_N6 | Non Unique | Default | STATUS | Obsolete |
| HRA_AUTO_XFER_MGR_CHANGES_N7 | Non Unique | Default | STATUS |  |
| HRA_AUTO_XFER_MGR_CHANGES_PK | Unique | Default | AUTO_XFER_MGR_CHG_ID |  |

---

[← Back to Index](../19_Performance_Management_Tables_Index.md)
