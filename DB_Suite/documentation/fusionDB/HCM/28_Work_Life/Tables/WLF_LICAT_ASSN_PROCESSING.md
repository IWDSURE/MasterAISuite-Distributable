# WLF_LICAT_ASSN_PROCESSING

This table will be used to store processing data setup for mass update of assignment records during learning catalog status update.

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** TABLE

**Tablespace:** WLF_LICAT_ASSN_PROCESSING

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicatassnprocessing-24436.html#wlflicatassnprocessing-24436](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlflicatassnprocessing-24436.html#wlflicatassnprocessing-24436)

## Primary Key

| Name | Columns |
|------|----------|
| WLF_LICAT_ASSN_PROCESSING_PK | LICAT_PROCESSING_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| LICAT_PROCESSING_ID | NUMBER |  | 18 | Yes | System generated unique identifier |
| PROCESS_ID | NUMBER |  | 18 |  | Process Id |
| ASSIGNMENT_CRITERIA | VARCHAR2 | 4000 |  |  | Assignment Criteria |
| ASSIGNMENT_CRITERIA_TYPE | VARCHAR2 | 30 |  |  | Assignment Criteria Type |
| COMMENTS | VARCHAR2 | 4000 |  |  | Comments |
| STATUS | VARCHAR2 | 30 |  |  | Status |
| REASON_CODE | VARCHAR2 | 30 |  |  | Reason Code |
| ACTION | VARCHAR2 | 30 |  |  | Action performed on Learning Catalog |
| DATA_SECURITY_PRIVILEGE | VARCHAR2 | 30 |  |  | Data Security Privilege |
| SOURCE | VARCHAR2 | 30 |  |  | Source |
| SOURCE_ID | NUMBER |  | 18 |  | Source Id |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| WLF_LICAT_ASSN_PROCESSING_U1 | Unique | WLF_LICAT_ASSN_PROCESSING_U1 | LICAT_PROCESSING_ID |

---

[← Back to Index](../28_Work_Life_Tables_Index.md)
