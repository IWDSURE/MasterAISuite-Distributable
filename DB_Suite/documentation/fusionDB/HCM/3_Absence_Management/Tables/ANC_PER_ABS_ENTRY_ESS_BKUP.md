# ANC_PER_ABS_ENTRY_ESS_BKUP

This table is to backup the absence entry and absence entry details record information for which duration were modified by ESS evaluate absence job

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** TABLE

**Tablespace:** FUSION_TS_TX_DATA

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentryessbkup-15443.html#ancperabsentryessbkup-15443](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancperabsentryessbkup-15443.html#ancperabsentryessbkup-15443)

## Primary Key

| Name | Columns |
|------|----------|
| ANC_PER_ABS_ENTRY_ESS_BKUP_PK | PER_ABS_ENTRY_ESS_BKUP_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments |
|---|---|---|---|---|---|
| PER_ABS_ENTRY_ESS_BKUP_ID | NUMBER |  | 18 | Yes | Absence entry backup id |
| PER_ABSENCE_ENTRY_ID | NUMBER |  | 18 | Yes | Absence entry id for which backup record is created |
| PERSON_ID | NUMBER |  | 18 | Yes | Person Id |
| BACKUP_RECORD_TYPE | VARCHAR2 | 64 |  | Yes | Backup record type to determine if backup is for absence entry record or absence entry detail record |
| PER_ABS_ENTRY_DTL_ID | NUMBER |  | 18 |  | Absence entry detail if backup is for entry detail record |
| DURATION | NUMBER |  |  |  | Duration of absence entry or detail record - Backed up value |
| DURATION_NEW | NUMBER |  |  |  | New duration value calculated by the ESS process |
| START_DATE_DURATION | NUMBER |  |  |  | Start Date Duration of absence entry - Backed up value |
| START_DATE_DURATION_NEW | NUMBER |  |  |  | New start date duration value calculated by the ESS process |
| END_DATE_DURATION | NUMBER |  |  |  | End Date Duration of absence entry - Backed up value |
| END_DATE_DURATION_NEW | NUMBER |  |  |  | New end date duration value calculated by the ESS process |
| EMPLOYEE_SHIFT_FLAG | VARCHAR2 | 20 |  |  | Employee shift flag of absence entry - Backed up value |
| EMPLOYEE_SHIFT_FLAG_NEW | VARCHAR2 | 20 |  |  | New employee shift flag computed by ESS process |
| ABS_CREATED_BY | VARCHAR2 | 64 |  |  | Created by value of absence entry or detail record - Backed up value |
| ABS_CREATION_DATE | TIMESTAMP |  |  |  | Created date value of absence entry or detail record - Backed up value |
| ABS_LAST_UPDATED_BY | VARCHAR2 | 64 |  |  | Last update by value of absence entry or detail record - Backed up value |
| ABS_LAST_UPDATE_DATE | TIMESTAMP |  |  |  | Last update date value of absence entry or detail record - Backed up value |
| ABS_OBJECT_VERSION | NUMBER |  | 9 |  | Object version number value of absence entry or detail record - Backed up value |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. |

## Indexes

| Index | Uniqueness | Tablespace | Columns |
|---|---|---|---|
| ANC_PER_ABS_ESS_BKUP_N1 | Non Unique | FUSION_TS_TX_DATA | PER_ABSENCE_ENTRY_ID |
| ANC_PER_ABS_ESS_BKUP_U1 | Unique | FUSION_TS_TX_DATA | PER_ABS_ENTRY_ESS_BKUP_ID |

---

[← Back to Index](../3_Absence_Management_Tables_Index.md)
